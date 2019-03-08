# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse
from math import*
from App.models import BusInfo1, StationTow0, StationTow1, db


#打开App显示车的位置
class Bus1InfoResource(Resource):
    def get(self,direction):
        list_s = []
        buses = BusInfo1.query.filter(BusInfo1.direction==direction).all()
        stations = StationTow0.query.all()
        stations1 = StationTow1.query.all()

        if direction == '0':
            for bus in buses:

                lngbus = float(bus.lng)
                latbus = float(bus.lat)

                lats = float(stations[0].lat)
                lngs = float(stations[0].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance01 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[1].lat)
                lngs = float(stations[1].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance02 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[2].lat)
                lngs = float(stations[2].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance03 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[3].lat)
                lngs = float(stations[3].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance04 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[4].lat)
                lngs = float(stations[4].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance05 = 2 * asin(sqrt(a)) * 6371 * 1000


                list_ = [distance01, distance02, distance03, distance04, distance05]
                list_.sort()
                if list_[0] == distance01:
                    data = {
                        'bus': bus.name,
                        'station': stations[0].name,
                        'distance': distance01,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance02:
                    data = {
                        'bus': bus.name,
                        'station': stations[1].name,
                        'distance': distance02,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance03:
                    data = {
                        'bus': bus.name,
                        'station': stations[2].name,
                        'distance': distance03,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance04:
                    data = {
                        'bus': bus.name,
                        'station': stations[3].name,
                        'distance': distance04,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance05:
                    data = {
                        'bus': bus.name,
                        'station': stations[4].name,
                        'distance': distance05,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                else:
                    pass
                list_s.append(data)

            return jsonify(list_s)


        elif direction == '1':
            for bus in buses:

                lngbus = float(bus.lng)
                latbus = float(bus.lat)

                lats = float(stations1[0].lat)
                lngs = float(stations1[0].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance01 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[1].lat)
                lngs = float(stations1[1].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance02 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[2].lat)
                lngs = float(stations1[2].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance03 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[3].lat)
                lngs = float(stations1[3].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance04 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[4].lat)
                lngs = float(stations1[4].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance05 = 2 * asin(sqrt(a)) * 6371 * 1000



                list_ = [distance01, distance02, distance03, distance04, distance05]
                list_.sort()
                if list_[0] == distance01:
                    data = {
                        'bus': bus.name,
                        'station': stations[0].name,
                        'distance': distance01,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance02:
                    data = {
                        'bus': bus.name,
                        'station': stations[1].name,
                        'distance': distance02,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance03:
                    data = {
                        'bus': bus.name,
                        'station': stations[2].name,
                        'distance': distance03,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance04:
                    data = {
                        'bus': bus.name,
                        'station': stations[3].name,
                        'distance': distance04,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance05:
                    data = {
                        'bus': bus.name,
                        'station': stations[4].name,
                        'distance': distance05,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                else:
                    pass
                list_s.append(data)

            return jsonify(list_s)
        else:
            pass

#获取所有车辆信息
class GetBus1Infos(Resource):
    def get(self):
        list_ = []
        buses = BusInfo1.query.all()
        if buses:
            for bus in buses:
                data = {
                    'id':bus.id,
                    'name':bus.name,
                    'latitude':bus.lat,
                    'longitude':bus.lng,
                    'direction':bus.direction,
                    'number': bus.number,
                    'feescale': bus.feescale,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify({})

parser = reqparse.RequestParser()
parser.add_argument(name='id', type=int)
parser.add_argument(name='name', type=str)
parser.add_argument(name='number', type=str)
parser.add_argument(name='feescale', type=float)

#添加车辆信息
class AddBus1Infos(Resource):
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        number = parse.get('number')
        feescale = parse.get('feescale')
        bus = BusInfo1()
        bus.name = name
        bus.number = number
        bus.feescale = feescale
        db.session.add(bus)
        db.session.commit()
        buss = BusInfo1.query.filter(BusInfo1.name==name).first()
        data = {
            'id': buss.id,
            'name': name,
            'number':number,
            'feescale':feescale,
        }
        return jsonify(data)

#修改车里信息
class PutBus1Infos(Resource):
    def put(self):
        parse = parser.parse_args()
        id = parse.get('id')
        name = parse.get('name')
        number = parse.get('number')
        feescale = parse.get('feescale')
        bus = BusInfo1.query.filter(BusInfo1.id==id).first()
        if bus:
            bus.name = name
            bus.number = number
            bus.feescale = feescale
            db.session.commit()
            data = {
                'id': id,
                'name': name,
                'number': number,
                'feescale': feescale,
            }
            return jsonify(data)
        else:
            return jsonify({})

#删除车辆信息
class DelBus1Infos(Resource):
    def delete(self,id):
        bus = BusInfo1.query.filter(BusInfo1.id==id).first()
        if bus:
            db.session.delete(bus)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})
