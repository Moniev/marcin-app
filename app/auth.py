from app import asyncSessionLoader
from crud import CRUD 
import datetime
from flask import Blueprint

auth: Blueprint = Blueprint("auth", __name__)

@auth.route("/login")
async def login():
    return 

