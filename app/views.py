from app import app
from app import client

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"

@app.route('/zoom/in')
def zoom_in():
  client.zoom_in()
  return "OK"

@app.route('/zoom/out')
def zoom_out():
  client.zoom_out()
  return "OK"

@app.route('/pan/left')
def pan_left():
  client.pan_left()
  return "OK"

@app.route('/pan/right')
def pan_right():
  client.pan_right()
  return "OK"

@app.route('/tilt/up')
def tilt_up():
  client.tilt_up()
  return "OK"

@app.route('/tilt/down')
def tilt_down():
  client.tilt_down()
  return "OK"

