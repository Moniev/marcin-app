from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint
from flask_login import login_required, logout_user, current_user


smtp: Blueprint = Blueprint("smtp", __name__)


@smtp.route("/sendContactEmail")
async def sendContactEmail():
    pass

@login_required
@smtp.route("/sendAdvertisementEmail")
async def sendAdvertisementEmail():
    pass 