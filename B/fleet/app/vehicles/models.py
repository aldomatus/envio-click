import uuid
import datetime
import pytz

from sqlalchemy_utils import UUIDType
from app.database import Base
from sqlalchemy import Column, String, DateTime, Float 

tz = pytz.timezone('America/Mexico_City')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(UUIDType(binary=False), primary_key=True)
    model = Column(String(120))
    brand = Column(String(120))
    vehicle_type = Column(String(120))
    maximum_laded_weight = Column(Float, nullable=False, default=0)
    VIN = Column(String(120), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz))
    updated_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz),onupdate=datetime.datetime.now(tz=tz))

    
    def __init__(self, model, brand, vehicle_type, maximum_laded_weight, VIN):
        self.id = uuid.uuid4()
        self.model = model    
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.maximum_laded_weight = maximum_laded_weight
        self.VIN = VIN
        self.created_at = datetime.datetime.now(tz=tz)
        self.updated_at = datetime.datetime.now(tz=tz)