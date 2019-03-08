
# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from math import*

from App.models import Station0, Station1

parser = reqparse.RequestParser()
parser.add_argument(name='lngr',type=float)
parser.add_argument(name='latr',type=float)


#根据用户位置信息，计算最近站点
class RecentStation(Resource):
    def post(self):
        list_ = []
        list_0 = []
        list_1 = []
        parse = parser.parse_args()
        #获取用户的经纬度信息
        lngr = parse.get('lngr')
        latr = parse.get('latr')

        stations0 = Station0.query.all()
        stations1 = Station1.query.all()

        for station0 in stations0:
            for station1 in stations1:

                lngs0 = float(station0.lng)
                lats0 =float(station0.lat)

                lngr, latr, lngs0, lats0 = map(radians, [lngr, latr, lngs0, lats0])
                dlon = lngs0 - lngr
                dlat = lats0 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats0) * sin(dlon / 2) ** 2
                distance0 = 2 * asin(sqrt(a)) * 6371 * 1000


                lngs1 = float(station1.lng)
                lats1 = float(station1.lat)

                lngr, latr, lngs1, lats1 = map(radians, [lngr, latr, lngs1, lats1])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance1 = 2 * asin(sqrt(a)) * 6371 * 1000

                list_0.append(distance0)
                list_1.append(distance1)
                list_0.sort()
                list_1.sort()
                if list_0[0] == distance0 and list_1[0] == distance1:
                    data = {
                        'station0': station0.name,
                        'direction0': station0.direction,
                        'station1': station1.name,
                        'direction1': station1.direction,
                    }
                    list_.append(data)
        return jsonify(list_)
