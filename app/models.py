from .extensions import db
from flask_security import UserMixin, RoleMixin

# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Summoner(db.Model):
    __tablename__ = 'summoner'
    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.BigInteger)
    name = db.Column(db.String(45))
    profile_icon_id = db.Column(db.INTEGER)
    revision_date = db.Column(db.BigInteger)
    summoner_level = db.Column(db.BigInteger)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.account_id = kwargs['accountId']
        self.name = kwargs['name']
        self.profile_icon_id = kwargs['profileIconId']
        self.revision_date = kwargs['revisionDate']
        self.summoner_level = kwargs['summonerLevel']