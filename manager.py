# -*- coding: utf-8 -*-
from flask import request
from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app

app = create_app('develop')

manager = Manager(app=app)
manager.add_command('db',MigrateCommand)


from qiniu import Auth, put_data
# 用户上传到服务器，服务器再上传到七牛云
@app.route("/upload", methods=["GET", "POST"])
def upload_qiniu():
    fp = request.files.get("file")
    file_name = fp.filename
    # 需要填写你的 Access Key 和 Secret Key
    ak = "6ogDlozD1mvq7OGfBD76ThIYF5BLGT3N_rmIxb9J"
    sk = "cBmGwtmtHyEiiDH2HWuOPowpwcfbV8mUS5n23mLx"
    # 构建鉴权对象
    q = Auth(ak, sk)
    # 要上传的空间
    bucket_name = 'uploadfile'
    # 上传到七牛后保存的文件名
    key = 's' + '/' + 'files' + '/' +file_name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_data(token, key, data=fp.read())
    # 如果上传成功
    if info.status_code == 200:
        # 数据库保存该地址
        img_url = "http://jxtidea.com/" + ret.get("key") #七牛云域名
        print(img_url)
    return '/'+key


if __name__ == '__main__':

    # manager.run()
    app.run(host='0.0.0.0',port='5000')