from flask import Blueprint, request, jsonify
from .models import History
from . import db

#  import model
from .predictor import predict_text, extract_keywords

main = Blueprint("main", __name__)


@main.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    #  dùng model thật
    result, confidence = predict_text(text)
    keywords = extract_keywords(text)

    #  lưu DB
    record = History(
        content=text,
        result=result,
        confidence=confidence
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({
        "result": result,
        "confidence": confidence,
        "keywords": keywords
    })


@main.route("/get-history", methods=["GET"])
def get_history():
    records = History.query.order_by(History.created_at.desc()).all()

    data = []
    for r in records:
        data.append({
            "id": r.id,
            "content": r.content,
            "result": r.result,
            "confidence": r.confidence,
            "created_at": str(r.created_at)
        })

    return jsonify(data)