import pathlib

'''BASE_DIR PATH'''
BASE_DIR = pathlib.Path(__file__).parent

'''POSTGRES CONNECTION STRING'''
DATABASE_URL = f"postgresql+asyncpg://u7prj23fn6atav:p1f0eaeb780fbbb7f30619d2b6561279b58d87161c7f845eae7cdeedcedd0a345@clhtb6lu92mj2.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/daacp5etuqvpde"

''' SMTP DATA'''
MAIL_SERVER = ""
MAIL_USERNAME = f"A@B.com"
MAIL_PASSWORD = f""
MAIL_PORT = "465"
MAIL_USE_TLS = False
MAIL_USE_SSL = True