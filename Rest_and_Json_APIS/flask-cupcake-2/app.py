# app.py - Flask App for Cupcake API
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

with app.app_context():
    db.create_all()

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})

@app.route("/")
def homepage():
    """Render homepage showing all cupcakes."""
    cupcakes = Cupcake.query.all()
    return render_template("index.html", cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["GET"])
def get_all_cupcakes():
    """Retrieve all cupcakes as JSON data."""
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """Create a new cupcake and return its data as JSON."""
    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data.get('image') or None
    )

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict()), 201


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["GET"])
def get_single_cupcake(cupcake_id):
    """Retrieve a specific cupcake by ID and return its data as JSON."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def modify_cupcake(cupcake_id):
    """Update details of a specific cupcake and return the updated data."""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # Update fields only if new data is provided; keep existing values otherwise
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    
    # Convert rating to float if provided to ensure correct data type
    if 'rating' in data:
        cupcake.rating = float(data['rating'])
    cupcake.image = data.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict()), 200  # Explicitly return 200 OK



@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete a cupcake by ID and return confirmation message."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
