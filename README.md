
# Instructions
Fork this repository and submit a url to the forked repository with your solution.
Please provide documentation in this README explaining the following:
- How to run including any configuration needed
USAGE: python server.py -d <port> <csv_filename>

- Any thoughts on how to expand this application in the future
Test Features:
extend the tests to cover more issues and boundary conditions. 
create testcases for data matching tests to validate the data not just statuses and lengths
Application Improvements:
Better error handling of more cases returning error messages faulty data checks and returning proper Http error messages and codes
Missing data and validation
Application Features:
Connecting to github accounts based on the ids and adding user activity information. 
Generating basic stats such as mean age of people. 
Aggreted summaries such as number of people who graduated in different decates,number of people who have github accounts in different decates,number of people who have github accounts in different decates. 
Plotting charts/dashboards for these aggregations and summaries.

- What you have covered or not covered.
Used a sqlalchemy engine to persist the data in a sqllite database.
Parsed the csv file to populate the database and return session.
Implemented Person class to create person instances
Implemented a JSON encoder to encode the person objects
Implemented the basic functionality as required. 
Implemented basic unit tests for success cases (could be be more elaborate and need more work)


## General instructions and tasks
Read and pull in data from people.csv.
Fill in the requests in server.py where TODOs are stated in the comments.
Get as many done as you can.
If you have time create unit tests.
Feel free to add other systems to the application.
Also feel free to submit issues on this public branch with questions if you have any.

