from . import db
from datetime import datetime

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    result = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "result": self.result,
            "confidence": self.confidence,
            "created_at": str(self.created_at)
        }