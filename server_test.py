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

	
	def test_b_get_people(self):
		result = self.app.get('/people') 				
		self.assertEqual(result.status_code, 200) 
		data =  json.loads(result.data)		
		self.assertTrue(len(data)>= 7)	
	def test_c_get_people_age(self):
		result = self.app.get('/people/age') 				
		self.assertEqual(result.status_code, 200) 
		data =  json.loads(result.data)		
		self.assertTrue(len(data)>= 7)	

	def test_d_get_people_lastname(self):
		result = self.app.get('/ids/lastname/Robiner') 				
		self.assertEqual(result.status_code, 200) 
		data =  json.loads(result.data)	
		self.assertTrue(len(data)>= 3)		
	def test_e_add_person(self):
		id = random.randint(20,1000)		
		result = self.app.post('/add/person',json = {"Age": 55, 
				"Dateof3rdGradeGraduation": "02/22/20", 
				"First": "First 1", 
				"GithubAcct": "abcd", 
				"ID": id, 
				"Last": "Robiner1"}) 				
		self.assertEqual(result.status_code, 200) 		
		 
	def test_f_add_person_existing_id(self):		
		result = self.app.post('/add/person',json = {"Age": 55, 
				"Dateof3rdGradeGraduation": "02/22/20", 
				"First": "First 1", 
				"GithubAcct": "abcd", 
				"ID": 15, 
				"Last": "Robiner1"})
			
		self.assertEqual(result.status_code, 400) 		
