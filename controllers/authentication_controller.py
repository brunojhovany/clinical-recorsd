from .namespaces import AuthenticationApi
from flask_restplus import Resource


@AuthenticationApi.route('/auth')
class AuthenticationController(Resource):
    def post(self):

        return {'message': 'ok esta listo'}
