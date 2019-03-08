# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse
from math import*
from App.models import BusInfo1, StationTow0, StationTow1, db


#打开App显示车的位置
class Test(Resource):
    def get(self,direction):
        list_s = []
        buses = BusInfo1.query.filter(BusInfo1.direction==direction).all()
        stations = StationTow0.query.all()
        stations1 = StationTow1.query.all()

        if direction == '0':
            list_ = []
            for bus in buses:
                for i in range(len(stations)):
                    lngbus = float(bus.lng)
                    latbus = float(bus.lat)

                    lats = float(stations[i].lat)
                    lngs = float(stations[i].lng)
                    lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                    dlon = lngs1 - lngr
                    dlat = lats1 - latr
                    a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                    distance = 2 * asin(sqrt(a)) * 6371 * 1000
                    list_.append(distance)
                    list_.sort()
                    print(i)

                    if list_[0] == distance:
                        data = {
                            'bus': bus.name,
                            'station': stations[i].name,
                            'distance': distance,
                            'latitude': bus.lat,
                            'longitude': bus.lng,
                            'number': bus.number,
                            'feescale': bus.feescale,
                        }
                        list_s.append(data)

            return jsonify(list_s)

        elif direction == '1':
            list_ = []
            for bus in buses:
                for i in range(len(stations1)):
                    lngbus = float(bus.lng)
                    latbus = float(bus.lat)

                    lats = float(stations1[i].lat)
                    lngs = float(stations1[i].lng)
                    lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                    dlon = lngs1 - lngr
                    dlat = lats1 - latr
                    a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                    distance = 2 * asin(sqrt(a)) * 6371 * 1000
                    list_.append(distance)
                    list_.sort()

                    if list_[0] == distance:
                        data = {
                            'bus': bus.name,
                            'station': stations1[i].name,
                            'distance': distance,
                            'latitude': bus.lat,
                            'longitude': bus.lng,
                            'number': bus.number,
                            'feescale': bus.feescale,
                        }
                        list_s.append(data)

            return jsonify(list_s)


        # if direction == '0':
        #     list_ = []
        #     for bus in buses:
        #         for station in stations:
        #             lngbus = float(bus.lng)
        #             latbus = float(bus.lat)
        #
        #             lats = float(station.lat)
        #             lngs = float(station.lng)
        #             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #             dlon = lngs1 - lngr
        #             dlat = lats1 - latr
        #             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #             distance = 2 * asin(sqrt(a)) * 6371 * 1000
        #             list_.append(distance)
        #             list_.sort()
        #
        #             if list_[0] == distance:
        #                 data = {
        #                     'bus': bus.name,
        #                     'station': station.name,
        #                     'distance': distance,
        #                     'latitude': bus.lat,
        #                     'longitude': bus.lng,
        #                     'number': bus.number,
        #                     'feescale': bus.feescale,
        #                 }
        #                 list_s.append(data)
        #
        #     return jsonify(list_s)
        #
        # elif direction == '1':
        #     list_ = []
        #     for bus in buses:
        #         for station in stations1:
        #
        #             lngbus = float(bus.lng)
        #             latbus = float(bus.lat)
        #
        #             lats = float(station.lat)
        #             lngs = float(station.lng)
        #             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
        #             dlon = lngs1 - lngr
        #             dlat = lats1 - latr
        #             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
        #             distance = 2 * asin(sqrt(a)) * 6371 * 1000
        #             list_.append(distance)
        #             list_.sort()
        #             if list_[0] == distance:
        #                 data = {
        #                     'bus': bus.name,
        #                     'station': station.name,
        #                     'distance': distance,
        #                     'latitude': bus.lat,
        #                     'longitude': bus.lng,
        #                     'number': bus.number,
        #                     'feescale': bus.feescale,
        #                 }
        #                 list_s.append(data)
        #                 if len(list_) == len(stations):
        #                     list_ = []
        #     return jsonify(list_s)