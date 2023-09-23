from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False, required=True)
    image=db.Column(db.String(500), nullable=False, required=True)
    price=db.Column(db.Float, nullable=False, required=True)
