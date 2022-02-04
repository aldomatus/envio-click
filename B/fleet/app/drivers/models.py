import uuid
import datetime
import pytz

from sqlalchemy_utils import UUIDType
from app.database import Base
from sqlalchemy import Column, String, DateTime, Boolean 

tz = pytz.timezone('America/Mexico_City')

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(String(120))
    first_lastname = Column(String(120))
    second_lastname = Column(String(120))
    dob = Column(DateTime, nullable=True, default = datetime.datetime(1990, 1, 1, hour=0, minute=0, second=0, microsecond=0))
    email = Column(String(120), unique=True)
    phone = Column(String(10))
    credential_type = Column(String(5))
    created_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz))
    updated_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz),onupdate=datetime.datetime.now(tz=tz))

    
    def __init__(self, email, name, first_lastname, second_lastname, dob, phone, credential_type):
        self.id = uuid.uuid4()
        self.email = email    
        self.name = name
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.dob = dob
        self.phone = phone
        self.credential_type = credential_type
        self.created_at = datetime.datetime.now(tz=tz)
        self.updated_at = datetime.datetime.now(tz=tz)