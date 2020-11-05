# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Rol(db.Model):
    __tablename__ = 'Rol'
    __table_args__ = {'schema': 'Catalogs'}

    rol_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    status_id = db.Column(db.ForeignKey('Catalogs.Status.status_id'), nullable=False)

    status = db.relationship('Status', primaryjoin='Rol.status_id == Status.status_id', backref='rols')



class Status(db.Model):
    __tablename__ = 'Status'
    __table_args__ = {'schema': 'Catalogs'}

    status_id = db.Column(db.Integer, primary_key=True)
    descriptiion = db.Column(db.String(20, 'SQL_Latin1_General_CP1_CI_AS'))



class RevokedToken(db.Model):
    __tablename__ = 'Revoked_Token'
    __table_args__ = {'schema': 'Security'}

    id_revoke_token = db.Column(db.Integer, primary_key=True)
    jti_revoke_token = db.Column(db.String(120, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)



class RolPerUser(db.Model):
    __tablename__ = 'Rol_Per_User'
    __table_args__ = {'schema': 'Security'}

    user_id = db.Column(db.ForeignKey('Security.User.user_id'), primary_key=True, nullable=False)
    rol_id = db.Column(db.ForeignKey('Catalogs.Rol.rol_id'), primary_key=True, nullable=False)
    status_id = db.Column(db.ForeignKey('Catalogs.Status.status_id'), nullable=False)

    rol = db.relationship('Rol', primaryjoin='RolPerUser.rol_id == Rol.rol_id', backref='rol_per_users')
    status = db.relationship('Status', primaryjoin='RolPerUser.status_id == Status.status_id', backref='rol_per_users')
    user = db.relationship('User', primaryjoin='RolPerUser.user_id == User.user_id', backref='rol_per_users')



class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'Security'}

    user_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    password = db.Column(db.String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    salt = db.Column(db.String(80, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    status_id = db.Column(db.ForeignKey('Catalogs.Status.status_id'))

    status = db.relationship('Status', primaryjoin='User.status_id == Status.status_id', backref='users')
