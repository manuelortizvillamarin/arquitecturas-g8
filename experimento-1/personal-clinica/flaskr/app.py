from flask_cors import CORS
from flask_restful import Api
from flaskr import create_app
from .vistas import VistaHealthCheck, VistaEntradaPacientes

app = create_app('default')
app_context = app.app_context()
app_context.push()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaHealthCheck, '/health')
api.add_resource(VistaEntradaPacientes, '/entrada_paciente')
