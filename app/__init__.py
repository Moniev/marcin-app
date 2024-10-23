import asyncio
from app.settings import DATABASE_URL, MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER, MAIL_PORT, MAIL_USE_SSL, MAIL_USE_TLS
from flask_login import LoginManager
from flask import Flask
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


'''REQUESTS FOR A CONNECTION TO DATABASE'''
def makeAsyncConnection() -> Union[AsyncEngine, bool]:
    try: 
        db = create_async_engine(
            url=DATABASE_URL,
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
    '''LOGIN MANAGER'''
    login_manager: LoginManager = LoginManager()
    login_manager.login_view = f"auth.login"
    login_manager.login_message_category = f"warning"
    login_manager.login_message = f"log in to proceed"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id: str):
        return User.query.get(int(id))
    
    '''DATABASE CREATION'''
    if connection:
        asyncio.run(createDatabase())
    else:
        print(f" * No connection to database")
    
    '''CONFIGS'''
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_BINDS"] = {
        "DB": DATABASE_URL,
        }
    app.config["MAIL_SERVER"] = MAIL_SERVER
    app.config["MAIL_USERNAME"] = MAIL_USERNAME
    app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
    app.config["MAIL_SERVER_PASSWORD"] = MAIL_PASSWORD
    app.config["MAIL_PORT"] = MAIL_PORT
    app.config["MAIL_USE_TLS"] = MAIL_USE_TLS
    app.config["MAIL_USE_SSL"] = MAIL_USE_SSL
    
    '''REGISTER BLUEPRINTS'''
    from .auth import auth
    from .views import views
    from .smtp import smtp
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views, url_prefix="/views")
    app.register_blueprint(smtp, url_prefix="/smtp")
    
    return app