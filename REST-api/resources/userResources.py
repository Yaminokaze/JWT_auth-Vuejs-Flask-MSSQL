from flask_restful import Resource, reqparse
from models.user import User
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from datetime import datetime
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)
parser.add_argument(
    'email', required=False)
parser.add_argument(
    'birthdayDate', required=False)
parser.add_argument(
    'country', required=False)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        new_user = User(
            username=data['username'],
            email=data['email'],
            country=data['country'],
            birthdayDate=datetime.strptime(
                data['birthdayDate'], "%d/%m/%Y").date() if data['birthdayDate'] is not None else None,
            password=User.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            response_object = {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            response_object = {'message': 'Something went wrong'}, 500
        pass

        return jsonify(response_object)


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class SecretResource(Resource):
    @jwt_required
    def get(self):
        userIdentity = get_jwt_identity()
        current_user = User.find_by_username(userIdentity)
        return {
            'username': '{}'.format(current_user.username),
            'email': '{}'.format(current_user.email),
            'country': '{}'.format(current_user.country),
            'birthdayDate': '{}'.format(current_user.birthdayDate),
        }, 200
