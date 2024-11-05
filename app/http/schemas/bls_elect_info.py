# coding: utf-8
import time

from marshmallow import Schema, fields



class BlsElectInfoSchema(Schema):
    id = fields.String()
    elect_height = fields.Integer()
    shard_id = fields.Integer()
    member_idx = fields.Integer()
    contribution_map = fields.String()
    local_sk = fields.String()
    common_pk = fields.String()