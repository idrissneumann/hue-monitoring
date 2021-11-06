import requests

import os
import json

from utils import log_msg, is_true

HUE_USERNAME=os.environ['HUE_USERNAME']
HUE_LIGHTS_COUNT = int(os.environ['HUE_LIGHTS_COUNT'])
HUE_MONITOR_LIGHTS_IDS=os.environ['HUE_MONITOR_LIGHTS_IDS'].split(",")
HUE_DISCOVERY_URL = os.environ['HUE_DISCOVERY_URL']

HUE_COLOR_KO=2000
HUE_COLOR_OK=30000

HUE_BRI_OK=20
HUE_BRI_KO=254

def get_bridge_ip():
    page=requests.get(HUE_DISCOVERY_URL)
    payload = json.loads(page.content)
    if len(payload) >= 1:
      return payload[0]['internalipaddress']
    else:
      return ""

def change_color(on, bri, color):
    for i in HUE_MONITOR_LIGHTS_IDS:
      r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, i), json = {"on": on, "sat": 254, "bri": bri, "hue": color})
      log_msg("DEBUG", "change_color", r.content)
