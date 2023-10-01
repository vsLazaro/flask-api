import uuid
from sqlalchemy import Column, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class PlaneCrash(Base):
    __tablename__ = 'plane_crash'
    
    id = Column(String(36), primary_key=True, default=generate_uuid, nullable=False)
    date = Column(String(20), nullable=False)
    time = Column(String(4), nullable=False)
    location = Column(String(255), nullable=False)
    operator = Column(String(255), nullable=False)
    flight_number = Column(String(50), nullable=False)
    route = Column(String(255), nullable=False)
    ac_type = Column(String(255), nullable=False)
    registration = Column(String(255), nullable=False)
    cn_ln = Column(String(255), nullable=False)
    aboard = Column(String(100), nullable=False)
    fatalities = Column(String(100), nullable=False)
    ground = Column(String(50), nullable=False)
    summary = Column(Text, nullable=False) 