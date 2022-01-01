# -*- coding: utf-8 -*-
"""
@author: Ceccato Rudy
European Leadership University - Master in Data Science
Module 02 Assignment 01 

Assignment Title: First Glance at Python Data Structures

Assignment steps: Step 1: Create a structure to store multiple students’ data using Python’s basic data structures. 
                  Make sure each student will have the following features: Name, ID, Degree, StartYear. 
                  Each student will have multiple courses taken from a specific lecturer 
                  (e.g., each student can take N different courses from M different lecturer, each of the information must be defined)

Step 2: Show the structure that you have designed in JSON/CSV format.

Step 3: Use the necessary library to load the  data from a  file to the Python environment. 
        Submit the Python files of your codes as well as thefile.

Created on Thu Dec  09 
 
"""

## importing csv file in read mode
with open(".\students_enrollment_Rudy.csv", 'r') as csv_infile:
    ##reading and removing leading and trailing characters
    for line in csv_infile:
        print(line.strip())
        
##printing informations about the imported file (an object)
print(csv_infile)

#############################NEXT: attempt to use JSON; not working
# #### Converting our CSV file into JSON using Pandas - NOT WORKING AS EXPECTED
# # import pandas as pd
# # df = pd.read_csv (".\students_enrollment_Rudy.csv", 'r')
# # jsonVer = df.to_json (".\students_enrollment_Rudy.json")

# # print(jsonVer)

# ##### Importing and reading JSON  ###### NOTE: Getting an error
# import json as jn
# with open(".\students_enrollment_Rudy.json", "r") as json_infile:
#     json_data = jn.load(json_infile)


# print(jason_data)