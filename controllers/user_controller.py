from flask import request
from flask_restplus import Resource
from .namespaces import UserApi
from models.swagger import new_user_swgger
from models.marshmallow import UserSchema
from marshmallow import ValidationError
from business import UserBusiness


@UserApi.route('/register')
class RegisterUser(Resource):
    @UserApi.expect(new_user_swgger)
    def post(self):
        try:
            payload = UserSchema().load(request.get_json())
            return UserBusiness.register_user(payload)
        except ValidationError as err:
            return {
                'message': 'EXPECTATION FAILED',
                'error': err.messages
            }, 417
