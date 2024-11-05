# coding: utf-8
import time

from marshmallow import Schema, fields


class RootSchema(Schema):
    name = fields.String()
    title = fields.String()
    author = fields.String()
    description = fields.String()


class BaseGroupSchema(Schema):
    name = fields.Method('get_name')
    timestamp = fields.Integer()
    channels = fields.List(fields.Dict)

    def get_name(self, obj):
        if obj.get('name', '') == '':
            return str(int(time.time()*1000))


class StrainGroupSchema(BaseGroupSchema):
    """应变 group extra 参数
    """
    sensor_num = fields.Integer(required=True)


class TdmsDataSchema(Schema):
    root = fields.Nested(RootSchema)
    group = fields.Method('get_group')
    type = fields.String(required=True)

    def get_group(self, obj):
        if obj.get('type') == 'strain':
            return StrainGroupSchema().dump(obj.get('group'))




