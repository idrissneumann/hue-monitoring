from flask import Flask
from flask_restful import Api
from multiprocessing import Process

from hue_monitoring_utils import check_app
from api_root import RootEndPoint
from api_manifest import ManifestEndPoint
from api_go_party import GoPartyEndPoint
from api_stop_party import StopPartyEndPoint
from api_stop_lights import StopLightsEndPoint

app = Flask(__name__)
api = Api(app)

async_process = Process( 
    target=check_app,
    daemon=True
)
async_process.start()

health_check_routes = ['/', '/health', '/health/', '/v1', '/v1/', '/v1/health', '/v1/health/']
manifest_routes = ['/manifest', '/manifest/', '/v1/manifest', '/v1/manifest/']
go_party_routes = ['/party', '/party/', '/v1/party', '/v1/party/']
stop_party_routes = ['/party/stop', '/party/stop', '/v1/party/stop', '/v1/party/stop/']
stop_lights_routes = ['/lights/off', '/lights/off', '/v1/lights/off', '/v1/lights/off/']

api.add_resource(RootEndPoint, *health_check_routes)
api.add_resource(ManifestEndPoint, *manifest_routes)
api.add_resource(GoPartyEndPoint, *go_party_routes)
api.add_resource(StopPartyEndPoint, *stop_party_routes)
api.add_resource(StopLightsEndPoint, *stop_lights_routes)

if __name__ == '__main__':
    app.run()
