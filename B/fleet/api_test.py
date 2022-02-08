import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://172.17.0.1:5022"
    DRIVERS_URL = "{}/drivers/".format(API_URL)

    DRIVER_OBJ = {
	    "name": "Usertest",
        "first_lastname": "lastnameTest",
        "second_lastname": "lastnameTest",
        "email": "test@envioclick.com",
        "phone": "000000000",
        "credential_type": "C",
		"dob": "1990-01-01"
                }

    def test_create_driver(self):
        r = requests.post(ApiTest.DRIVERS_URL, json=ApiTest.DRIVER_OBJ)
        self.assertEqual(r.status_code, 201)

if __name__ == '__main__':
    unittest.main()