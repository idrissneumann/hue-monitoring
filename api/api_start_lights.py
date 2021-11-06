from flask_restful import Resource

from utils import log_msg
from hue_utils import switch_on

class StartLightsEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopLights", "turn of lights")
        switch_on()
        return {
            "status": "ok"
        }
