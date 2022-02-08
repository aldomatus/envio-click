import unittest
import requests
import time


class ApiTest(unittest.TestCase):
    API_URL = "http://172.17.0.1:5022"
    ASSIGNMENTS_URL = "{}/assignments/".format(API_URL)
    DRIVER_EMAIL = 'test@envioclick.com'
    VEHICLE_VIN = 'TESTR41JXMM109125'


    def test_cancel_assignments(self):
        CANCEL_DRIVER_ASSIGNMENTS = "{}cancel_assignment/{}/{}".format(ApiTest.ASSIGNMENTS_URL, ApiTest.DRIVER_EMAIL, ApiTest.VEHICLE_VIN)
        r = requests.put(CANCEL_DRIVER_ASSIGNMENTS)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()