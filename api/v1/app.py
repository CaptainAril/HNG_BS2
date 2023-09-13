from flask import Flask, jsonify, request

from models import storage
from models.models import Person

app = Flask(__name__)

@app.route("/api/status")
def status():
    return jsonify({'status':'OK', 'code':200})


@app.route("/api", methods=['POST'])
def create_person():
    """Handles creation of Person object with `name`."""
    name = request.json.get('name')

    if name and isinstance(name, str):
        if storage.get(name=name):
            return jsonify(error=f"User ({name}) already exists!"), 400
        person = Person(name=name)
        person.create()
        return jsonify(person.to_dict()), 201
    else:
        return jsonify(error="Name must be a valid string!"), 400
    

@app.route("/api/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_person(id):
    """Handles retrieval, update and deletion of person with `id` from database."""
    person = storage.get(id=id)
    if not person:
        return jsonify(error=f"Person with id {id} not found!"), 404
    
    if request.method == 'GET':
        return jsonify(person.to_dict()), 200
    
    elif request.method == 'PUT':
        name = request.json.get('name')

        if name and isinstance(name, str):
            __user_exist = storage.get(name=name)
            if __user_exist and __user_exist is not person:
                return jsonify(error=f"Name ({name}) already exists!"), 400
            person.update(name=name)
            return jsonify(person.to_dict()), 200
        else:
            return jsonify(error="Name must be a valid string!"), 400
        
    elif request.method == 'DELETE':
        person.delete()
        return jsonify(message="Person deleted successfully!"), 200


@app.teardown_appcontext
def teardown(exception):
    """Tear down method"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """Handles HTTP 404 error"""
    return jsonify(error="Invalid Endpoint!"), 404

@app.errorhandler(415)
def error_415(error):
    """Handles HTTP 415 error"""
    return jsonify(error="Not a valid JSON!"), 415

@app.errorhandler(405)
def error_405(error):
    """Handles HTTP 405 error"""
    return jsonify(error="Method not allowed for endpoint!"), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, load_dotenv=True)
