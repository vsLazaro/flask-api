import uuid
from flask_sqlalchemy import SQLAlchemy

# Inicialização do SQLAlchemy
db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class PlaneCrash(db.Model):
    __tablename__ = 'plane_crash'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True, nullable=False)
    date = db.Column(db.String(20))
    time = db.Column(db.String(4))
    location = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    flight_number = db.Column(db.String(50))
    route = db.Column(db.String(255))
    ac_type = db.Column(db.String(255))
    registration = db.Column(db.String(255))
    cn_ln = db.Column(db.String(255))
    aboard = db.Column(db.String(100))
    fatalities = db.Column(db.String(100))
    ground = db.Column(db.String(50))
    summary = db.Column(db.Text) 