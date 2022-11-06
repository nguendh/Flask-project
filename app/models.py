from flask import request, make_response, jsonify

from app import db
from flask_restful import Resource


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User {}, {}, {}>'.format(self.username, self.full_name, self.address)


