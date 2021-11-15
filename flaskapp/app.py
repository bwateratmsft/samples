from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='db', port=6379, socket_timeout=1)

@app.route('/')
def index():
    try:
        hitCount = db.incr('hitCount')
        return f'Hello there! This page has been accessed {hitCount} times.'
    except:
        return 'Hello there! We couldn\'t reach the redis instance so we don\'t know how many times this page has been accessed.'