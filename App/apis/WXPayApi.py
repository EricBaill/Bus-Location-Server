# -*- coding: utf-8 -*-
import hashlib
import time

import requests
import xmltodict
from flask_restful import Resource, reqparse
import random

from App.models import Order, BusInfo, db

parser = reqparse.RequestParser()
parser.add_argument(name='auth_code',type=str)

#微信扫码支付
class WXPay(Resource):
    def post(self):
        parse = parser.parse_args()
        auth_code = parse.get('auth_code')

        #参数配置
        appid = 'wx8f8eae4c7f709a50'
        mch_id = '1488536192'
        #作为公交车编号
        body = 'bus05'
        total_fee = '200'
        spbill_create_ip = '192.168.1.100'
        auth_code = auth_code[1:]

        #生成随机字符串
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        strs = []
        for x in range(32):
            strs.append(chars[random.randrange(0, len(chars))])
        nonce_str = "".join(strs)

        t = time.time()
        out_trade_no = str(round(t * 10)) + str(round(t * 10)) + str(round(t))  # 毫秒级时间戳

        #生成签名(注意按照ASCII排序，必填参数一个不能少)
        stringA = "appid={}&auth_code={}&body={}&mch_id={}&nonce_str={}&out_trade_no={}&spbill_create_ip={}&total_fee={}".format(appid,auth_code,body,mch_id,nonce_str,out_trade_no,spbill_create_ip,total_fee);

        stringB = stringA + "&key=UagwknH5Pw7MbFDKvMmi3BVYDEw7vHaK" #注：key为商户平台设置的密钥key
        sign = (hashlib.md5(stringB.encode("utf-8")).hexdigest()).upper()
        out_trade_no = out_trade_no[:11]
        data = {
            "appid":appid,
            "mch_id":mch_id,
            "nonce_str":nonce_str,
            "sign":sign,
            "body":body,
            "out_trade_no":out_trade_no,
            "total_fee":total_fee,
            "spbill_create_ip":spbill_create_ip,
            "auth_code":auth_code,
        }

        #添加订单
        bus = BusInfo.query.filter(BusInfo.name==body).first()
        if bus:
            order = Order()
            order.money = float(total_fee) / 100.00
            order.bus_id = bus.id
            order.order_code = out_trade_no
            db.session.add(order)
            db.session.commit()
        else:
            pass


        # 将json格式转换成xml格式
        xml = []
        for k in sorted(data.keys()):
            v = data.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
        xmlstr = '<xml>{}</xml>'.format(''.join(xml))

        url = 'https://api.mch.weixin.qq.com/pay/micropay'
        r = requests.post(url, data=xmlstr,headers={'Content-Type': 'application/xml'})
        #设置字符集防止出现乱码
        xml_str = r.text.encode('ISO-8859-1').decode('utf-8')

        #将xml格式转换成json格式
        json_str = xmltodict.parse(xml_str)
        return json_str


