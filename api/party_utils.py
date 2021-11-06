import requests
import json
import time
import random

import os

from multiprocessing import Process

from utils import log_msg, is_not_empty

HUE_USERNAME = os.environ['HUE_USERNAME']
HUE_DISCOVERY_URL = os.environ['HUE_DISCOVERY_URL']
HUE_LIGHTS_COUNT = int(os.environ['HUE_LIGHTS_COUNT'])

HUE_BRI=254

def get_bridge_ip():
  page=requests.get(HUE_DISCOVERY_URL)
  payload = json.loads(page.content)
  if is_not_empty(payload):
    return payload[0]['internalipaddress']
  
  return ""

def random_color():
  return random.randint(0, 65535)

def change_color(bri, color, light):
  r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, light), json = {"on": True, "sat": 254, "bri": bri, "hue": color})
  log_msg("DEBUG", "change_color", "color = {}, light = {}, response = {}".format(color, light, r.content))

def stop_party():
  for i in range(1, HUE_LIGHTS_COUNT):
    change_color(0, 0, i)

def go_party():
  while True:
    stop_party()
    time.sleep(0.3)
    for i in range(1, HUE_LIGHTS_COUNT):
      change_color(HUE_BRI, random_color(), i)
    time.sleep(0.7)

party_async_process = Process( 
  target=go_party,
  daemon=True
)
