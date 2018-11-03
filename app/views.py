from app import app
from app import client

@app.route('/')
@app.route('/index')
def index():
  return """
<html>
<body>
<script type="text/javascript">
document.addEventListener('DOMContentLoaded', function() {
  function ptz(action) {
    var oReq = new XMLHttpRequest();
    oReq.open("GET", action);
    oReq.send()
  }
  document.getElementById("pan_left").addEventListener("click", function() {
    ptz("/pan/left")
  });
  document.getElementById("pan_right").addEventListener("click", function() {
    ptz("/pan/right")
  });
  document.getElementById("tilt_up").addEventListener("click", function() {
    ptz("/tilt/up")
  });
  document.getElementById("tilt_down").addEventListener("click", function() {
    ptz("/tilt/down")
  });
  document.getElementById("zoom_in").addEventListener("click", function() {
    ptz("/zoom/in")
  });
  document.getElementById("zoom_out").addEventListener("click", function() {
    ptz("/zoom/out")
  });
  document.getElementById("freeze").addEventListener("click", function() {
    ptz("freeze")
  });
}, false);
</script>
<button type="button" id="freeze">freeze</button>
<br/>
<br/>
<button type="button" id="pan_left">LEFT</button>
<br/>
<br/>
<button type="button" id="pan_right">RIGHT</button>
<br/>
<br/>
<button type="button" id="tilt_up">UP</button>
<br/>
<br/>
<button type="button" id="tilt_down">DOWN</button>
<br/>
<br/>
<button type="button" id="zoom_in">IN</button>
<br/>
<br/>
<button type="button" id="zoom_out">OUT</button>
</body>
</html>

"""

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

@app.route('/freeze')
def freeze():
  client.freeze()
  return "OK"

