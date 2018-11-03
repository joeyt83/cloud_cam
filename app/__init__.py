import json
from cloud_cam import CloudCamClient
from flask import Flask

app = Flask(__name__)

# Read app config and load into flask's config object.
APP_CONF = json.loads(open('app_config.json').read())
for k, v in APP_CONF.iteritems():
  app.config[k.upper()] = v

client = CloudCamClient(
  app.config["CLOUD_CAM_HOST"],
  app.config["CLOUD_CAM_USER"],
  app.config["CLOUD_CAM_PASS"],
  app.config["MOVE_SPEED"]
)

from app import views
