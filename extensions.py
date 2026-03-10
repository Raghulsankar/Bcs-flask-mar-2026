from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()  # ORM
jwt = JWTManager()  # Manage Token  create and expire
