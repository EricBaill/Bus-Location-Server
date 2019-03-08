# -*- coding: utf-8 -*-

from flask import Flask
from App import settings
from App.apis import init_apis
from App.ext import init_ext
from flask_cors import CORS


def create_app(ENV_NAME):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config.from_object(settings.env.get(ENV_NAME))
    #当浏览器显示中文乱码的时候  那么需要加这个忽略编码格式
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.config['JSON_AS_ASCII'] = False
    init_ext(app)
    init_apis(app)

    return app