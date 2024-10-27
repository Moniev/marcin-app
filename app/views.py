from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint, render_template
from flask_cors import cross_origin

views: Blueprint = Blueprint("views", __name__)

@views.route("/home")
@cross_origin()
async def home() -> str:
    return {}


@views.route("/calendar")
@cross_origin()
async def calendar() -> str:
    return {}

