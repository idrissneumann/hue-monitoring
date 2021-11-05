from flask_restful import Resource

import os

from party_utils import party_async_process, stop_party
from utils import log_msg

pid = os.getpid()
class StopPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopPartyEndPoint", "kill party_async_process")
        party_async_process.terminate()
        stop_party()
        os._exit(1)
