from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Revoked_Token(db.Model):
    __tablename__ = 'Revoked_Token'
    __table_args__ = {'schema': 'Security'}

    id_revoke_token = db.Column(db.Integer, primary_key=True)
    jti_revoke_token = db.Column(
        db.String(120, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti: str) -> bool:
        db_result = cls.query.filter_by(jti_revoke_token=jti)
        if db_result:
            return True
        else:
            return False


class Status(db.Model):
    __tablename__ = 'Status'
    __table_args__ = {'schema': 'Catalogs'}

    status_id = db.Column(db.Integer, primary_key=True)
    descriptiion = db.Column(db.String(20, 'SQL_Latin1_General_CP1_CI_AS'))


class RolPerUser(db.Model):
    __tablename__ = 'Rol_Per_User'
    __table_args__ = {'schema': 'Security'}

    user_id = db.Column(db.ForeignKey('Security.User.user_id'),
                        primary_key=True, nullable=False)
    rol_id = db.Column(db.ForeignKey('Catalogs.Rol.rol_id'),
                       primary_key=True, nullable=False)
    status_id = db.Column(db.ForeignKey(
        'Catalogs.Status.status_id'), nullable=False)

    rol = db.relationship(
        'Rol', primaryjoin='RolPerUser.rol_id == Rol.rol_id', backref='rol_per_users')
    status = db.relationship(
        'Status', primaryjoin='RolPerUser.status_id == Status.status_id', backref='rol_per_users')
    user = db.relationship(
        'User', primaryjoin='RolPerUser.user_id == User.user_id', backref='rol_per_users')


class Rol(db.Model):
    __tablename__ = 'Rol'
    __table_args__ = {'schema': 'Catalogs'}

    rol_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(
        db.String(15, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    status_id = db.Column(db.ForeignKey(
        'Catalogs.Status.status_id'), nullable=False)

    Status = db.relationship(
        'Status', primaryjoin='Rol.status_id == Status.status_id', backref='rols')


class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'Security'}

    user_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(
        db.String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    password = db.Column(
        db.String(180, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    status_id = db.Column(db.ForeignKey('Catalogs.Status.status_id'))

    Status = db.relationship(
        'Status', primaryjoin='User.status_id == Status.status_id', backref='users')

    def get_id(self):
        return self.username

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'status': Status.serialize(self.status_id)
        }

    def save(self):
        self.user_id = self.get_next_id()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_next_id(cls):
        conn = db.engine.raw_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT NEXT VALUE FOR Security.user_id_seq AS user_id')
            res = list(cursor.fetchall())
            cursor.close()
            return res[0][0]
        finally:
            conn.close()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_all_usuers(cls):
        users = cls.query.all()
        return {'users': list(map(lambda element: cls.serialize(element), users))}


class Clinic(db.Model):
    __tablename__ = 'Clinic'
    __table_args__ = {'schema': 'Clinic'}

    clinic_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(120, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    name = db.Column(
        db.String(120, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    status_id = db.Column(db.ForeignKey('Catalogs.Status.status_id'))

    status = db.relationship(
        'Status', primaryjoin='Clinic.status_id == Status.status_id', backref='clinics')

    @classmethod
    def find_by_id(cls, clinic_id):
        return cls.query.filter_by(clinic_id=clinic_id).first()


class ClinicPerUser(db.Model):
    __tablename__ = 'Clinic_Per_User'
    __table_args__ = {'schema': 'Clinic'}

    user_id = db.Column(db.ForeignKey('Security.User.user_id'),
                        primary_key=True, nullable=False)
    clinic_id = db.Column(db.ForeignKey(
        'Clinic.Clinic.clinic_id'), primary_key=True, nullable=False)
    status_id = db.Column(db.ForeignKey(
        'Catalogs.Status.status_id'), nullable=False)

    clinic = db.relationship(
        'Clinic', primaryjoin='ClinicPerUser.clinic_id == Clinic.clinic_id', backref='clinic_per_users')
    status = db.relationship(
        'Status', primaryjoin='ClinicPerUser.status_id == Status.status_id', backref='clinic_per_users')
    user = db.relationship(
        'User', primaryjoin='ClinicPerUser.user_id == User.user_id', backref='clinic_per_users')
