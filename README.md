# Disaster Response Pipeline Project
## Installation
There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

### Summary:
To help emergency workers in different organizations make quick response for people who need help, the project create a web app to classify a new message in several categories, such as water, food, medical supplies. To classify the message into several categories, I trained a multioutput random forest classifier. 

### Data Descriptions:
The data are real messages that were sent during disaster events provided by Figure Eight. There are two csv files called disaster_messages.csv
and disaster_categories.csv in data folder. 

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
