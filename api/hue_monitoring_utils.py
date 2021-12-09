import requests

import os
import sys

from lxml import html
from time import sleep
from utils import log_msg, is_true
from hue_utils import change_color, HUE_USERNAME, HUE_MONITOR_LIGHTS_IDS, HUE_BRI_KO, HUE_BRI_OK, HUE_COLOR_KO, HUE_COLOR_OK

APP_NAME=os.environ['APP_NAME']
APP_USERNAME=os.environ['APP_USERNAME']
APP_PASSWORD=os.environ['APP_PASSWORD']
SLACK_TOKEN=os.environ['SLACK_TOKEN']
SLACK_USERNAME=os.environ['SLACK_USERNAME']
SLACK_CHANNEL=os.environ['SLACK_CHANNEL']
APP_URLS=os.environ['APP_URLS'].split(",")
ENABLE_MONITORING=os.environ['ENABLE_MONITORING']
ERROR_WAIT_TIME=int(os.environ['ERROR_WAIT_TIME'])

def change_colors(bri, color):
    for i in HUE_MONITOR_LIGHTS_IDS:
      change_color(bri, color, i)

def slack_message(emoji, channel, color, message, token, user):
  r = requests.post("https://hooks.slack.com/services/{}".format(token), json = {"channel": channel, "username": user, "icon_emoji": emoji, "attachments": [{"color": color, "text": message}]})
  log_msg("DEBUG", "slack_message", r.content)


def appstatus_status(url, username, password):
   page=requests.get("{}?p=radiator".format(url), auth=(username, password))
   tree = html.fromstring(page.content)
   val=tree.xpath('//a[@href="?p=status" and @class="btn btn-large btn-success"]/text()')
   result = len(val) >= 1
   if not result:
      slack_message(":scream_cat:", SLACK_CHANNEL, "#BB0000", "There is a problem on the application {}, check the following page: {}".format(APP_NAME, url), SLACK_TOKEN, SLACK_USERNAME)
   return result

def check_app():
  if is_true(ENABLE_MONITORING):
    status = True
    while True:
      try:
        for app in APP_URLS:
          log_msg("INFO", "HueMonitoring", "check {}".format(app))
          status = status and appstatus_status("{}/status".format(app), APP_USERNAME, APP_PASSWORD)

        if status:
          change_colors(HUE_BRI_OK, HUE_COLOR_OK)
        else:
          change_colors(HUE_BRI_KO, HUE_COLOR_KO)
      except:
        log_msg("ERROR", "check_app", "Unexpected error on indices loop = {}".format(sys.exc_info()[0]))
        sleep(ERROR_WAIT_TIME)
