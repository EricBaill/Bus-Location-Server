# # -*- coding: utf-8 -*-
#
#
# # def trans_dict_to_xml(data):
# data = {
#         "appid":"appid",
#         "mch_id":"appid",
#         "nonce_str":"appid",
#         "sign":"appid",
#         "body":"appid",
#         "out_trade_no":"appid",
#         "total_fee":"appid",
#         "spbill_create_ip":"appid",
#         "auth_code":"appid",
#         }
# xml = []
# for k in sorted(data.keys()):
#     v = data.get(k)
#     if k == 'detail' and not v.startswith('<![CDATA['):
#         v = '<![CDATA[{}]]>'.format(v)
#     xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
# print('<xml>{}</xml>'.format(''.join(xml)))