import uuid
import datetime
import pytz

from sqlalchemy_utils import UUIDType
from app.database import Base
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

tz = pytz.timezone('America/Mexico_City')

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(UUIDType(binary=False), primary_key=True)
    vehicle_id = Column(UUIDType(binary=False), ForeignKey('vehicles.id'))
    driver_id =  Column(UUIDType(binary=False), ForeignKey('drivers.id'))
    expiration_date = Column(DateTime, nullable = False, default = datetime.datetime.now(tz=tz))
    is_expired = Column(Boolean, default=False)
    area = Column(String(300))
    notes = Column(Text())
    created_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz))
    updated_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz),onupdate=datetime.datetime.now(tz=tz))

    
    def __init__(self, vehicle_id, driver_id, expiration_date, is_expired, area, notes):
        self.id = uuid.uuid4()
        self.vehicle_id = vehicle_id    
        self.driver_id = driver_id
        self.expiration_date = expiration_date
        self.is_expired = is_expired
        self.area = area
        self.notes = notes
        self.created_at = datetime.datetime.now(tz=tz)
        self.updated_at = datetime.datetime.now(tz=tz)