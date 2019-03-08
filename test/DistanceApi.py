# -*- coding: utf-8 -*-
import requests
from flask_restful import Resource, reqparse
from math import*


parser = reqparse.RequestParser()
parser.add_argument(name='start',type=str)
parser.add_argument(name='end',type=str)

class Distance(Resource):
    def post(self):
        parse = parser.parse_args()
        start = parse.get('start')
        end = parse.get('end')

        print(start)
        print(end)

        url1 = "http://api.map.baidu.com/geocoder?address=" + start + "&output=json&ak=GPccFSSW7vYUNcSpoKCzzGNsRxNGGyf1"
        response = requests.get(url1)
        answer = response.json()
        startlng = answer['result']['location']['lng']
        startlat = answer['result']['location']['lat']

        url2 = "http://api.map.baidu.com/geocoder?address=" + end + "&output=json&ak=GPccFSSW7vYUNcSpoKCzzGNsRxNGGyf1"
        response = requests.get(url2)
        answer = response.json()
        endlng = answer['result']['location']['lng']
        endlat = answer['result']['location']['lat']

        print('startlat：%s'%startlat)
        print('startlng：%s'%startlng)
        print('endlat：%s'%endlat)
        print('endlng：%s'%endlng)

        ra = 6378.140
        rb = 6356.755
        flatten = (ra - rb) / ra
        rad_lat_A = radians(startlat)
        rad_lng_A = radians(startlng)
        rad_lat_B = radians(endlat)
        rad_lng_B = radians(endlng)
        pA = atan(rb / ra * tan(rad_lat_A))
        pB = atan(rb / ra * tan(rad_lat_B))
        xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
        c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
        c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
        dr = flatten / 8 * (c1 - c2)
        distance = ra * (xx + dr)
        return ('距离={0:.3f} km'.format(distance))

