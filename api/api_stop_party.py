from flask_restful import Resource

import os
import signal

from utils import log_msg
class StopPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopPartyEndPoint", "kill party_async_process")
        os.kill(os.getpid(), signal.SIGTERM)
