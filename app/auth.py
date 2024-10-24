from app import asyncSessionLoader
from app.utils import measureExecutionTime
import app.crud
import datetime
from flask import Blueprint, render_template
from flask_login import login_required, logout_user, current_user


auth: Blueprint = Blueprint("auth", __name__)

@auth.route("/login")
async def login() -> str:
    return  render_template("login.html")

@login_required
@auth.route("/adminPage")
async def adminPage() -> str:
    return render_template("AdminPage.html")