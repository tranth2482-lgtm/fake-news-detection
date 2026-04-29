from flask import Blueprint, request, jsonify
from .models import History
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Backend OK"

@main.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text")

    result = "Fake"
    confidence = 0.9

    record = History(
        content=text,
        result=result,
        confidence=confidence
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({
        "result": result,
        "confidence": confidence
    })

@main.route("/get-history")
def get_history():
    records = History.query.all()
    return jsonify([r.to_dict() for r in records])