# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse
from math import*

from App.models import BusInfo1

parser = reqparse.RequestParser()
parser.add_argument(name='station',type=str)
parser.add_argument(name='lat',type=float)
parser.add_argument(name='lng',type=float)
parser.add_argument(name='direction',type=int)
parser.add_argument(name='busname',type=str)

#计算车辆进站时间和距离
class Bus1Location(Resource):
    def post(self):
        parse = parser.parse_args()
        station = parse.get('station')
        lats = parse.get('lat')
        lngs = parse.get('lng')
        direction = parse.get('direction')
        busname = parse.get('busname')

        print(busname)

        if direction == 0:
            bus = BusInfo1.query.filter(BusInfo1.name==busname,BusInfo1.direction==direction).first()
            if bus:
                lngbus = float(bus.lng)
                latbus = float(bus.lat)

                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance = 2 * asin(sqrt(a)) * 6371 * 1000

                speed = int(bus.speed)
                time_ = distance / speed
                data = {
                    'bus': bus.name,
                    'distance': distance,
                    'time_': time_,
                    'station': station
                }
                return jsonify(data)
            else:
                return jsonify({})

        elif direction == 1:
            bus = BusInfo1.query.filter(BusInfo1.name==busname,BusInfo1.direction==direction).first()
            print(bus)
            if bus:
                lngbus = float(bus.lng)
                latbus = float(bus.lat)

                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance = 2 * asin(sqrt(a)) * 6371 * 1000

                speed = int(bus.speed)
                time_ = distance / speed
                data = {
                    'bus': bus.name,
                    'distance': distance,
                    'time_': time_,
                    'station': station
                }
                return jsonify(data)
            else:
                return jsonify({})
        else:
            return jsonify({})



        # if direction == 0:
        #     bus01 = BusInfo.query.filter(BusInfo.name=='bus01',BusInfo.direction==direction).first()
        #     if bus01:
        #         lngbus = float(bus01.lng)
        #         latbus = float(bus01.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance01 = 1000000000000000000000000000000000000000000
        #
        #     bus02 = BusInfo.query.filter(BusInfo.name == 'bus02', BusInfo.direction == direction).first()
        #     if bus02:
        #         lngbus = float(bus02.lng)
        #         latbus = float(bus02.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance02 = 1000000000000000000000000000000000000000000
        #
        #
        #     bus03 = BusInfo.query.filter(BusInfo.name == 'bus03', BusInfo.direction == direction).first()
        #     if bus03:
        #         lngbus = float(bus03.lng)
        #         latbus = float(bus03.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance03 = 1000000000000000000000000000000000000000000
        #
        #
        #     bus04 = BusInfo.query.filter(BusInfo.name == 'bus04', BusInfo.direction == direction).first()
        #     if bus04:
        #         lngbus = float(bus04.lng)
        #         latbus = float(bus04.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance04 = 1000000000000000000000000000000000000000000
        #
        #
        #     bus05 = BusInfo.query.filter(BusInfo.name == 'bus05', BusInfo.direction == direction).first()
        #     if bus05:
        #         lngbus = float(bus05.lng)
        #         latbus = float(bus05.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance05 = 1000000000000000000000000000000000000000000
        #
        #     bus06 = BusInfo.query.filter(BusInfo.name == 'bus06', BusInfo.direction == direction).first()
        #     if bus06:
        #         lngbus = float(bus06.lng)
        #         latbus = float(bus06.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance06 = 1000000000000000000000000000000000000000000
        #
        #     bus07 = BusInfo.query.filter(BusInfo.name == 'bus07', BusInfo.direction == direction).first()
        #     if bus07:
        #         lngbus = float(bus07.lng)
        #         latbus = float(bus07.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance07 = 1000000000000000000000000000000000000000000
        #
        #     list_ = [distance01, distance02, distance03, distance04, distance05,distance06,distance07]
        #     list_.sort()
        #     if list_[0] == distance01:
        #         speed = int(bus01.speed)
        #         time_ = distance01 / speed
        #         data = {
        #             'bus':'bus01',
        #             'distance': distance01,
        #             'time_':time_,
        #             'station':station
        #         }
        #     elif list_[0] == distance02:
        #         speed = int(bus02.speed)
        #         time_ = distance02 / speed
        #         data = {
        #             'bus': 'bus02',
        #             'distance': distance02,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance03:
        #         speed = int(bus03.speed)
        #         time_ = distance03 / speed
        #         data = {
        #             'bus': 'bus03',
        #             'distance': distance03,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance04:
        #         speed = int(bus04.speed)
        #         time_ = distance04 / speed
        #         data = {
        #             'bus': 'bus04',
        #             'distance': distance04,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance05:
        #         speed = int(bus05.speed)
        #         time_ = distance05 / speed
        #         data = {
        #             'bus': 'bus05',
        #             'distance': distance05,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance06:
        #         speed = int(bus06.speed)
        #         time_ = distance06 / speed
        #         data = {
        #             'bus': 'bus06',
        #             'distance': distance06,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance07:
        #         speed = int(bus07.speed)
        #         time_ = distance07 / speed
        #         data = {
        #             'bus': 'bus07',
        #             'distance': distance07,
        #             'time_': time_,
        #             'station': station
        #         }
        #     else:
        #         pass
        #     return jsonify(data)
        #
        # elif direction == 1:
        #     bus01 = BusInfo.query.filter(BusInfo.name == 'bus01', BusInfo.direction == direction).first()
        #     if bus01:
        #         lngbus = float(bus01.lng)
        #         latbus = float(bus01.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance01 = 1000000000000000000000000000000000000000000
        #
        #     bus02 = BusInfo.query.filter(BusInfo.name == 'bus02', BusInfo.direction == direction).first()
        #     if bus02:
        #         lngbus = float(bus02.lng)
        #         latbus = float(bus02.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance02 = 1000000000000000000000000000000000000000000
        #
        #     bus03 = BusInfo.query.filter(BusInfo.name == 'bus03', BusInfo.direction == direction).first()
        #     if bus03:
        #         lngbus = float(bus03.lng)
        #         latbus = float(bus03.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance03 = 1000000000000000000000000000000000000000000
        #
        #     bus04 = BusInfo.query.filter(BusInfo.name == 'bus04', BusInfo.direction == direction).first()
        #     if bus04:
        #         lngbus = float(bus04.lng)
        #         latbus = float(bus04.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance04 = 1000000000000000000000000000000000000000000
        #
        #     bus05 = BusInfo.query.filter(BusInfo.name == 'bus05', BusInfo.direction == direction).first()
        #     if bus05:
        #         lngbus = float(bus05.lng)
        #         latbus = float(bus05.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance05 = 1000000000000000000000000000000000000000000
        #
        #     bus06 = BusInfo.query.filter(BusInfo.name == 'bus06', BusInfo.direction == direction).first()
        #     if bus06:
        #         lngbus = float(bus06.lng)
        #         latbus = float(bus06.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance06 = 1000000000000000000000000000000000000000000
        #
        #     bus07 = BusInfo.query.filter(BusInfo.name == 'bus07', BusInfo.direction == direction).first()
        #     if bus07:
        #         lngbus = float(bus07.lng)
        #         latbus = float(bus07.lat)
        #
        #         lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #         dlon = lngs1 - lngr
        #         dlat = lats1 - latr
        #         a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #         distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
        #     else:
        #         distance07 = 1000000000000000000000000000000000000000000
        #
        #     list_ = [distance01, distance02, distance03, distance04, distance05, distance06, distance07]
        #     list_.sort()
        #
        #     if list_[0] == distance01:
        #         speed = int(bus01.speed)
        #         time_ = distance01 / speed
        #         data = {
        #             'bus': 'bus01',
        #             'distance': distance01,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance02:
        #         speed = int(bus02.speed)
        #         time_ = distance02 / speed
        #         data = {
        #             'bus': 'bus02',
        #             'distance': distance02,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance03:
        #         speed = int(bus03.speed)
        #         time_ = distance03 / speed
        #         data = {
        #             'bus': 'bus03',
        #             'distance': distance03,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance04:
        #         speed = int(bus04.speed)
        #         time_ = distance04 / speed
        #         data = {
        #             'bus': 'bus04',
        #             'distance': distance04,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance05:
        #         speed = int(bus05.speed)
        #         time_ = distance05 / speed
        #         data = {
        #             'bus': 'bus05',
        #             'distance': distance05,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance06:
        #         speed = int(bus06.speed)
        #         time_ = distance06 / speed
        #         data = {
        #             'bus': 'bus06',
        #             'distance': distance06,
        #             'time_': time_,
        #             'station': station
        #         }
        #     elif list_[0] == distance07:
        #         speed = int(bus07.speed)
        #         time_ = distance07 / speed
        #         data = {
        #             'bus': 'bus07',
        #             'distance': distance07,
        #             'time_': time_,
        #             'station': station
        #         }
        #     else:
        #         pass
        #     return jsonify(data)
