from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):  # Capitalized class name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name and email:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    else:
        return jsonify({"error": "Name and Email are required"}), 400

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)

@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_to_delete = User.query.get(id)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "User deleted successfully!"})
    else:
        return jsonify({"error": "User not found"})
    
@app.route('/update_user/<int:id>', methods = ['PUT'])
def update_user(id):
    user = db.session.get(User,id)
    if not user:
        return jsonify({"error": "User not found!"})
    
    data =  request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Both name and email are required for full update"})
    
    user.name = name
    user.email = email
    db.session.commit()

    return jsonify({"Message": "User Add Updated Successfully!"})

     
@app.route('/update_user/<int:id>', methods = ['PATCH'])
def patch_user(id):
    user = db.session.get(User, id)
    if not user:
        return jsonify({"error": "User not found!"})
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name is not None:
        user.name = name
    if email is not None:
        user.email = email

    db.session.commit()

    return jsonify({"Message": "User Update Successfully!"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=1111)
