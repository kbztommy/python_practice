from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_security import Security, SQLAlchemyUserDatastore
from .extensions import db, security, bootstrap
from .main import main as main_blueprint
from .filters import time_format_filter, champion_id_filter, item_id_filter, item_img_filter, champion_img_filter
from .filters import summoner_spell_id_filter, summoner_spell_img_filter


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    bootstrap.init_app(app)

    app.register_blueprint(main_blueprint)
    app.jinja_env.filters['timestamp_format'] = time_format_filter
    app.jinja_env.filters['champion_id_format'] = champion_id_filter
    app.jinja_env.filters['item_id_format'] = item_id_filter
    app.jinja_env.filters['item_img_format'] = item_img_filter
    app.jinja_env.filters['champion_img_format'] = champion_img_filter
    app.jinja_env.filters['summoner_spell_id_format'] = summoner_spell_id_filter
    app.jinja_env.filters['summoner_spell_img_format'] = summoner_spell_img_filter
    return app
