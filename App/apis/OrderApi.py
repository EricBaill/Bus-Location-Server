# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource
import datetime
from sqlalchemy import extract, and_


from App.models import Order

#(线路1)
#获取某辆车的日订单
class OrderResource(Resource):
    def get(self,id):
        list_ = []
        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')
        days = datetime.datetime.now().strftime('%d')

        orders = Order.query.filter(Order.bus_id.__eq__(id), and_(
            extract('year', Order.create_at) == years,
            extract('month', Order.create_at) == months,
            extract('day', Order.create_at) == days
        )).all()
        if orders:
            for order in orders:
                data = {
                    'id':order.id,
                    'order_code':order.order_code,
                    'money':order.money,
                    'create_at':order.create_at
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

#获取某辆车的月订单
class OrderResource01(Resource):
    def get(self,id):
        list_ = []
        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')

        orders = Order.query.filter( Order.bus_id.__eq__(id), and_(
            extract('year', Order.create_at) == years,
            extract('month', Order.create_at) == months,
        )).all()
        if orders:
            for order in orders:
                data = {
                    'id':order.id,
                    'order_code':order.order_code,
                    'money':order.money,
                    'create_at':order.create_at
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


#(线路2)
#获取某辆车的日订单
class OrderResource02(Resource):
    def get(self,id):
        list_ = []
        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')
        days = datetime.datetime.now().strftime('%d')

        orders = Order.query.filter(Order.bus1_id.__eq__(id), and_(
            extract('year', Order.create_at) == years,
            extract('month', Order.create_at) == months,
            extract('day', Order.create_at) == days
        )).all()
        if orders:
            for order in orders:
                data = {
                    'id':order.id,
                    'order_code':order.order_code,
                    'money':order.money,
                    'create_at':order.create_at
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

#获取某辆车的月订单
class OrderResource03(Resource):
    def get(self,id):
        list_ = []
        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')

        orders = Order.query.filter( Order.bus1_id.__eq__(id), and_(
            extract('year', Order.create_at) == years,
            extract('month', Order.create_at) == months,
        )).all()
        if orders:
            for order in orders:
                data = {
                    'id':order.id,
                    'order_code':order.order_code,
                    'money':order.money,
                    'create_at':order.create_at
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])