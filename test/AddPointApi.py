# -*- coding: utf-8 -*-
import requests
from flask_restful import Resource, reqparse

#获取GPS信息
parser = reqparse.RequestParser()
parser.add_argument(name='entity_name',type=str)
parser.add_argument(name='latitude',type=str)
parser.add_argument(name='longitude',type=str)
parser.add_argument(name='loc_time',type=str)
parser.add_argument(name='speed',type=str)
parser.add_argument(name='direction',type=str)

#车辆轨迹上传
class AddPoint(Resource):
    def post(self):
        ak = 'GPccFSSW7vYUNcSpoKCzzGNsRxNGGyf1'
        service_id = 208883
        coord_type_input = 'wgs84'

        parse = parser.parse_args()
        entity_name = parse.get('entity_name')
        latitude = parse.get('latitude')
        longitude = parse.get('longitude')
        loc_time = parse.get('loc_time')
        speed = parse.get('speed')
        direction = parse.get('direction')

        data = {
            'ak':ak,
            'service_id':service_id,
            'entity_name':entity_name,
            'latitude':latitude,
            'longitude':longitude,
            'loc_time':loc_time,
            'coord_type_input':coord_type_input,
            'speed':speed,
            'direction':direction,
        }

        url = 'http://yingyan.baidu.com/api/v3/track/addpoint'
        response = requests.post(url,data)
        json = response.json()
        return json

