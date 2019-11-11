import requests
import json
import time
import random

import os

HUE_USERNAME = os.environ['HUE_USERNAME']

HUE_BRI=254

global stop_party
stop_party=True

def get_bridge_ip():
    page=requests.get("https://discovery.meethue.com/")
    payload = json.loads(page.content)
    if len(payload) >= 1:
      return payload[0]['internalipaddress']
    else:
      return ""

def random_color():
    return random.randint(0,65535)

def change_color(bri, color, light):
    r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, light), json = {"on": True, "sat": 254, "bri": bri, "hue": color})
    print("color = {}, light = {}, response = {}".format(color, light, r.content))

def go_party():
  global stop_party
  stop_party = False
  while not stop_party:
    change_color(0, 0, 1)
    change_color(0, 0, 2)
    change_color(0, 0, 3)
    time.sleep(0.3)
    change_color(HUE_BRI, random_color(), 1)
    change_color(HUE_BRI, random_color(), 2)
    change_color(HUE_BRI, random_color(), 3)
    time.sleep(0.7)


def stop_party():
  global stop_party
  stop_party = True
