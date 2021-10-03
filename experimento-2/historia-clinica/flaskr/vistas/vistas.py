from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, exceptions


class VistaHistoriaClinica(Resource):

    @jwt_required()
    def get(self):
        return {"msg":"Accede exitosamente a la información de historia clínica"}
