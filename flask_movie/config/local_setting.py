# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/movie_cat"

SECRET_KEY = "123456key"


DOMAIN = {
    "www":"http://127.0.0.1"
}


#RELEASE_PATH = "/home/www/release_version"