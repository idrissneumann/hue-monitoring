from flask_restful import Resource

import os

from party_utils import party_async_process, stop_party
from utils import log_msg

class StopPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopPartyEndPoint", "kill party_async_process")
        try:
            party_async_process.terminate()
            stop_party()
            os._exit(1)
        except AttributeError:
            return {
                "status": "ok",
                "details": "no process to stop"
            }
