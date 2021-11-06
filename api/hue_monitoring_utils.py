import requests
import json

import os

from lxml import html
from utils import log_msg, is_true

APP_NAME=os.environ['APP_NAME']
APP_USERNAME=os.environ['APP_USERNAME']
APP_PASSWORD=os.environ['APP_PASSWORD']
HUE_USERNAME=os.environ['HUE_USERNAME']
HUE_LIGHTS_COUNT = int(os.environ['HUE_LIGHTS_COUNT'])
SLACK_TOKEN=os.environ['SLACK_TOKEN']
SLACK_USERNAME=os.environ['SLACK_USERNAME']
APP_UI_URL=os.environ['APP_UI_URL']
APP_WS_URL=os.environ['APP_WS_URL']
ENABLE_MONITORING=os.environ['ENABLE_MONITORING']

HUE_COLOR_KO=2000
HUE_COLOR_OK=30000

HUE_BRI_OK=20
HUE_BRI_KO=254

def get_bridge_ip():
    page=requests.get("https://discovery.meethue.com/")
    payload = json.loads(page.content)
    if len(payload) >= 1:
      return payload[0]['internalipaddress']
    else:
      return ""

def change_color(bri, color):
    for i in range(1, HUE_LIGHTS_COUNT):
      r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, i), json = {"on": True, "sat": 254, "bri": bri, "hue": color})
      log_msg("DEBUG", "slack_message", r.content)

def slack_message(emoji, channel, color, message, token, user):
  r = requests.post("https://hooks.slack.com/services/{}".format(token), json = {"channel": channel, "username": user, "icon_emoji": emoji, "attachments": [{"color": color, "text": message}]})
  log_msg("DEBUG", "slack_message", r.content)


def appstatus_status(url, username, password):
   page=requests.get("{}?p=radiator".format(url), auth=(username, password))
   tree = html.fromstring(page.content)
   val=tree.xpath('//a[@href="?p=status" and @class="btn btn-large btn-success"]/text()')
   result = len(val) >= 1
   if not result:
      slack_message(":scream_cat:", "prod", "#BB0000", "There is a problem on the application {}, check the following page: {}".format(APP_NAME, url), SLACK_TOKEN, SLACK_USERNAME)
   return result

def check_app():
  if is_true(ENABLE_MONITORING):
    while True:
      log_msg("INFO", "HueMonitoring", "check {}".format(APP_UI_URL))
      status = appstatus_status("{}/status".format(APP_UI_URL), APP_USERNAME, APP_PASSWORD)
      status = status and appstatus_status("{}/status".format(APP_WS_URL), APP_USERNAME, APP_PASSWORD)

      if status:
        change_color(HUE_BRI_OK, HUE_COLOR_OK)
      else:
        change_color(HUE_BRI_KO, HUE_COLOR_KO)
