# -*- coding: utf-8 -*-

from flask_restful import Api

from App.apis.Bus1InfoApi import Bus1InfoResource, GetBus1Infos, AddBus1Infos, PutBus1Infos, DelBus1Infos
from App.apis.Bus1LocationApi import Bus1Location
from App.apis.BusInfoApi import BusInfoResource, GetBusInfos, AddBusInfos, PutBusInfos, DelBusInfos
from App.apis.BusLocationApi import BusLocation
from App.apis.GetInformApi import Informs, Informs01, Informs02, AddInforms, PutInforms, DelInforms, ManagerInforms
from App.apis.GetStationsApi import GetStations, GetStations01, PutStations, DelStations, addStations
from App.apis.OrderApi import OrderResource, OrderResource01, OrderResource02, OrderResource03
from App.apis.RecentStation1Api import RecentStation1
from App.apis.RecentStationApi import RecentStation
from App.apis.StationsTowApi import StationsTow, StationsTow01, PutStationTow, addStationTow, DelStationTow
from App.apis.TestApi import Test
from App.apis.WXPayApi import WXPay

api = Api()
#需要注意  api的初始化 要和init方法联系 否则无法初始化
def init_apis(app):
    api.init_app(app=app)


#离用户最近的站点
api.add_resource(RecentStation,'/api/recentstation/')
api.add_resource(RecentStation1,'/api/recentstation1/')

#获取车辆位置信息
api.add_resource(BusInfoResource,'/api/businfo/<direction>/')
api.add_resource(Bus1InfoResource,'/api/bus1info/<direction>/')

#获取所有车辆信息
api.add_resource(GetBusInfos,'/api/getbusinfos/')
api.add_resource(GetBus1Infos,'/api/getbus1infos/')

#添加车辆信息
api.add_resource(AddBusInfos,'/api/addbusinfos/')
api.add_resource(AddBus1Infos,'/api/addbus1infos/')

#修改车辆信息
api.add_resource(PutBusInfos,'/api/putbusinfos/')
api.add_resource(PutBus1Infos,'/api/putbus1infos/')

#删除车辆信息
api.add_resource(DelBusInfos,'/api/delbusinfos/<id>/')
api.add_resource(DelBus1Infos,'/api/delbus1infos/<id>/')


#(线路一)
#获取正向站点位置信息
api.add_resource(GetStations,'/api/getstations/')
#获取反向站点位置信息
api.add_resource(GetStations01,'/api/getstations/back/')
#编辑站点信息
api.add_resource(PutStations,'/api/putstations/')
#添加站点信息
api.add_resource(addStations,'/api/addstations/')
#删除站点信息
api.add_resource(DelStations,'/api/delstations/direction/<direction>/id/<id>/')


#(线路二)
#获取正向站点位置信息
api.add_resource(StationsTow,'/api/getstations/tow/')
#获取反向站点位置信息
api.add_resource(StationsTow01,'/api/getstations/back/tow/')
#编辑站点信息
api.add_resource(PutStationTow,'/api/putstations/tow/')
#添加站点信息
api.add_resource(addStationTow,'/api/addstations/tow/')
#删除站点信息
api.add_resource(DelStationTow,'/api/delstations/direction/<direction>/id/<id>/tow/')

#公交车离站台距离和时间
api.add_resource(BusLocation,'/api/buslocation/')
api.add_resource(Bus1Location,'/api/bus1location/')

#微信扫码支付
api.add_resource(WXPay,'/api/wxpay/')

#获取通知信息
api.add_resource(Informs,'/api/getinfos/')
api.add_resource(Informs01,'/api/getinfos/flag/<flag>/')
api.add_resource(Informs02,'/api/getinfos/id/<id>/')
api.add_resource(ManagerInforms,'/api/get/all/infos/')

#添加通知信息
api.add_resource(AddInforms,'/api/addinfos/')
#修改通知信息
api.add_resource(PutInforms,'/api/putinfos/')
#删除通知信息
api.add_resource(DelInforms,'/api/delinfos/<id>/')

#获取某辆车的日订单
api.add_resource(OrderResource,'/api/order/day/<id>/')
#获取某辆车的月订单
api.add_resource(OrderResource01,'/api/order/month/<id>/')

#获取某辆车的日订单
api.add_resource(OrderResource02,'/api/order/day/tow/<id>/')
#获取某辆车的月订单
api.add_resource(OrderResource03,'/api/order/month/tow/<id>/')


api.add_resource(Test,'/api/test/<direction>/')




