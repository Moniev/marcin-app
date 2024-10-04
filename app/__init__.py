from asgiref.wsgi import WsgiToAsgi
import asyncio
from app.settings import DATABASE_URL, MAIL_ADDRESS, MAIL_SERVER_PASSWORD
from flask_login import LoginManager
from flask import Flask
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from typing import Union


'''WEB SERVER GATEWAY INTERFACE OBJECT'''
app = Flask(__name__)


'''WRAPPED WSGI TO ASGI'''
asgi_app: Flask = WsgiToAsgi(app)


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
    except:
        return False
    
    
'''CONNECTION VARIABLE'''    
connection: Union[AsyncEngine, bool] = makeAsyncConnection()


'''ASYNC POSTGRES INITIALIZATION'''
async def createDatabase() -> None:
    connection: AsyncEngine = makeAsyncConnection()
    if connection:
        async with connection.begin() as _connection:
            '''IMPORTING MODELS GOES HERE'''
            # FULLFILL YOUR DUTY WITH PROPER MODELS IMPORTS
            ''' ^^^ ^^^ ^^^ ^^^  ^^^ ^^^ '''
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
    
    '''LOGIN MANAGER'''
    login_manager: LoginManager = LoginManager()
    login_manager.login_view = f"auth.login"
    login_manager.login_message_category = f"warning"
    login_manager.login_message = f"log in to proceed"
    login_manager.init_app(app)
    
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
    app.config["MAIL_ADRRESS"] = MAIL_ADDRESS
    app.config["MAIL_SERVER_PASSWORD"] = MAIL_SERVER_PASSWORD
    
    '''REGISTER BLUEPRINTS'''
    from .auth import auth
    from .views import views
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views, url_prefix=f"/views")
    
    
    return app