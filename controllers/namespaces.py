from flask_restplus import Namespace
from models.swagger import new_user_swgger


AuthenticationApi = Namespace('Authentication', 'All related with authentication')


UserApi = Namespace('User', 'User management')
UserApi.add_model('new_user', new_user_swgger)
