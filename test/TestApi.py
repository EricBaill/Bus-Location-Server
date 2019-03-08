# # -*- coding: utf-8 -*-
# from flask import jsonify
# from flask_restful import Resource
# from math import*
# from App.models import BusInfo, Station0
#
#
# class BusInfoResource(Resource):
#     def get(self,direction):
#
#         buses = BusInfo.query.filter(BusInfo.direction==direction).all()
#         stations = Station0.query.all()
#
#         if direction == '0':
#             lngbus = float(buses[0].lng)
#             latbus = float(buses[0].lat)
#
#             lats = float(stations[0].lat)
#             lngs = float(stations[0].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[1].lat)
#             lngs = float(stations[1].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[2].lat)
#             lngs = float(stations[2].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[3].lat)
#             lngs = float(stations[3].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[4].lat)
#             lngs = float(stations[4].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[5].lat)
#             lngs = float(stations[5].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[6].lat)
#             lngs = float(stations[6].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[7].lat)
#             lngs = float(stations[7].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance08 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[8].lat)
#             lngs = float(stations[8].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance09 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[9].lat)
#             lngs = float(stations[9].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance10 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             list_01 = [distance01, distance02, distance03, distance04, distance05,distance06, distance07, distance08, distance09, distance10]
#             list_01.sort()
#             if list_01[0] == distance01:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '金运路',
#                     'distance': distance01,
#                 }
#             elif list_01[0] == distance02:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '金沙江西路',
#                     'distance': distance02,
#                 }
#             elif list_01[0] == distance03:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '丰庄',
#                     'distance': distance03,
#                 }
#             elif list_01[0] == distance04:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '祁连山南路',
#                     'distance': distance04,
#                 }
#             elif list_01[0] == distance05:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '真北路',
#                     'distance': distance05,
#                 }
#             elif list_01[0] == distance06:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '大渡河路',
#                     'distance': distance05,
#                 }
#             elif list_01[0] == distance07:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '金沙江路',
#                     'distance': distance07,
#                 }
#             elif list_01[0] == distance08:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '隆德路',
#                     'distance': distance08,
#                 }
#             elif list_01[0] == distance09:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '武宁路',
#                     'distance': distance09,
#                 }
#             elif list_01[0] == distance10:
#                 data01 = {
#                     'bus': 'bus01',
#                     'station': '长寿路',
#                     'distance': distance10,
#                 }
#             else:
#                 pass
#
#
#             lngbus = float(buses[1].lng)
#             latbus = float(buses[1].lat)
#
#             lats = float(stations[0].lat)
#             lngs = float(stations[0].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[1].lat)
#             lngs = float(stations[1].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[2].lat)
#             lngs = float(stations[2].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[3].lat)
#             lngs = float(stations[3].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[4].lat)
#             lngs = float(stations[4].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[5].lat)
#             lngs = float(stations[5].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[6].lat)
#             lngs = float(stations[6].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[7].lat)
#             lngs = float(stations[7].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance08 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[8].lat)
#             lngs = float(stations[8].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance09 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[9].lat)
#             lngs = float(stations[9].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance10 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             list_02 = [distance01, distance02, distance03, distance04, distance05, distance06, distance07, distance08,
#                        distance09, distance10]
#             list_02.sort()
#             if list_02[0] == distance01:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '金运路',
#                     'distance': distance01,
#                 }
#             elif list_02[0] == distance02:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '金沙江西路',
#                     'distance': distance02,
#                 }
#             elif list_02[0] == distance03:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '丰庄',
#                     'distance': distance03,
#                 }
#             elif list_02[0] == distance04:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '祁连山南路',
#                     'distance': distance04,
#                 }
#             elif list_02[0] == distance05:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '真北路',
#                     'distance': distance05,
#                 }
#             elif list_02[0] == distance06:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '大渡河路',
#                     'distance': distance05,
#                 }
#             elif list_02[0] == distance07:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '金沙江路',
#                     'distance': distance07,
#                 }
#             elif list_02[0] == distance08:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '隆德路',
#                     'distance': distance08,
#                 }
#             elif list_02[0] == distance09:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '武宁路',
#                     'distance': distance09,
#                 }
#             elif list_02[0] == distance10:
#                 data02 = {
#                     'bus': 'bus02',
#                     'station': '长寿路',
#                     'distance': distance10,
#                 }
#             else:
#                 pass
#
#             lngbus = float(buses[2].lng)
#             latbus = float(buses[2].lat)
#
#             lats = float(stations[0].lat)
#             lngs = float(stations[0].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[1].lat)
#             lngs = float(stations[1].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[2].lat)
#             lngs = float(stations[2].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[3].lat)
#             lngs = float(stations[3].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[4].lat)
#             lngs = float(stations[4].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[5].lat)
#             lngs = float(stations[5].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[6].lat)
#             lngs = float(stations[6].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[7].lat)
#             lngs = float(stations[7].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance08 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[8].lat)
#             lngs = float(stations[8].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance09 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[9].lat)
#             lngs = float(stations[9].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance10 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             list_03 = [distance01, distance02, distance03, distance04, distance05, distance06, distance07, distance08,
#                        distance09, distance10]
#             list_03.sort()
#             if list_03[0] == distance01:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '金运路',
#                     'distance': distance01,
#                 }
#             elif list_03[0] == distance02:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '金沙江西路',
#                     'distance': distance02,
#                 }
#             elif list_03[0] == distance03:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '丰庄',
#                     'distance': distance03,
#                 }
#             elif list_03[0] == distance04:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '祁连山南路',
#                     'distance': distance04,
#                 }
#             elif list_03[0] == distance05:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '真北路',
#                     'distance': distance05,
#                 }
#             elif list_03[0] == distance06:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '大渡河路',
#                     'distance': distance05,
#                 }
#             elif list_03[0] == distance07:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '金沙江路',
#                     'distance': distance07,
#                 }
#             elif list_03[0] == distance08:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '隆德路',
#                     'distance': distance08,
#                 }
#             elif list_03[0] == distance09:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '武宁路',
#                     'distance': distance09,
#                 }
#             elif list_03[0] == distance10:
#                 data03 = {
#                     'bus': 'bus03',
#                     'station': '长寿路',
#                     'distance': distance10,
#                 }
#             else:
#                 pass
#
#             lngbus = float(buses[3].lng)
#             latbus = float(buses[3].lat)
#
#             lats = float(stations[0].lat)
#             lngs = float(stations[0].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[1].lat)
#             lngs = float(stations[1].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[2].lat)
#             lngs = float(stations[2].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[3].lat)
#             lngs = float(stations[3].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[4].lat)
#             lngs = float(stations[4].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[5].lat)
#             lngs = float(stations[5].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[6].lat)
#             lngs = float(stations[6].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[7].lat)
#             lngs = float(stations[7].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance08 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[8].lat)
#             lngs = float(stations[8].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance09 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[9].lat)
#             lngs = float(stations[9].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance10 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             list_04 = [distance01, distance02, distance03, distance04, distance05, distance06, distance07, distance08,
#                        distance09, distance10]
#             list_04.sort()
#             if list_04[0] == distance01:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '金运路',
#                     'distance': distance01,
#                 }
#             elif list_04[0] == distance02:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '金沙江西路',
#                     'distance': distance02,
#                 }
#             elif list_04[0] == distance03:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '丰庄',
#                     'distance': distance03,
#                 }
#             elif list_04[0] == distance04:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '祁连山南路',
#                     'distance': distance04,
#                 }
#             elif list_04[0] == distance05:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '真北路',
#                     'distance': distance05,
#                 }
#             elif list_04[0] == distance06:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '大渡河路',
#                     'distance': distance05,
#                 }
#             elif list_04[0] == distance07:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '金沙江路',
#                     'distance': distance07,
#                 }
#             elif list_04[0] == distance08:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '隆德路',
#                     'distance': distance08,
#                 }
#             elif list_04[0] == distance09:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '武宁路',
#                     'distance': distance09,
#                 }
#             elif list_04[0] == distance10:
#                 data04 = {
#                     'bus': 'bus04',
#                     'station': '长寿路',
#                     'distance': distance10,
#                 }
#             else:
#                 pass
#
#             lngbus = float(buses[4].lng)
#             latbus = float(buses[4].lat)
#
#             lats = float(stations[0].lat)
#             lngs = float(stations[0].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance01 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[1].lat)
#             lngs = float(stations[1].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance02 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[2].lat)
#             lngs = float(stations[2].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance03 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[3].lat)
#             lngs = float(stations[3].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance04 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[4].lat)
#             lngs = float(stations[4].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance05 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[5].lat)
#             lngs = float(stations[5].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance06 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[6].lat)
#             lngs = float(stations[6].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance07 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[7].lat)
#             lngs = float(stations[7].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance08 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[8].lat)
#             lngs = float(stations[8].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance09 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             lats = float(stations[9].lat)
#             lngs = float(stations[9].lng)
#             lngr, latr, lngs1, lats1 = map(radians, [lngs, lats, lngbus, latbus])
#             dlon = lngs1 - lngr
#             dlat = lats1 - latr
#             a = sin(dlat / 2) ** 2 + cos(latr) * cos(lats1) * sin(dlon / 2) ** 2
#             distance10 = 2 * asin(sqrt(a)) * 6371 * 1000
#
#             list_05 = [distance01, distance02, distance03, distance04, distance05, distance06, distance07, distance08,
#                        distance09, distance10]
#             list_05.sort()
#             if list_05[0] == distance01:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '金运路',
#                     'distance': distance01,
#                 }
#             elif list_05[0] == distance02:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '金沙江西路',
#                     'distance': distance02,
#                 }
#             elif list_05[0] == distance03:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '丰庄',
#                     'distance': distance03,
#                 }
#             elif list_05[0] == distance04:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '祁连山南路',
#                     'distance': distance04,
#                 }
#             elif list_05[0] == distance05:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '真北路',
#                     'distance': distance05,
#                 }
#             elif list_05[0] == distance06:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '大渡河路',
#                     'distance': distance05,
#                 }
#             elif list_05[0] == distance07:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '金沙江路',
#                     'distance': distance07,
#                 }
#             elif list_05[0] == distance08:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '隆德路',
#                     'distance': distance08,
#                 }
#             elif list_05[0] == distance09:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '武宁路',
#                     'distance': distance09,
#                 }
#             elif list_05[0] == distance10:
#                 data05 = {
#                     'bus': 'bus05',
#                     'station': '长寿路',
#                     'distance': distance10,
#                 }
#             else:
#                 pass
#
#             return jsonify(data01,data02,data03,data04,data05)
#
#
#
#
#         elif direction == '1':
#             pass
#


# -*- coding: utf-8 -*-