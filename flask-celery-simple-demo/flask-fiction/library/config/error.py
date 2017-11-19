#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

class Err(object):
    Invalid_request = 400
    Unauthorized = 401
    Forbidden = 403
    Not_found = 404
    Not_acceptable = 406
    Gone = 410
    Unprocesable_entity = 422
    Internal_server_error = 500
    Unknown_error = 510
    User_unreachable = 520
    Invalid_params = 420
    Invalid_token = 440
    Not_cli = 450
    Password_error = 460
    Unregistered_account = 470
    Model_error = 480
    Result_is_empty = 490

    class Msg(object):
        Invalid_request = 'Invalid Request'  # [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
        Unauthorized = 'Unauthorized'  # 表示用户没有权限（令牌、用户名、密码错误）。
        Forbidden = 'Forbidden'  # 表示用户得到授权（与401错误相对），但是访问是被禁止的。
        Not_found = 'Not Found'  # 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
        Not_acceptable = 'Not Acceptable'  # 用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
        Gone = 'Gone'  # [GET]：用户请求的资源被永久删除，且不会再得到的。
        Unprocesable_entity = 'Unprocesable Entity'  # [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
        Internal_server_error = 'Internal Server Error'  # 服务器发生错误，用户将无法判断发出的请求是否成功。
        Unknown_error = 'Unknown Error'  # 未知错误
        Invalid_params = 'Invalid Params'  # 无效参数
        Invalid_token = 'Invalid Token'  # 请求鉴权token未通过
        Not_cli = 'Not Cli'  # 不是cli请求
        Password_error = 'Password Error'  # 密码错误
        Unregistered_account = 'Unregistered Account'  # 账号未注册
        Model_error = 'Model Error'  # Model层出现错误
        Result_is_empty = 'Result is empty'  # 结果为空
        User_unreachable = 'User is unreachable'  # 用户不可达
