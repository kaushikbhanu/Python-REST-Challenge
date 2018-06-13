from server import app
import unittest 
import json
import random
class FlaskPersonTests(unittest.TestCase): 
	@classmethod
	def setUpClass(cls):
		pass 

	@classmethod
	def tearDownClass(cls):
		pass 

	def setUp(self):
		# creates a test client
		self.app = app.test_client()
		self.app.debug =FlaskPersonTests
		# propagate the exceptions to the test client
		self.app.testing = False 

	def tearDown(self):
		pass 

	def test_a_ping(self):
		# sends HTTP GET request to the application
		# on the specified path
		result = self.app.get('/ping') 		
		self.assertEqual(b'pong',result.data)
		# assert the status code of the response
		self.assertEqual(result.status_code, 200) 