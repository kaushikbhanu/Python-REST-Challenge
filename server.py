from flask import Flask, request, jsonify, Response
import argparse
import sys
from people import *

#Web app
app = Flask(__name__)
@app.route('/ping',methods=['GET'])
def pingServer():
    '''
    Ping request to make sure server is alive, return 'pong'
    '''        
    return Response("pong",200)

@app.route('/people',methods=['GET'])
def getPeople():
    '''
    Return a standard JSON block of people in any order of format. Must be valid JSON
    '''    
    return jsonify(session.query(Person).all())


@app.route('/people/age',methods=['GET'])
def sortPeopleByAge():
    '''
    Returns Json block containing a list of people sorted by age youngest to oldest
    '''    
    return jsonify(session.query(Person).order_by("_Age").all())
    
@app.route('/ids/lastname/<lastname>',methods=['GET'])
def getIdsByLastName(lastname):
    '''
    Returns Json block of ids found for the given last name
    Using path params
    '''    
    return jsonify(session.query(Person).filter_by(_Last=lastname).with_entities(Person._ID).all())


# TODO Create an endpoint POST that accepts a 'person' and appends it to our people. Returns the newley update JSON block of all people.
# New endpoint goes here.
@app.route('/add/person',methods=['POST'])
def addPerson():
    '''
    accepts a 'person' and appends it to our people. 
    Returns the newley update JSON block of all people.
    '''    
    # just adding some basic checks. id should be self incremental but as its not specified, expecting it from user
    req_data = request.get_json()
    print(req_data)
    assert "ID" in req_data.keys()
    assert "First" in req_data.keys()
    assert "Last" in req_data.keys()
    assert "Age" in req_data.keys()
    assert "GithubAcct" in req_data.keys()
    assert "Dateof3rdGradeGraduation" in req_data.keys()
    id = None
    first=None
    last = None
    age = None
    githubacct = None
    dateof3rdGraduation = None
    try:
        id = int(req_data["ID"])
    except:
        return Response("Id field is bad", 400)
        
    first=req_data["First"]
    last = req_data["Last"]
    try:
        age = int(req_data["Age"])
    except:
        pass
    githubacct = req_data["GithubAcct"]
    try:
        dateof3rdGraduation = datetime.strptime(req_data["Dateof3rdGradeGraduation"],"%m/%d/%y")
    except:
        pass
    try:
        per = Person(_ID = id,_First=first,_Last = last,_Age = age,_GithubAcct =githubacct,_Dateof3rdGradeGraduation=dateof3rdGraduation)
        session.add(per)
        session.commit()
    except:
        return Response("Error in adding the record", 400)
    return jsonify(session.query(Person).all())

# Optional Challenge: Persist the data somehow


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--debug", help="Optional Debug Mode for stack traces", action="store_true")

    # TODO: pass in a port from the command line and run on that port i.e. 'python3 server.py 9000 test.csv'
    parser.add_argument("port", help="Port to run server")
    parser.add_argument("file", help="File to import data from")
    args = parser.parse_args()

    # TODO: Initialize any pre-application start code here if needed
    # TODO: Read in people from people.csv into an appropraite data structure so that the endpoints can return data based
    #       on the data in the csv.    
    session = initializeDb(fileName = args.file,forceNewDbCreation=False)    
    app.json_encoder = PersonEncoder
    app.debug=args.debug
    app.run(port=args.port)

