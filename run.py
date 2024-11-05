import logging
import os

from flask import Flask, request

# from app.http.handlers.data_report import data_router
from app.http.handlers.hello import hello_router
from app.http.handlers.course import course_router

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['BASE_DIR'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.register_blueprint(hello_router)
app.register_blueprint(course_router)
# app.register_blueprint(data_router, url_prefix='/data')
