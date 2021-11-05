from flask_restful import Resource

global party_async_process
from party_utils import party_async_process

from utils import log_msg
class StopPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "StopPartyEndPoint", "kill party_async_process")
        party_async_process.kill()
        return {
            'status': 'ok'
        }
