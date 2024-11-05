# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import logging
# import os

# from app.controllers.data_controller import save_data_organized_by_date
# from app.http.schemas.tdms import TdmsDataSchema
# from flask import Blueprint, current_app, jsonify, request

# data_router = Blueprint('data_router', __name__)


# @data_router.route('/report', methods=['POST'])
# def report():
#     try:
#         payload = request.get_json()

#         input = TdmsDataSchema().dump(payload)
#         save_data_organized_by_date(
#             input.data,
#             os.path.join(current_app.config['BASE_DIR'], 'data', input.data['type']),
#             max_num=100,
#             compress=True,
#             file_rotate_size_kb=1024)
#     except Exception as e:
#         logging.error(e)
#         return jsonify({
#             'status': False,
#             'message': str(e),
#         })

#     return jsonify({'status': True})
