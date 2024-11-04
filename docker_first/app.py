from flask import Flask ,render_template
from redis import RedisError,Redis
import os
#import socket

app = Flask(__name__)
redis = Redis(host="redis",db=0,socket_connect_timeout=2,socket_timeout=2)

@app.route('/')
def welcome():
    try :
        views = redis.incr('compteur')
    except :
        views = '<i>not connected to redis</i>' 
    
    
        
    return render_template('welcome.html',views=views)


@app.route('/bonjour/<string:name>')
def bonjour(name:str=None,args=""):
    
    #args=os.getcwd()
    return render_template('bonjour.html',name=name,args=os.getenv("NOM","UnknownUser"))

@app.route("/bonjour")
def bonjourNone():
    name = "unknown_user"
    return render_template('bonjour.html',name=name)

# interaction db user, template, api rest, security  ...
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1024)