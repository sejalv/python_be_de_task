# RELAYR ONBOARDING

## Task 1: Python Test

### Objective 
The purpose of this test is to give us a small sample of your code and to see how you approach and solve a simple problem. Ideally you should not spend more than an hour or two on this. 

This is a simple class to extract matching strings from a list regardless of the characters order.
 
You will design & write a Python class that accepts a list of strings in the constructor. The class will expose a find function that accepts a string. The function will return all strings from the list that contain the exact same characters as the string passed into it. The order of the characters in the strings is not relevant. 
For example, the constructor should take an array as follows:

``` 
    string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']; 
    finder = Finder(string_list);
```

Calling `finder.find('sad')` should return a list containing the string "**asd**".

In the case where more than one member of the initialization list matches the key the return list will have more than one member. 

### Requirements
State your assumptions. Anywhere you feel that the requirements are unclear please make an assumption and document that assumption. Please comment your code where needed. Find the right balance between comments and self-documenting code. Code quality is of high importance. Strive to minimize the number of external dependencies. The performance of your code matters, so please try to keep your code as optimized as possible. Choose a testing framework and write tests to showcase the quality of your solution, its performance (e.g. 50k+ runs, large initialization arrays etc.) and its edge cases. Deliver 3-4 bullet points detailing the reasons for choosing the testing framework Python 3, PEP 8 

### Deliverables 
* python source-code and tests 
* Instructions on how to run your project as well as tests 
* Simple way of installing dependencies if needed 
* Any other material that you feel is relevant for your solution 

### Setup & Configuration
* **Step 1**: clone this repo (only one branch here: `master`)
* **Step 2**: sync and resolve dependencies: `pipenv install`

### Test App
- Run `pipenv shell`   
- Run `pytest` OR `pytest -v` (verbose)  
- Run `exit` to exit the shell

## Requirements
- [python 3.7](https://www.python.org/downloads/release/python-376/)
- [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
- [pytest](https://docs.pytest.org/en/latest/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)

[Pipfile](/Pipfile)


## Task 2: Big Data Deep-Dive

The purpose of this assignment is to help us understand your perspective on big data systems, ahead of the technical interviews. To achieve this, you are tasked with creating a high-level diagram of a big data system that solves the challenge of applying sentiment analysis to a real-time stream of tweets. 

### Assumptions 
* the sentiment analysis model is pre-trained and available 
* sentiment analysis models are available for all languages 
* you have direct access to the twitter firehose, outputting ~6k tweets per second 
* there is an SDK available that allows you to connect to the firehose 

### Requirements 
* the system is real-time 
* the system has a way to cope with back-pressure 
* the system routes tweets to the correct model depending on language 
* the system performs basic feature engineering as follows: 
* converting emoticons / smileys to tokens 
* converting GPS coordinates if available to City + Country 
* the system saves data to the database system of your choice 
* the system and the storage backend can scale horizontally 

### Deliverables 
* high-level description of the system (2-3 sentences)
* high-level system diagram (can be hand-drawn and photographed, no aesthetic requirements beyond readability) 
* description of libraries / frameworks chosen to solve the task (bullet points + 1 sentence for each suffice) 
* any observations that you feel are relevant 

### Notes 
* coding is not required 
* logic such as routing can be expressed using boxes and arrows 
* technology choices can be based on what's available or what you're familiar with
* there is generally no single right way to solve a task: focus on explaining your choices rather than finding the perfect tool 


[Answers](/task_2_big_data/README.md)

[Diagram](/task_2_big_data/RelayR_Task_2.jpeg)