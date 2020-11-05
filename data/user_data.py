from .entities import User
from werkzeug.exceptions import InternalServerError

class UserData(User):
    @classmethod
    def register_user(cls, user_data):
        try:
            new_user = User(
                username=user_data['username'],
                password=user_data['password'],
                status_id=2
            )
            new_user.save()
        except Exception as err:
            print(err.args)
            raise InternalServerError('Ops! database exception')  # AQUI se insertara un manejador de logs para ver que pedo
