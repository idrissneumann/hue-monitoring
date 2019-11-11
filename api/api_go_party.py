from flask_restful import Resource
from multiprocessing import Process

from party_utils import go_party

class GoPartyEndPoint(Resource):
    def get(self):
        async_process = Process( 
            target=go_party,
            daemon=True
        )
        async_process.start()
        return {
            'status': 'ok'
        }
