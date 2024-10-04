from app import createApp
from flask import Flask, url_for, redirect


app: Flask = createApp()


@app.route('/')
async def index():
    return redirect(url_for('views.landingPage'))

if __name__ == "__main__":
    app.run()