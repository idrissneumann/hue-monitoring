from flask_restful import Resource

from party_utils import party_async_process
from utils import log_msg
class GoPartyEndPoint(Resource):
    def get(self):
        log_msg("INFO", "GoPartyEndPoint", "enable party_async_process")
        party_async_process.start()
        return {
            'status': 'ok'
        }
