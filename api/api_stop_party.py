from flask_restful import Resource

import os
import signal

from party_utils import party_async_process
from utils import log_msg

pid = os.getpid()
class StopPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopPartyEndPoint", "kill party_async_process")
        party_async_process.terminate()
        os.kill(pid, signal.SIGTERM)
