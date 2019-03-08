# Bus-Location 接口文档

# Client Apis

## 站点信息

+ 获取站点信息

  | Method | Url               |
  | ------ | ----------------- |
  | GET    | /api/getlocation/ |

  返回说明

  ~~~~
  // 200
  
  [{
          'id': ,			//站点ID
          'name': ,		//站点名称
          'latitude': ,	//站点纬度
          'longitude': ,	//站点经度
          'direction':,	//站点方向
   }]
  ~~~~

  

## 车辆信息

+ 获取公交车的位置信息

  | Method | Url                       |
  | ------ | ------------------------- |
  | GET    | /api/businfo/<direction>/ |

  返回说明

  ~~~
  // 200
  
  {
      'bus': ,		//车辆名称
      'station': ,	//该车辆下一站点名称
      'distance':,	//该车辆到下一站点的距离
      'latitude':,	//车辆维度
      'longitude':,	//车辆经度
      'number':,		//车辆编号
      'feescale':,    //收费标准
  }
  ~~~



## 消息通知

+ 获取消息通知

  | Method | Url            |
  | ------ | -------------- |
  | GET    | /api/getinfos/ |

  返回说明

  ~~~~
  // 200
  
  [{
      'id':,			//消息ID
      'title':,		//消息标题
      'content':,	 	//消息内容
      'cover_img':,	//封面图
      'flag':info.,	//类型
  }]
  ~~~~



## 最近站点信息

+ 获取用户最近站点信息

  | Method | Url                 |
  | ------ | ------------------- |
  | POST   | /api/recentstation/ |

  返回说明

  ~~~
  // 200
  
  [{
      'station0': ,	//正向线路站点名称
      'direction0':,	//正向线路站点距离
      'station1':, 	//反向线路站点名称
      'direction1': ,	//反向线路站点距离
  }]
  ~~~



## 车辆进站距离和时间

+ 计算公交车离站台距离和时间

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/buslocation/ |

  返回说明

  ~~~
  // 200
  
  {
      'bus':,		//车辆名称
      'distance':,//车辆离下一站点距离
      'time_':,	//进站时间
      'station':	//下一站点名称
  }
  ~~~

  




# Management Apis

## 站点信息

+ 添加站点信息

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/addstations/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//站点ID
      'name':,		//站点名称
      'latitude': ,	//站点纬度
      'longitude': ,	//站点经度
      'direction': ,	//站点方向
  }
  ~~~



+ 编辑站点信息

  | Method | Url               |
  | ------ | ----------------- |
  | PUT    | /api/putstations/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//站点ID
      'name':,		//站点名称
      'latitude': ,	//站点纬度
      'longitude': ,	//站点经度
      'direction': ,	//站点方向
  }
  ~~~

  

+ 删除站点信息

  | Method | Url                                             |
  | ------ | ----------------------------------------------- |
  | DELETE | /api/delstations/direction/<direction>/id/<id>/ |

  返回说明

  ~~~
  // 200
  
  {
    'msg':'删除成功！'
  }
  ~~~



## 车辆信息

+ 获取车辆信息

  | Method | Url               |
  | ------ | ----------------- |
  | GET    | /api/getbusinfos/ |

  返回说明

  ~~~
  //  200
  
  [{
      'id':,			//车辆ID
      'name':,		//车辆名称
      'latitude':,	//车辆纬度
      'longitude':,	//车辆经度
      'direction':,	//车辆方向
      'number':,		//车辆编号
      'feescale':,    //收费标准
  }]
  ~~~



+ 添加车辆信息

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/addbusinfos/ |

  返回说明

  ~~~
  // 200
  
  {
      'id': ,		  //车辆ID
      'name': ,	  //车辆名称
      'number':,	  //车辆编号
      'feescale':,  //收费标准
  }
  ~~~



+ 编辑车辆信息

  | Method | Url               |
  | ------ | ----------------- |
  | PUT    | /api/putbusinfos/ |

  返回说明

  ~~~
  // 200
  
  {
      'id': ,		  //车辆ID
      'name': ,	  //车辆名称
      'number':,	  //车辆编号
      'feescale':,  //收费标准
  }
  ~~~

  

+ 删除车辆信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | DELETE | /api/delbusinfos/<id>/ |

  返回说明

  ~~~
  // 200
  
  {
    'msg':'删除成功！'
  }
  ~~~



## 信息通知

+ 添加信息通知

  | Method | Url            |
  | ------ | -------------- |
  | POST   | /api/addinfos/ |

  返回说明

  ~~~
  // 200
  {
      'id':,			//消息ID
      'title':,		//消息标题
      'content':,	 	//消息内容
      'cover_img':,	//封面图
      'flag':info.,	//类型
  }
  ~~~



+ 编辑信息通知

  | Method | Url            |
  | ------ | -------------- |
  | PUT    | /api/putinfos/ |

  返回说明

  ~~~
  // 200
  {
      'id':,			//消息ID
      'title':,		//消息标题
      'cover_img':,	//封面图
  }
  ~~~

  

+ 删除信息通知

  | Method | Url                 |
  | ------ | ------------------- |
  | DELETE | /api/delinfos/<id>/ |

  返回说明

  ~~~
  // 200
  
  {
    'msg':'删除成功！'
  }
  ~~~



## 订单信息

+ 获取车辆日订单信息

  | Method | Url                  |
  | ------ | -------------------- |
  | GET    | /api/order/day/<id>/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//订单ID
      'order_code':,	//订单号
      'money':,		//金额
      'create_at':	//订单创建时间
  }
  ~~~



+ 获取车辆日订单信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | GET    | /api/order/month/<id>/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//订单ID
      'order_code':,	//订单号
      'money':,		//金额
      'create_at':	//订单创建时间
  }
  ~~~

  