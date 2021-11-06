import time
import random

from multiprocessing import Process

from hue_utils import change_color, HUE_USERNAME, HUE_LIGHTS_COUNT

HUE_BRI=254

def random_color():
  return random.randint(0, 65535)

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
