from flask_restplus import Model, fields


new_user_swgger = Model('new_user', {
    'username': fields.String(required=True, descripcion='username'),
    'password': fields.String(required=True, descripcion='strong pasword'),
    'clinic': fields.Integer(required=True)
})
