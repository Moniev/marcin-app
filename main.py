from app import createApp
from flask import Flask, url_for, redirect


app: Flask = createApp()


@app.route('/')
async def index():
    return redirect(url_for("views.home"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)