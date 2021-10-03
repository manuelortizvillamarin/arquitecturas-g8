from flask_cors import CORS

from flaskr import create_app
from .servicio import monitor

app = create_app('default')
app_context = app.app_context()
app_context.push()

cors = CORS(app)

monitor.run()
