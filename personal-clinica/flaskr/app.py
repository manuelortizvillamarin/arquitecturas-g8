from flaskr import create_app
from flask_restful import Api
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

cors = CORS(app)


