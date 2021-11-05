from flask_restful import Resource
from multiprocessing import Process

from party_utils import go_party, party_async_process

class GoPartyEndPoint(Resource):
    def get(self):
        global party_async_process
        if party_async_process is None:
            party_async_process = Process( 
                target=go_party,
                daemon=True
            )
            party_async_process.start()
        return {
            'status': 'ok'
        }
