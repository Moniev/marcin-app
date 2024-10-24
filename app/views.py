from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint, render_template


views: Blueprint = Blueprint("views", __name__)

@views.route("/home")
async def home() -> str:
    return render_template("home.html")


@views.route("/calendar")
async def calendar() -> str:
    return render_template("calendar.html")

