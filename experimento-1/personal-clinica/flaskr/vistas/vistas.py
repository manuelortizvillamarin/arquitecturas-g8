from flask_restful import Resource


class VistaHealthCheck(Resource):

    def get(self):
        return '', 200


class VistaEntradaPacientes(Resource):

    def post(self):
        for i in range(400000):
            print(i)
        return '', 200
