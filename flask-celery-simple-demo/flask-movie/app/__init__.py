# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import pymysql

main = Flask(__name__)

main.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:8889/movie"
main.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
main.config["SECRET_KEY"] = '6b1193db99e042508923b35a0358460f'
main.debug = True
db = SQLAlchemy(main)

# 导入蓝图对象
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
main.register_blueprint(home_blueprint)
main.register_blueprint(admin_blueprint, url_prefix="/admin")


# 404页面
@main.errorhandler(404)
def age_not_found(error):
    return render_template("home/404.html"), 404
