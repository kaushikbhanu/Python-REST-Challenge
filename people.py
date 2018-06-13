import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from json import JSONEncoder
Base = declarative_base()
class Person(Base):
	__tablename__ = 'person'
	_ID = Column(Integer, primary_key=True)
	_First = Column(String(250))
	_Last = Column(String(250))
	_Age = Column(Integer)
	_GithubAcct = Column(String(250))
	_Dateof3rdGradeGraduation = Column(Date)
class PersonEncoder(JSONEncoder):	
	def default(self, o):
		if isinstance(o, Person): 
			return { "ID" : o._ID,
				 "First" : o._First, 
				 "Last" : o._Last, 
				 "Age" : o._Age, 
				 "GithubAcct" : o._GithubAcct, 
				 "Date of 3rd Grade Graduation" : str(o._Dateof3rdGradeGraduation) }
		return JSONEncoder.default(self, o)

def initializeDb(fileName="persons.csv", forceNewDbCreation=False):
	if forceNewDbCreation:
		os.remove("persons.db")
	databaseExists =  False
	if os.path.isfile("persons.db"):
		databaseExists = True
	engine = create_engine('sqlite:///persons.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	if not databaseExists or forceNewDbCreation:		
		with open(fileName) as f:        
			next(f)
			for line in f:			
				personvalues = line.split(",")        
				id = int(personvalues[0])
				first = personvalues[1]
				last = personvalues[2]
				age = None
				try:
					age = int(personvalues[3])
				except:
					pass
				githubacct = personvalues[4]
				dateText = personvalues[5].replace("\n","")			
				dateof3rdGraduation = None
				try:
					dateof3rdGraduation = datetime.strptime(dateText,"%m/%d/%y")
				except:
					pass	
				per = Person(_ID = id,_First=first,_Last = last,_Age = age,_GithubAcct =githubacct,_Dateof3rdGradeGraduation=dateof3rdGraduation)	
				session.add(per)
			session.commit()
	return session
initializeDb()