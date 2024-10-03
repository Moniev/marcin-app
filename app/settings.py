import pathlib

'''BASE_DIR PATH'''
BASE_DIR = pathlib.Path(__file__).parent

'''POSTGRES CONNECTION STRING'''
DATABASE_URL = f"postgresql+asyncpg://user:password@ip:5432/database_name"

''' SMTP DATA'''
MAIL_ADDRESS = f""
MAIL_SERVER_PASSWORD = f""
