from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sensor.db"
db = SQLAlchemy(app)

class SensorData(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    timestamp   = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float, nullable=False)
    vibration   = db.Column(db.Float, nullable=False)
    humidity    = db.Column(db.Float, nullable=False)

@app.route("/sensor", methods=["POST"])
def add_sensor():
    data = request.get_json()
    sd = SensorData(
        temperature=data["temperature"],
        vibration=data["vibration"],
        humidity=data["humidity"]
    )
    db.session.add(sd)
    db.session.commit()
    return jsonify({"status": "ok"}), 201

@app.route("/sensor/latest")
def get_latest():
    limit = int(request.args.get("limit", 10))
    records = SensorData.query.order_by(SensorData.id.desc()).limit(limit).all()
    result = [
        {
            "id": r.id,
            "timestamp": r.timestamp.isoformat(),
            "temperature": r.temperature,
            "vibration": r.vibration,
            "humidity": r.humidity
        } for r in records
    ]
    return jsonify(result)

if __name__ == "__main__":
    # Uygulama bağlamını açıp tabloyu oluşturuyoruz (sadece ilk defa çalışır)
    with app.app_context():
        db.create_all()
    # API'yi debug modda ve 5000 portunda başlat
    app.run(debug=True, port=5000)
