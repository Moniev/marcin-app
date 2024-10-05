from app import asyncSessionLoader
from app.utils import measureExecutionTime
from app.crud import CRUD 
import datetime
from flask import Blueprint, render_template

views: Blueprint = Blueprint("views", __name__)

@views.route("/landingPage")
async def landingPage():
    return