from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Tüm kaynaklara CORS izni

# SQLite veritabanı ayarı (aynı klasörde sensor.db dosyası oluşturur)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    vibration = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)

@app.route("/sensor", methods=["POST", "OPTIONS"])
def post_sensor():
    """
    Sensör verisini alır (JSON) ve veritabanına kaydeder.
    Örnek payload:
    {
      "temperature": 23.5,
      "vibration": 1.2,
      "humidity": 54.3
    }
    """
    data = request.get_json(force=True)
    sensor = SensorData(
        temperature=data.get("temperature"),
        vibration=data.get("vibration"),
        humidity=data.get("humidity")
    )
    db.session.add(sensor)
    db.session.commit()
    return jsonify({"status": "ok", "id": sensor.id}), 201

@app.route("/sensor", methods=["GET"])
@app.route("/sensor/latest", methods=["GET"])
def get_latest():
    """
    Son eklenen sensör verilerini döner.
    ?limit=param ile geri dönecek kayıt sayısını belirleyebilirsiniz (default 10).
    """
    limit = int(request.args.get("limit", 10))
    records = SensorData.query.order_by(SensorData.id.desc()).limit(limit).all()
    result = [
        {
            "id": r.id,
            "timestamp": r.timestamp.isoformat(),
            "temperature": r.temperature,
            "vibration": r.vibration,
            "humidity": r.humidity
        }
        for r in records
    ]
    return jsonify(result)

if __name__ == "__main__":
    # İlk çalıştırmada tabloyu oluştur
    with app.app_context():
        db.create_all()
    # Tüm arayüzlerden erişim için host="0.0.0.0"
    app.run(debug=True, host="0.0.0.0", port=5000)
