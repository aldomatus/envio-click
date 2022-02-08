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

    DRIVER_EMAIL = 'test@envioclick.com'
    VEHICLE_VIN = 'TESTR41JXMM109125'

    def test_create_assignments(self):
        r = requests.post(ApiTest.ASSIGNMENTS_URL, json=ApiTest.ASSIGNMENTS_OBJ)
        self.assertEqual(r.status_code, 201)


    def test_get_driver(self):
        GET_DRIVER_ASSIGNMENTS = "{}get_assignment/{}".format(ApiTest.ASSIGNMENTS_URL, ApiTest.DRIVER_EMAIL)
        r = requests.get(GET_DRIVER_ASSIGNMENTS)
        self.assertEqual(r.status_code, 200)


    def test_cancel_assignments(self):
        CANCEL_DRIVER_ASSIGNMENTS = "{}cancel_assignment/{}/{}".format(ApiTest.ASSIGNMENTS_URL, ApiTest.DRIVER_EMAIL, ApiTest.VEHICLE_VIN)
        r = requests.put(CANCEL_DRIVER_ASSIGNMENTS)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()