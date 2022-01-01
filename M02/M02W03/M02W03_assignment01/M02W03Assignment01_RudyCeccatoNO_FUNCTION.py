# -*- coding: utf-8 -*-
"""
@author: Ceccato Rudy

M2 - W3 Assignment: Transforming Data Structures

Due Saturday 25th by 23:59 Points 100 

Most of the time you will work on reshaping, modifying and transforming data structures in your data science projects. 
In this week’s assignment you are expected to do the following to transform your data.


Step 1: Write a function to transform a “hash/dictionary” into a list (in conservative order)

Step 2: Write a function to transform a “hash/dictionary” into a 2D tuple

Step 3: Write a function to transform a 2D “tuple” into a list

Step 4: Write a function to transform a  2D “tuple” into a “hash/dictionary”
 

Use example data structures that you can create based on your current level of knowledge. 
Make sure you execute the functions to show that they work correctly. 
Submit your solution on Campus as a Jupyter notebook.


"""

########################################
####PYTHON PROGRAM TO DEMONSTRATE CONVERSIONS 
####FROM/TO DIFFERENT DATA STRUCTURES
########################################

####Step 1: Write a function to transform a “hash/dictionary” 
####into a list (in conservative order)
####FROM DICTIONARY TO LIST
#creating a simple 1D dictionary
a_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#### Method 01 converting from dictionary to list
##Using item() and list() RETURNS LIST OF TUPLES
dict_to_list01 = list(a_dict.items()) 
print("First Dictionary to list of tuples conversion: \n", dict_to_list01)

#### Method 02 converting from dictionary to list
##Looping through dictionary and use items() and append()
## RETURNS LIST OF LIST - 2D list
##generate empty list
dict_to_list02 = []
for keys,values in a_dict.items():
    dict_to_list02.append([keys, values])
print("Second Dictionary to list conversion: \n", dict_to_list02)

#### Method 03 converting from dictionary to list
####SAME AS ABOVE BUT WITH LIST COMPREHENSION
##Using list comprehension to create a list for the keys and values
##and the 
##Using list comprehension + dict(zip())
dict_to_list03 = []
keysList = [key for key in a_dict]
print(keysList)
dict_to_list03.append(keysList)
values = [a_dict[key] for key in a_dict]
dict_to_list03.append(values)
print("Third Dictionary to list conversion, keys and values as separate lists: \n", dict_to_list03)

#### Method 04 converting from dictionary to list
##looping though dictionary and retrieving individual keys and values to append
dict_to_list04 = []
for key in a_dict:
    dict_to_list04.append(key)
    dict_to_list04.append(a_dict[key])
print("Fourth Dictionary to list conversion one long list: \n", dict_to_list04)

#### Method 05 converting from dictionary to list
##Dictionary inside list
dict_to_list05 = [{key:value for (key,value) in a_dict.items()}]
print("Fifth Dictionary to list conversion list with inner dictionary: \n", dict_to_list05)

####Step 2: Write a function to transform a “hash/dictionary” 
####into a 2D tuple
####FROM DICTIONARY TO 2D TUPLE

##Looping through dictionary and use items() and append()
## RETURNS TUPLE OF TUPLE - 2D list
##Using item() and tuple() RETURNS 2D TUPLES
dict_to_tuple01 = tuple(a_dict.items()) 
print(" Dictionary to 2D TUPLE conversion: \n",  dict_to_tuple01)


####Step 3: Write a function to transform a 2D “tuple” into a list
tuple_to_list01 = [list(item) for item in dict_to_tuple01]
print("2D TUPLE to 2D list conversion: \n", tuple_to_list01)

##Step 4: Write a function to transform a  2D “tuple” into a “hash/dictionary
tuple_to_dict01 = dict((item[0], item[1]) for item in dict_to_tuple01)
print("2D TUPLE to Dictionary conversion: \n", tuple_to_dict01)


# # Conversion of JSON data to
# ##importing and reading the csv file
# with open("./Homelessness_Report_10_2021.csv", mode = 'r') as in_file:
#     reader = csv.reader(in_file)
    
#     col_headers = []
#     ##exctracting headers with next() method
#     col_headers = next(reader)
   
#     ##exctracting each table row using comprehension - loop method also included
#     rows = [row for row in reader ]
#     # for row in reader:
#     #     rows.append(row)
#     print(rows)
    
# #converting the headers list into dictionary for reference
# headers_ref ={n:col_headers[n-1] for n in range(0, len(col_headers)+1)}
# #print(rows)
# print(col_headers)##for reference
 
 
 
 
 

 
# # Opening JSON file
# with open("./Homelessness_Report_10_2021.json") as json_file:
#     in_data = json.load(json_file)
    
#     # for reading nested data [0] represents
#     # the index value of the list
# ####print(in_data) #### a list of dictionaries
    

#     # listed_json = list(in_data)
#     # print(listed_json)

#     # # for printing the key-value pair of
#     # # nested dictionary for loop can be used
#     # print("\nPrinting nested dictionary as a key-value pair\n")
#     # for i in in_data:
#     #     print("Total Adults", )
#     #     print("Male Adults", )
#     #     print("Female Adults", i[])
#     #     print()