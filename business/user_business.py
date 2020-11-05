from data import UserData, ClinicData
from .security_business import PassworManager


class UserBusiness():
    @classmethod
    def register_user(cls, user_data: dict):
        try:
            clinic_id = user_data['clinic']
            clinic = ClinicData.find_by_id(clinic_id)
            if not clinic:
                return {
                    'message': 'can\'t register user',
                    'error': 'the clinic does not exist'
                }, 400
            hashed_password = PassworManager.hashpassword(user_data['password'])
            print(len(hashed_password))
            user_data['password'] = hashed_password
            UserData.register_user(user_data)
            return {'message': 'successfully registered user. contact your administrator to assign their roles'}, 200
        except Exception:
            return {
                'message': 'can\'t register user',
                'error': 'Internal server error'
            }, 500
