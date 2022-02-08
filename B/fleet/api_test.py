import unittest
import requests
class ApiTest(unittest.TestCase):
    API_URL = "http://172.17.0.1:5022"
    DRIVERS_URL = "{}/drivers/".format(API_URL)
    VEHICLES_URL = "{}/vehicles/".format(API_URL)
    ASSIGNMENTS_URL = "{}/assignments/".format(API_URL)

    DRIVER_OBJ = {
	    "name": "Usertest",
        "first_lastname": "lastnameTest",
        "second_lastname": "lastnameTest",
        "email": "test@envioclick.com",
        "phone": "000000000",
        "credential_type": "C",
		"dob": "1990-01-01"
                }
    
    VEHICLE_OBJ = {
        "model": "Testmodel",
        "brand": "Testbrand",
        "vehicle_type": "TestType",
        "maximum_laded_weight": 20,
        "VIN":"TESTR41JXMM109125"
                }


    def test_create_driver(self):
        r = requests.post(ApiTest.DRIVERS_URL, json=ApiTest.DRIVER_OBJ)
        self.assertEqual(r.status_code, 201)


    def test_create_vehicle(self):
        r = requests.post(ApiTest.VEHICLES_URL, json=ApiTest.VEHICLE_OBJ)
        self.assertEqual(r.status_code, 201)    

if __name__ == '__main__':
    unittest.main()