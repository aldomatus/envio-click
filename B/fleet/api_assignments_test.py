import unittest
import requests
import time
class ApiTest(unittest.TestCase):
    API_URL = "http://172.17.0.1:5022"
    ASSIGNMENTS_URL = "{}/assignments/".format(API_URL)
    
    ASSIGNMENTS_OBJ = {

        "VIN": "TESTR41JXMM109125",
        "driver_email":"test@envioclick.com",
        "notes": "Test",
        "area":"TestArea",
        "expiration_date": "2022-03-13",
        "is_expired": False
				}

    DRIVER_EMAIL = 'aldo.matus@envioclick.com'


    def test_create_driver(self):
        r = requests.post(ApiTest.DRIVERS_URL, json=ApiTest.DRIVER_OBJ)
        self.assertEqual(r.status_code, 201)


    def test_create_vehicle(self):
        r = requests.post(ApiTest.VEHICLES_URL, json=ApiTest.VEHICLE_OBJ)
        self.assertEqual(r.status_code, 201)


    def test_get_driver(self):
        GET_DRIVER_ASSIGNMENTS = "{}get_assignment/{}".format(ApiTest.ASSIGNMENTS_URL, ApiTest.DRIVER_EMAIL)
        r = requests.get(GET_DRIVER_ASSIGNMENTS)
        self.assertEqual(r.status_code, 200)
    
    time.sleep(5) # Esperar 2 segundos para guardar los registros de driver y vehicle



class ApiAssignmentsTest(unittest.TestCase):
    def test_create_assignments(self):
        r = requests.post(ApiTest.ASSIGNMENTS_URL, json=ApiTest.ASSIGNMENTS_OBJ)
        self.assertEqual(r.status_code, 201)


if __name__ == '__main__':
    unittest.main()