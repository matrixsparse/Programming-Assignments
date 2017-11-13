# -*- coding: utf-8 -*-

from flask import Flask

main = Flask(__name__)

# @main.route("/")
# def index():
#     return "hello world!"

if __name__ == "__main__":
    main.run()