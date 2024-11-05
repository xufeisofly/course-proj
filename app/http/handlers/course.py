# coding: utf-8

from flask import Blueprint, jsonify, render_template
from app.controllers.course1_controller import get_bls_elect_info_list

course_router = Blueprint('course_router', __name__)

@course_router.route('/course1')
def course1():
    elect_infos = get_bls_elect_info_list();
    return render_template('course1/index.html', elect_infos=elect_infos)

@course_router.route('/course1/bls_elect_info_list')
def bls_elect_info_list():
    return jsonify({'data': get_bls_elect_info_list()})