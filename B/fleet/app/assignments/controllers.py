from lib2to3.pgen2 import driver
from app.database import db_session
from app.assignments.models import Assignment
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import asc, and_

from app.drivers.controllers import get_driver_expedient
from app.vehicles.controllers import get_vehicle_expedient

import pytz
import datetime

tz = pytz.timezone('America/Mexico_City')


def create_assignment_expedient(request):
    try:
        list_id = get_id(request["driver_email"], request["VIN"])
        if get_assignment_expedient(list_id[1], list_id[0]) == None:
            Assignment_dict = {
                "vehicle_id": list_id[0],
                "driver_id": list_id[1],
                "expiration_date": datetime.datetime.strptime(request['expiration_date'], '%Y-%m-%d'),
                "area": request["area"],
                "notes": request["notes"],
                "is_expired": request["is_expired"],
            }      
            b = Assignment(**Assignment_dict)
            db_session.add(b)
            db_session.commit()
            return Assignment_dict, True
        else:
            return None, False
    except Exception as e:
        print(e)
        False


def get_assignment_expedient(driver_id, vehicle_id):
    try:
        return db_session.query(Assignment).filter(and_(Assignment.vehicle_id==str(vehicle_id).replace('-', ''), Assignment.driver_id==str(driver_id).replace('-', ''))).one()
    except Exception as e:
        print('assignment does not exist in fleet database yet | ', e)
        return None


def get_id(driver_email, vehicle_VIN):
    list_id = []
    try:
        list_id.append(get_vehicle_expedient(vehicle_VIN).id)
        list_id.append(get_driver_expedient(driver_email).id)
        return list_id
    except Exception as e:
        print(e)
        return None


def get_driver_assignments(driver_email):
    try:
        driver_id = get_driver_expedient(driver_email).id
        print(driver_id)
        assignments = db_session.query(Assignment).filter_by(driver_id=str(driver_id).replace('-', '')).all()

        dict_assignments = {}
        for assigment in assignments:
            dict_assignments[str(assigment.vehicle_id)] = {
                    "vehicle_id": assigment.vehicle_id,
                    "driver_id": assigment.driver_id,
                    "expiration_date": assigment.expiration_date,
                    "notes": assigment.notes,
                    "is_expired": assigment.is_expired,
                }
        return dict_assignments

    except Exception as e:
        print(f'Driver {driver_email} does not have any vehicle assigned yet | {e}')
        return None


def cancel_driver_assignments(driver_email, VIN):
    list_id = get_id(driver_email, VIN)
    assignment_to_cancel = get_assignment_expedient(list_id[1], list_id[0])
    assignment_to_cancel.is_expired = True
    db_session.add(assignment_to_cancel)
    db_session.commit()

    assigment = get_assignment_expedient(list_id[1], list_id[0])
    data = {}
    data = {
            "vehicle_id": assigment.vehicle_id,
            "driver_id": assigment.driver_id,
            "expiration_date": assigment.expiration_date,
            "is_expired": assigment.is_expired,
           }

    return (data)
