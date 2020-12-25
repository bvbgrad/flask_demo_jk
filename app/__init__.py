from datetime import datetime as dt
import os
import logging
from flask import Flask


app = Flask(__name__)

# configure the app
app.config.from_object('app.instance.config.BaseConfig')
if app.env == "development":
    app.config.from_object('app.instance.config.DevelopmentConfig')
    logging.basicConfig(level=logging.DEBUG)
elif app.env == "test":
    app.config.from_object('app.instance.config.TestConfig')
    logging.basicConfig(level=logging.DEBUG)
elif app.env == "production":
    app.config.from_object('app.instance.config.ProductionConfig')

logging.info("Flask Application initialized")


@app.route("/", methods=["GET"])
def return_home():
    try:
        hostname = os.environ['HOSTNAME']
    except Exception:
        hostname = 'demo'
    current_time = dt.now().strftime("%Y%m%d %H:%M:%S")
    msg = f"<h3>Flask host '{hostname}', time = {current_time}</h3>"
    return msg, 200
