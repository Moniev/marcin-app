from app import asyncSessionLoader
from crud import CRUD 
import datetime
from flask import Blueprint

views: Blueprint = Blueprint("views", __name__)

@views.route("/landingPage")
async def landingPage():
    return 