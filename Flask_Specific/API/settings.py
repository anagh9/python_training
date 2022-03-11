from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from redis import Redis
import logging

class BaseConfig(object):
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = None
    CACHE_DEFAULT_TIMEOUT = 500


app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
# cache = Cache(app)
cache = Cache(config={"CACHE_TYPE": "RedisCache",
              "host": "127.0.0.1", "CACHE_REDIS_PORT": 6379})
cache.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
