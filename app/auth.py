from app import asyncSessionLoader
from app.utils import measureExecutionTime
from app.crud import CRUD 
import datetime
from flask import Blueprint, render_template

auth: Blueprint = Blueprint("auth", __name__)

@auth.route("/login")
async def login():
    return 

