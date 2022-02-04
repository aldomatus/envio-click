from app.database import db_session
from app.drivers.models import Driver
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import asc, and_
import pytz
import datetime

tz = pytz.timezone('America/Mexico_City')


def create_driver_expedient(request):
    try:
        if get_driver_expedient(request["email"]) == None:
            Driver_dict = {
                "email": request["email"],
                "name": request["name"],
                "first_lastname": request["first_lastname"],
                "second_lastname": request["second_lastname"],
                "phone": request["phone"],
                "credential_type": request["credential_type"],
                "dob": datetime.datetime.strptime(request['dob'], '%Y-%m-%d'),
            }        
            b = Driver(**Driver_dict)
            db_session.add(b)
            db_session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        False


def get_driver_expedient(email):
    try:
       return db_session.query(Driver).filter_by(email=email).one()
    except Exception as e:
        print('User does not exist in fleet database yet | ', e)
        return None