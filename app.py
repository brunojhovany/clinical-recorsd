from flask import Flask
from flask_restplus import Api
import os
from controllers import AuthenticationApi, UserApi
from flask_jwt_extended import JWTManager
from data import db, Revoked_Token, User


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
api = Api(app, version='0.1.0', title='Clinical records', doc='/docs')
jwt = JWTManager(app)

db.init_app(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return Revoked_Token.is_jti_blacklisted(jti)


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': User.Roles}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


@app.before_first_request
def create_database():
    db.create_all()


api.add_namespace(AuthenticationApi, path='/api/authentication')
api.add_namespace(UserApi, path='/api/user')

if __name__ == '__main__':
    app.run()
