from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import initialize_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
initialize_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

routes = Blueprint('routes', __name__)

@routes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@routes.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    return jsonify({'username': user.username})

@routes.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    user.username = data['username']
    db.session.commit()
    return jsonify({'message': 'User updated!'})

@routes.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'})
    return jsonify({'message': 'Logged in successfully!'})

def initialize_routes(app):
    app.register_blueprint(routes)
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

routes = Blueprint('routes', __name__)

@routes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@routes.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    return jsonify({'username': user.username})

@routes.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    user.username = data['username']
    db.session.commit()
    return jsonify({'message': 'User updated!'})

@routes.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'})
    return jsonify({'message': 'Logged in successfully!'})

def initialize_routes(app):
    app.register_blueprint(routes)

