# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Station0, Station1, db

parser = reqparse.RequestParser()
parser.add_argument(name='id', type=int)
parser.add_argument(name='name', type=str)
parser.add_argument(name='latitude', type=float)
parser.add_argument(name='longitude', type=float)
parser.add_argument(name='direction', type=int)


#获取正向站点位置信息
class GetStations(Resource):
    def get(self):
        list_ = []
        stations = Station0.query.all()
        if stations:
            for station in stations:
                data = {
                        'id': station.id,
                        'name': station.name,
                        'latitude': station.lat,
                        'longitude': station.lng,
                        'direction': station.direction,
                    }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


#获取反向站点位置信息
class GetStations01(Resource):
    def get(self):
        list_ = []
        stations = Station1.query.all()
        if stations:
            for station in stations:
                data = {
                        'id': station.id,
                        'name': station.name,
                        'latitude': station.lat,
                        'longitude': station.lng,
                        'direction': station.direction,
                    }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

#编辑站点信息
class PutStations(Resource):
    def put(self):

        parse = parser.parse_args()
        id = parse.get('id')
        name = parse.get('name')
        latitude = parse.get('latitude')
        longitude = parse.get('longitude')
        direction = parse.get('direction')

        if direction == 0:
            station = Station0.query.filter(Station0.id==id,Station0.direction==direction).first()
            if station:
                station.name = name
                station.lat = latitude
                station.lng = longitude
                db.session.commit()
                data = {
                    'id':id,
                    'name':name,
                    'latitude': latitude,
                    'longitude': longitude,
                    'direction': direction,
                }
                return jsonify(data)
            else:
                return jsonify({})
        elif direction == 1:
            station = Station1.query.filter(Station1.id == id,Station1.direction==direction).first()
            if station:
                station.name = name
                station.lat = latitude
                station.lng = longitude
                db.session.commit()
                data = {
                    'id': id,
                    'name': name,
                    'latitude': latitude,
                    'longitude': longitude,
                    'direction': direction,
                }
                return jsonify(data)
            else:
                return jsonify({})
        else:
            return jsonify({})

#添加站点信息
class addStations(Resource):
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        latitude = parse.get('latitude')
        longitude = parse.get('longitude')
        direction = parse.get('direction')

        if direction == 0:
            station = Station0()
            station.name = name
            station.lat = latitude
            station.lng = longitude
            station.direction = direction
            db.session.add(station)
            db.session.commit()
            stat = Station0.query.filter(Station0.name==name,Station0.direction==direction).first()
            data = {
                'id':stat.id,
                'name':name,
                'latitude': latitude,
                'longitude': longitude,
                'direction': direction,
            }
            return jsonify(data)

        elif direction == 1:
            station = Station1()
            station.name = name
            station.lat = latitude
            station.lng = longitude
            station.direction = direction
            db.session.add(station)
            db.session.commit()
            stat = Station1.query.filter(Station1.name == name,Station1.direction==direction).first()
            data = {
                'id': stat.id,
                'name': name,
                'latitude': latitude,
                'longitude': longitude,
                'direction': direction,
            }
            return jsonify(data)
        else:
            return jsonify({})

#删除站点信息
class DelStations(Resource):
    def delete(self,direction,id):
        if direction == '0':
            station = Station0.query.filter(Station0.id==id).first()
            if station:
                db.session.delete(station)
                db.session.commit()
                return jsonify({'msg':'删除成功！'})
            else:
                return jsonify({})
        elif direction == '1':
            station = Station1.query.filter(Station1.id == id).first()
            if station:
                db.session.delete(station)
                db.session.commit()
                return jsonify({'msg': '删除成功！'})
            else:
                return jsonify({})
        else:
            return jsonify({})


