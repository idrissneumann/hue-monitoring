import requests
import json

import os

from lxml import html

PRODIT_USERNAME=os.environ['PRODIT_USERNAME']
PRODIT_PASSWORD=os.environ['PRODIT_PASSWORD']
HUE_USERNAME=os.environ['HUE_USERNAME']
SLACK_COMWORK_TOKEN=os.environ['SLACK_COMWORK_TOKEN']
LIGHT_NUMBER=os.environ['LIGHT_NUMBER']
SLACK_UPRODIT_USERNAME=os.environ['SLACK_UPRODIT_USERNAME']

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
    r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, LIGHT_NUMBER), json = {"on": True, "sat": 254, "bri": bri, "hue": color})
    print(r.content)

def slack_message(emoji, channel, color, message, token, user):
  r = requests.post("https://hooks.slack.com/services/{}".format(token), json = {"channel": channel, "username": user, "icon_emoji": emoji, "attachments": [{"color": color, "text": message}]})
  print(r.content)

def appstatus_status(url, username, password):
   page=requests.get("{}?p=radiator".format(url), auth=(username, password))
   tree = html.fromstring(page.content)
   val=tree.xpath('//a[@href="?p=status" and @class="btn btn-large btn-success"]/text()')
   result = len(val) >= 1
   if not result:
      slack_message(":scream_cat:", "prod", "#BB0000", "There is a problem on uprodit, check the following page: {}".format(url), SLACK_COMWORK_TOKEN, SLACK_UPRODIT_USERNAME)
   return result

def check_uprodit():
  while True:
    status = appstatus_status("https://www.uprodit.com/status", PRODIT_USERNAME, PRODIT_PASSWORD)
    status = status and appstatus_status("http://91.121.80.56:8080/prodit-ws/status", PRODIT_USERNAME, PRODIT_PASSWORD)

    if status:
      change_color(HUE_BRI_OK, HUE_COLOR_OK)
    else:
      change_color(HUE_BRI_KO, HUE_COLOR_KO)
