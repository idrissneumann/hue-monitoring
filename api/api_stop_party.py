from flask_restful import Resource

from party_utils import party_async_process
class StopPartyEndPoint(Resource):
    def get(self):
        global party_async_process
        if party_async_process is not None:
            party_async_process.kill()
            party_async_process = None
        return {
            'status': 'ok'
        }
