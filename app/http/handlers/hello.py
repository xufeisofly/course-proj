# coding: utf-8

from flask import Blueprint, jsonify, render_template

hello_router = Blueprint('hello_router', __name__)

@hello_router.route('/hello')
def hello():
    return jsonify({
        "msg": "hello",
    })

@hello_router.route('/home')
def home():
    name = "world"
    return render_template('index.html', name=name)