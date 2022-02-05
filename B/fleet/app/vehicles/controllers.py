from app.database import db_session
from app.vehicles.models import Vehicle
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import asc, and_
import pytz
import datetime

tz = pytz.timezone('America/Mexico_City')


def create_vehicle_expedient(request):
    try:
        if get_vehicle_expedient(request["VIN"]) == None:
            Vehicle_dict = {
                "model": request["model"],
                "brand": request["brand"],
                "vehicle_type": request["vehicle_type"],
                "maximum_laded_weight": request["maximum_laded_weight"],
                "VIN": request["VIN"],
            }        
            b = Vehicle(**Vehicle_dict)
            db_session.add(b)
            db_session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        False


def get_vehicle_expedient(VIN):
    try:
        return db_session.query(Vehicle).filter_by(VIN=VIN).one()
    except Exception as e:
        print('Vehicle does not exist in fleet database yet | ', e)
        return None