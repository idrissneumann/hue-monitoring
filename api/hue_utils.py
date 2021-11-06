import requests

import os
import json

from utils import log_msg

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

def hue_state(on, bri, color, light_id):
    r = requests.put("http://{}/api/{}/lights/{}/state".format(get_bridge_ip(), HUE_USERNAME, light_id), json = {"on": on, "sat": 254, "bri": bri, "hue": color})
    log_msg("DEBUG", "hue_state", r.content)

def hue_states(on, bri, color):
    for i in range(1, HUE_LIGHTS_COUNT):
      hue_state(on, bri, color, i)

def change_color(bri, color, light_id):
    hue_state(True, bri, color, light_id)

def switch_off():
    hue_states(False, 0, 0)
