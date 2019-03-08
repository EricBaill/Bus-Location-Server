# -*- coding: utf-8 -*-

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#公交车站点信息表
class Station0(db.Model):
    __tablename__ = 'station0'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.String(255), nullable=False)
    direction = db.Column(db.Integer,default=0,nullable=False)

class Station1(db.Model):
    __tablename__ = 'station1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.String(255), nullable=False)
    direction = db.Column(db.Integer,default=1,nullable=False)

class StationTow0(db.Model):
    __tablename__ = 'stationtow0'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.String(255), nullable=False)
    direction = db.Column(db.Integer,default=1,nullable=False)

class StationTow1(db.Model):
    __tablename__ = 'stationtow1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.String(255), nullable=False)
    direction = db.Column(db.Integer,default=1,nullable=False)

#公交车信息表
class BusInfo(db.Model):
    __tablename__ = 'bus_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255))
    lat = db.Column(db.String(255))
    speed = db.Column(db.String(255))
    money = db.Column(db.Float,default=0.0,nullable=False)
    feescale = db.Column(db.Float,default=0.0,nullable=False)
    number = db.Column(db.String(255),nullable=False)
    direction = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

class BusInfo1(db.Model):
    __tablename__ = 'bus_info1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lng = db.Column(db.String(255))
    lat = db.Column(db.String(255))
    speed = db.Column(db.String(255))
    money = db.Column(db.Float,default=0.0,nullable=False)
    feescale = db.Column(db.Float,default=0.0,nullable=False)
    number = db.Column(db.String(255),nullable=False)
    direction = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

#信息通知表
class Inform(db.Model):
    __tablename__ = 'inform'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    cover_img = db.Column(db.String(255))
    flag = db.Column(db.String(68))
    content = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

#订单表
class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    order_code= db.Column(db.String(255), nullable=False)
    money = db.Column(db.Float,default=0.0,nullable=False)
    bus_id = db.Column(db.ForeignKey('bus_info.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    bus1_id = db.Column(db.ForeignKey('bus_info1.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    bus = db.relationship('BusInfo', primaryjoin='Order.bus_id == BusInfo.id', backref='order')
    bus1 = db.relationship('BusInfo1', primaryjoin='Order.bus1_id == BusInfo1.id', backref='order')

