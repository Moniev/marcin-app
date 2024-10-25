import asyncio
from dotenv import load_dotenv
from flask_login import LoginManager
from flask import Flask
import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from typing import Union
from flask_mail import Mail
 
'''WEB SERVER GATEWAY INTERFACE OBJECT'''
app = Flask(__name__)


'''BASE CLASS FOR DATABASE MODELS'''
class Base(DeclarativeBase):
    pass


load_dotenv()

'''REQUESTS FOR A CONNECTION TO DATABASE'''
def makeAsyncConnection() -> Union[AsyncEngine, bool]:
    try: 
        db = create_async_engine(
            url=os.getenv("DATABASE_URL"),
            echo=True,
            poolclass=NullPool,
        )
        return db
    except Exception as e:
        print(e)
        return False
    
    
'''CONNECTION VARIABLE'''    
connection: Union[AsyncEngine, bool] = makeAsyncConnection()


'''ASYNC POSTGRES INITIALIZATION'''
async def createDatabase() -> None:
    connection: AsyncEngine = makeAsyncConnection()
    if connection:
        async with connection.begin() as _connection:
            from .models import Customer, Task, TaskIncome, TaskLocation, User
            await _connection.run_sync(Base.metadata.create_all)
        await connection.dispose()

'''ASYNC POSTGRES SESSION OBJECT'''
def asyncSessionLoader() -> async_sessionmaker[AsyncSession]:
    if connection:
        session = async_sessionmaker(
            bind=connection,
            expire_on_commit=False
        )
        return session
    
'''APP'''
def createApp() -> Flask:
    from .models import User
    from .crud import getUserbyId
    
    '''LOGIN MANAGER'''
    login_manager: LoginManager = LoginManager()
    login_manager.login_view = f"auth.login"
    login_manager.login_message_category = f"warning"
    login_manager.login_message = f"log in to proceed"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id: str):
        return getUserbyId(async_session=asyncSessionLoader(), id=(int(id)))
    
    '''DATABASE CREATION'''
    if connection:
        asyncio.run(createDatabase())
    else:
        print(f" * No connection to database")
    
    '''CONFIGS'''
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_BINDS"] = {
        "DB": os.getenv("DATABASE_URL"),
        }
    app.config["MAIL_SERVER"] =os.getenv("MAIL_SERVER")
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_SERVER_PASSWORD"] = os.getenv("MAIL_SERVER")
    app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
    app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS")
    app.config["MAIL_USE_SSL"] = os.getenv("MAIL_USE_SLL")
    
    '''REGISTER BLUEPRINTS'''
    from .auth import auth
    from .views import views
    from .smtp import smtp
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views, url_prefix="/views")
    app.register_blueprint(smtp, url_prefix="/smtp")
    
    return app