# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse
from math import*
from App.models import BusInfo, Station0, Station1, db


#打开App显示车的位置
class BusInfoResource(Resource):
    def get(self,direction):
        list_s = []
        buses = BusInfo.query.filter(BusInfo.direction==direction).all()
        stations = Station0.query.all()
        stations1 = Station1.query.all()

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

                lats = float(stations[5].lat)
                lngs = float(stations[5].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance06 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[6].lat)
                lngs = float(stations[6].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance07 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[7].lat)
                lngs = float(stations[7].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance08 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[8].lat)
                lngs = float(stations[8].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance09 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[9].lat)
                lngs = float(stations[9].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance10 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[10].lat)
                lngs = float(stations[10].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance11 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[11].lat)
                lngs = float(stations[11].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance12 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[12].lat)
                lngs = float(stations[12].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance13 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[13].lat)
                lngs = float(stations[13].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance14 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[14].lat)
                lngs = float(stations[14].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance15 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[15].lat)
                lngs = float(stations[15].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance16 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[16].lat)
                lngs = float(stations[16].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance17 = 2 * asin(sqrt(a)) * 6371 * 1000


                list_ = [distance01, distance02, distance03, distance04, distance05,distance06, distance07, distance08, distance09, distance10,distance11, distance12, distance13, distance14, distance15, distance16, distance17]
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
                elif list_[0] == distance06:
                    data = {
                        'bus': bus.name,
                        'station': stations[5].name,
                        'distance': distance05,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance07:
                    data = {
                        'bus': bus.name,
                        'station': stations[6].name,
                        'distance': distance07,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance08:
                    data = {
                        'bus': bus.name,
                        'station': stations[7].name,
                        'distance': distance08,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance09:
                    data = {
                        'bus': bus.name,
                        'station': stations[8].name,
                        'distance': distance09,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance10:
                    data = {
                        'bus': bus.name,
                        'station': stations[9].name,
                        'distance': distance10,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance11:
                    data = {
                        'bus': bus.name,
                        'station': stations[10].name,
                        'distance': distance11,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance12:
                    data = {
                        'bus': bus.name,
                        'station': stations[11].name,
                        'distance': distance12,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance13:
                    data = {
                        'bus': bus.name,
                        'station': stations[12].name,
                        'distance': distance13,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance14:
                    data = {
                        'bus': bus.name,
                        'station': stations[13].name,
                        'distance': distance14,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance15:
                    data = {
                        'bus': bus.name,
                        'station': stations[14].name,
                        'distance': distance15,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance16:
                    data = {
                        'bus': bus.name,
                        'station': stations[15].name,
                        'distance': distance16,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance17:
                    data = {
                        'bus': bus.name,
                        'station': stations[16].name,
                        'distance': distance17,
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

                lats = float(stations1[5].lat)
                lngs = float(stations1[5].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance06 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[6].lat)
                lngs = float(stations1[6].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance07 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[7].lat)
                lngs = float(stations1[7].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance08 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[8].lat)
                lngs = float(stations1[8].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance09 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations1[9].lat)
                lngs = float(stations1[9].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance10 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[10].lat)
                lngs = float(stations[10].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance11 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[11].lat)
                lngs = float(stations[11].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance12 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[12].lat)
                lngs = float(stations[12].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance13 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[13].lat)
                lngs = float(stations[13].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance14 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[14].lat)
                lngs = float(stations[14].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance15 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[15].lat)
                lngs = float(stations[15].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance16 = 2 * asin(sqrt(a)) * 6371 * 1000

                lats = float(stations[16].lat)
                lngs = float(stations[16].lng)
                lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
                dlon = lngs1 - lngr
                dlat = lats1 - latr
                a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
                distance17 = 2 * asin(sqrt(a)) * 6371 * 1000

                list_ = [distance01, distance02, distance03, distance04, distance05, distance06, distance07, distance08,
                         distance09, distance10, distance11, distance12, distance13, distance14, distance15, distance16,
                         distance17]
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
                elif list_[0] == distance06:
                    data = {
                        'bus': bus.name,
                        'station': stations[5].name,
                        'distance': distance05,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance07:
                    data = {
                        'bus': bus.name,
                        'station': stations[6].name,
                        'distance': distance07,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance08:
                    data = {
                        'bus': bus.name,
                        'station': stations[7].name,
                        'distance': distance08,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance09:
                    data = {
                        'bus': bus.name,
                        'station': stations[8].name,
                        'distance': distance09,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance10:
                    data = {
                        'bus': bus.name,
                        'station': stations[9].name,
                        'distance': distance10,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance11:
                    data = {
                        'bus': bus.name,
                        'station': stations[10].name,
                        'distance': distance11,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance12:
                    data = {
                        'bus': bus.name,
                        'station': stations[11].name,
                        'distance': distance12,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance13:
                    data = {
                        'bus': bus.name,
                        'station': stations[12].name,
                        'distance': distance13,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance14:
                    data = {
                        'bus': bus.name,
                        'station': stations[13].name,
                        'distance': distance14,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance15:
                    data = {
                        'bus': bus.name,
                        'station': stations[14].name,
                        'distance': distance15,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance16:
                    data = {
                        'bus': bus.name,
                        'station': stations[15].name,
                        'distance': distance16,
                        'latitude': bus.lat,
                        'longitude': bus.lng,
                        'number': bus.number,
                        'feescale': bus.feescale,
                    }
                elif list_[0] == distance17:
                    data = {
                        'bus': bus.name,
                        'station': stations[16].name,
                        'distance': distance17,
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
class GetBusInfos(Resource):
    def get(self):
        list_ = []
        buses = BusInfo.query.all()
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
class AddBusInfos(Resource):
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        number = parse.get('number')
        feescale = parse.get('feescale')
        bus = BusInfo()
        bus.name = name
        bus.number = number
        bus.feescale = feescale
        db.session.add(bus)
        db.session.commit()
        buss = BusInfo.query.filter(BusInfo.name==name).first()
        data = {
            'id': buss.id,
            'name': name,
            'number':number,
            'feescale':feescale,
        }
        return jsonify(data)

#修改车里信息
class PutBusInfos(Resource):
    def put(self):
        parse = parser.parse_args()
        id = parse.get('id')
        name = parse.get('name')
        number = parse.get('number')
        feescale = parse.get('feescale')
        bus = BusInfo.query.filter(BusInfo.id==id).first()
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
class DelBusInfos(Resource):
    def delete(self,id):
        bus = BusInfo.query.filter(BusInfo.id==id).first()
        if bus:
            db.session.delete(bus)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})
