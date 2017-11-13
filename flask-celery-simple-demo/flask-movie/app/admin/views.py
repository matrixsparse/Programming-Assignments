# -*- coding: utf-8 -*-
# 视图文件

from flask import render_template, redirect, url_for, flash, session
from . import admin
from app.admin.forms import LoginForm
from app.models import Admin


# 后台管理index页面
@admin.route("/")
def index():
    return render_template("admin/index.html")


# 后台管理登录页面
@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！")
            return redirect(url_for("admin.login"))
    return render_template('admin/login.html', form=form)


# 后台管理退出登录页面
@admin.route("/logout/")
def logout():
    return redirect(url_for('admin.login'))


# 后台管理退出登录页面
@admin.route("/pwd/")
def pwd():
    return render_template('admin/pwd.html')


# 后台管理编辑标签
@admin.route("/tag/add")
def tag_add():
    return render_template('admin/tag_add.html')


# 后台管理标签列表
@admin.route("/tag/list")
def tag_list():
    return render_template('admin/tag_list.html')


# 后台管理添加电影
@admin.route("/movie/add")
def movie_add():
    return render_template('admin/movie_add.html')


# 后台管理电影列表
@admin.route("/movie/list")
def movie_list():
    return render_template('admin/movie_list.html')


# 后台管理添加预告
@admin.route("/preview/add")
def preview_add():
    return render_template('admin/preview_add.html')


# 后台管理预告列表
@admin.route("/preview/list")
def preview_list():
    return render_template('admin/preview_list.html')


# 后台管理会员列表
@admin.route("/user/list")
def user_list():
    return render_template('admin/user_list.html')


# 后台管理评论列表
@admin.route("/comment/list")
def comment_list():
    return render_template('admin/comment_list.html')


# 后台管理收藏列表
@admin.route("/moviecol/list")
def moviecol_list():
    return render_template('admin/moviecol_list.html')


# 后台管理操作日志列表
@admin.route("/oplog/list")
def oplog_list():
    return render_template('admin/oplog_list.html')


# 后台管理管理员登录日志列表
@admin.route("/adminloginlog/list")
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


# 后台管理会员登录日志列表
@admin.route("/userloginlog/list")
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


# 后台管理添加权限
@admin.route("/auth/add")
def auth_add():
    return render_template('admin/auth_add.html')


# 后台管理权限列表
@admin.route("/role/add")
def role_add():
    return render_template('admin/role_add.html')


# 后台管理角色列表
@admin.route("/role/list")
def role_list():
    return render_template('admin/role_list.html')


# 后台管理权限列表
@admin.route("/auth/list")
def auth_list():
    return render_template('admin/auth_list.html')


# 后台管理添加管理员
@admin.route("/admin/add")
def admin_add():
    return render_template('admin/admin_add.html')


# 后台管理管理员列表
@admin.route("/admin/list")
def admin_list():
    return render_template('admin/admin_list.html')
