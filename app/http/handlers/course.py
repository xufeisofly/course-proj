# coding: utf-8

from flask import Blueprint, jsonify, render_template
from app.controllers.course1_controller import get_bls_elect_info_list, get_bls_block_info_list

course_router = Blueprint('course_router', __name__)

@course_router.route('/course1/elect_info_list')
def elect_info_list():
    elect_infos = get_bls_elect_info_list()
    return render_template('course1/elect_info_list.html', elect_infos=elect_infos)

@course_router.route('/course1/block_info_list')
def block_info_list():
    block_infos = get_bls_block_info_list()
    return render_template('course1/block_info_list.html', block_infos=block_infos)