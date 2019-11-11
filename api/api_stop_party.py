from flask_restful import Resource
from multiprocessing import Process

from party_utils import stop_party

class StopPartyEndPoint(Resource):
    def get(self):
        async_process = Process( 
            target=stop_party,
            daemon=True
        )
        async_process.start()
        return {
            'status': 'ok'
        }
