from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from io import BytesIO
from pathlib import Path
from flask_mysqldb import MySQL

db = SQLAlchemy()

migrate = Migrate()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    db.app = app

    #Jalankan Flask db init dan db migrate dulu untuk kali pertama
    migrate.init_app(app, db)
    migrate.app = app

    from app.auth import bp_auth as auth
    app.register_blueprint(auth)

    from app.buku import bp_buku as buku
    app.register_blueprint(buku)

    from app.member import bp_member as member
    app.register_blueprint(member)

    from app.transaksi import bp_transaksi as transaksi
    app.register_blueprint(transaksi)

    app.add_url_rule('/', endpoint='index')
    db.create_all()
    return app