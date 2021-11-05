import requests
import json
import time
import random

import os

from multiprocessing import Process

HUE_USERNAME = os.environ['HUE_USERNAME']
HUE_DISCOVERY_URL = os.environ['HUE_DISCOVERY_URL']

HUE_BRI=254

def get_bridge_ip():
  page=requests.get(HUE_DISCOVERY_URL)
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

def stop_party():
  change_color(0, 0, 1)
  change_color(0, 0, 2)
  change_color(0, 0, 3)

def go_party():
  while True:
    stop_party()
    time.sleep(0.3)
    change_color(HUE_BRI, random_color(), 1)
    change_color(HUE_BRI, random_color(), 2)
    change_color(HUE_BRI, random_color(), 3)
    time.sleep(0.7)

party_async_process = Process( 
  target=go_party,
  daemon=True
)
