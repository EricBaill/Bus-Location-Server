# -*- coding: utf-8 -*-
import requests
from flask import jsonify
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument(name='entity_name',type=str)
parser.add_argument(name='start_time',type=str)
parser.add_argument(name='end_time',type=str)

class GetDistance(Resource):
    def post(self):
        #车辆起始点和结束点的距离
        parse = parser.parse_args()
        entity_name = parse.get('entity_name')
        start_time = parse.get('start_time')
        end_time = parse.get('end_time')

        url = 'http://yingyan.baidu.com/api/v3/track/getdistance?ak=GPccFSSW7vYUNcSpoKCzzGNsRxNGGyf1&service_id=208883&entity_name={}&start_time={}&end_time={}&is_processed=1&process_option=need_denoise=1,need_mapmatch=0,radius_threshold=0,transport_mode=driving&supplement_mode=driving'.format(entity_name,start_time,end_time)

        response = requests.get(url)
        resData = response.json()
        return jsonify(resData)