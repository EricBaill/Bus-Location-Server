# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Inform, db


#获取信息通知
class Informs(Resource):
    def get(self):
        infos = Inform.query.all()
        if infos:
            if len(infos) >= 3:
                info = infos[-1]
                info1 = infos[-2]
                info2 = infos[-3]
                data = {
                    'id': info.id,
                    'title': info.title,
                    'content': info.content,
                    'cover_img': info.cover_img,
                    'flag': info.flag,
                }
                data1 = {
                    'id': info1.id,
                    'title': info1.title,
                    'content': info1.content,
                    'cover_img': info1.cover_img,
                    'flag': info1.flag,
                }
                data2 = {
                    'id': info2.id,
                    'title': info2.title,
                    'content': info2.content,
                    'cover_img': info2.cover_img,
                    'flag': info2.flag,
                }

                list_ = [data,data1,data2]
                return jsonify(list_)

            elif len(infos) == 2:
                info = infos[-1]
                info1 = infos[-2]
                data = {
                    'id': info.id,
                    'title': info.title,
                    'content': info.content,
                    'cover_img': info.cover_img,
                    'flag': info.flag,
                }
                data1 = {
                    'id': info1.id,
                    'title': info1.title,
                    'content': info1.content,
                    'cover_img': info1.cover_img,
                    'flag': info1.flag,
                }

                list_ = [data, data1]
                return jsonify(list_)
            elif len(infos) == 1:
                info = infos[0]
                data = {
                    'id': info.id,
                    'title': info.title,
                    'content': info.content,
                    'cover_img': info.cover_img,
                    'flag': info.flag,
                }
                return jsonify(data)
            else:
                pass
        else:
            return jsonify([])



class Informs01(Resource):
    def get(self,flag):
        info = Inform.query.filter(Inform.flag==flag).first()
        if info:
            data = {
                'id': info.id,
                'title': info.title,
                'content': info.content,
                'cover_img': info.cover_img,
                'flag': info.flag,
            }
            return jsonify(data)
        else:
            return jsonify({})


class Informs02(Resource):
    def get(self,id):
        info = Inform.query.filter(Inform.id==id).first()
        if info:
            data = {
                'id': info.id,
                'title': info.title,
                'content': info.content,
                'cover_img': info.cover_img,
                'flag': info.flag,
            }
            return jsonify(data)
        else:
            return jsonify({})

parser = reqparse.RequestParser()
parser.add_argument(name='id', type=int)
parser.add_argument(name='title', type=str)
parser.add_argument(name='content', type=str)
parser.add_argument(name='cover_img', type=str)
parser.add_argument(name='flag', type=str)

#添加通知信息
class AddInforms(Resource):
    def post(self):
        parse = parser.parse_args()
        title = parse.get('title')
        content = parse.get('content')
        cover_img = parse.get('cover_img')
        flag = parse.get('flag')
        info = Inform()
        info.title = title
        info.content = content
        info.cover_img = cover_img
        info.flag = flag
        db.session.add(info)
        db.session.commit()
        print(content)
        info1 = Inform.query.filter(Inform.content==content,Inform.flag==flag).first()
        data = {
            'id':info1.id,
            'title': title,
            'content': content,
            'cover_img': cover_img,
            'flag': flag,
            }
        return jsonify(data)

#修改通知信息
class PutInforms(Resource):
    def put(self):
        parse = parser.parse_args()
        id = parse.get('id')
        title = parse.get('title')
        cover_img = parse.get('cover_img')
        info = Inform.query.filter(Inform.id==id).first()
        if info:
            info.title = title
            info.cover_img = cover_img
            db.session.commit()
            data = {
                'id':id,
                'title': title,
                'cover_img': cover_img,
                }
            return jsonify(data)
        else:
            return jsonify({})

#删除通知信息
class DelInforms(Resource):
    def delete(self,id):
        info = Inform.query.filter(Inform.id==id).first()
        if info:
            db.session.delete(info)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})

class ManagerInforms(Resource):
    def get(self):
        list_ = []
        infos = Inform.query.all()
        if infos:
            for info in infos:
                data = {
                    'id': info.id,
                    'title': info.title,
                    'content': info.content,
                    'cover_img': info.cover_img,
                    'flag': info.flag,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])
