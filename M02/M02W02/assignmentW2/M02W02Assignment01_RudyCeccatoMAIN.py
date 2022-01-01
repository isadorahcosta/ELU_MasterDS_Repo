# -*- coding: utf-8 -*-
"""
@author: Ceccato Rudy
European Leadership University - Master in Data Science
Module 02 Assignment 03 

Assignment Steps:

1. Download the following Black Friday (Links to an external site.)Links to an external site. dataset from Kaggle.

2. Create minimum 5 visualizations from this dataset and share your key observations. Motivate why you chose to perform these types of visualizations. What do they tell you about your data? 

Upload your solution Jupyter notebook on Campus. Please make sure to keep the executed outputs.

Dataset description:

The dataset is a sample of  transactions at a retails store. It contains information about different types of products purchases and some information about the customers. The store wants to better understand the customer purchase behavior with regards to different products.

Although the dataset is designed for a regression problem (where we are trying to predict the dependent variable (the amount of purchase) with the help of the information contained in the other variables), please use it for visualisation in this exercise.

Created on Thu Dec  16 
"""
from matplotlib import pyplot as plt
#from matplotlib import mlab as mlab
import numpy as np
import csv
##importing and reading the csv file
with open("./archive/train.csv", mode = 'r') as in_file:
    reader = csv.reader(in_file)
    
    col_headers = []
    
    ##exctracting headers with next() method
    col_headers = next(reader)
   
    ##exctracting each row using comprehension - loop method also included
    rows = [row for row in reader ]
    # for row in reader:
    #     rows.append(row)
    
#converting the headers list into dictionary for reference
headers_ref ={n:col_headers[n-1] for n in range(0, len(col_headers)+1)}
    
#print(rows)
print(col_headers)
##function to get a single category (headers_ref column) as a list
## extract(a_dataset, column index)
def extract(data_set, index):
    column = []
    
    for row in data_set:
        value = row[index]
        column.append(value)
    return column

##generate frequency table as a dictionary
def freq_col(data_set):
    freq_table = {}
    for row in data_set:
        if row in freq_table:
            freq_table[row] +=1
        else:
           freq_table[row] = 1
    return freq_table
#########
#########GENDER  & MARITAL STATUS DATA
##extracting column to list
gender_list = extract(rows,2)
marr_status = extract(rows,7)
# print(gender_list)## debug output
# print(marr_status)## debug output
##freq table for gender and marital status
# gender_freq = freq_col(gender_list)
# marr_status_freq = freq_col(marr_status)
# print(gender_freq)## debug output
# print(marr_status_freq)## debug output


##List for customer marriage by gender
f_married = 0
f_single = 0
m_married = 0
m_single = 0
## frequencies for married/single F and M assuming 0=single, 1=married
counter = 0
for gender in range(0, len(gender_list)):
    if marr_status[counter] == '0' and gender_list[counter] == 'F':
        f_single+=1
    elif  marr_status[counter] == '1' and gender_list[counter] == 'F':
        f_married+=1
    elif marr_status[counter] == '0' and gender_list[counter] == 'M':
        m_single+=1
    elif  marr_status[counter] == '1' and gender_list[counter] == 'M':
        m_married+=1
    counter +=1
        
# print(f_married)
# print(f_single)
# print(m_married)
# print(m_single)

# ##set up plot data with matplotlib.subplot

# ## add labels
plt.title("Shopper's Marital Status By Gender")

# ## generate graph data
x_data_lable = ['F', 'M']
layer00 = [f_married, m_married]
layer01 = [f_single, m_single]
# plot stacked bargraph
plt.bar(x_data_lable, layer00, color='#FC0F3A')
plt.bar(x_data_lable, layer01, bottom=layer00, color='#1FC3AA')
# ## adding legend
plt.legend(["Married", "Single"])
# ## display graph
plt.show()



# #########OCCUPATION DATA
# occupation_list_str = extract(rows,4)
# #converting string list to int list via comprehension

# occupation_list_int = [int(val) for val in occupation_list_str]
# print(occupation_list_int[7756])
# #sorting string
# # occupation_list_int.sort()
# # #creating frequency hast table/dict for occupation types
# # occupation_list_int_freq = freq_col(occupation_list_int)
# # #print(occupation_list_int) ## debug output
# # # print(occupation_list_int_freq ) ## debug output
# # # print(occupation_list_int_freq.keys()) ## debug output

# #########CLOTHS DATA
# cloths_list_str = extract(rows,8)
# #print(cloths_list_str) ##debug out
# #converting string list to int list via comprehension
# cloths_list_int = [int(val) for val in cloths_list_str]
# #print(cloths_list_int) ##debug out
# # print(max(cloths_list_int), min(cloths_list_int))
# #converting string list to int list via comprehension for 

# # for cloth in cloths_list_int:
    
    
# # cloths_list_0 = [cloths_list_int_0+=1 for val in cloths_list_int if occupation_list_int_freq.keys() == '0']

# # # #sorting string
# # # cloths_list_int_0.sort()
# # # print(cloths_list_int_0)
# # # print(cloths_list_int_m)
# # # print(cloths_list_int_f)
# # ##evaluating frequency (quantity) of each item purchase by gender
# # # ###########m_cloths_purch = freq_col(cloths_list_int_m)
# job_cloths = {0: [], 1:[], 2:[], 3:[0], 4:[]}###, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
# cloths_list_by_job_0 =[]
# cloths_list_by_job_1 =[]
# cloths_list_by_job_2 =[]
# cloths_list_by_job_3 =[]
# cloths_list_by_job_4 =[]
# cloths_list_by_job_5 =[]
# cloths_list_by_job_6 =[]
# cloths_list_by_job_7 =[]
# cloths_list_by_job_8 =[]
# cloths_list_by_job_9 =[]
# cloths_list_by_job_10 =[]
# cloths_list_by_job_11 =[]
# cloths_list_by_job_12 =[]
# cloths_list_by_job_13 =[]
# cloths_list_by_job_14 =[]
# cloths_list_by_job_15 =[]
# cloths_list_by_job_16 =[]
# cloths_list_by_job_17 =[]
# cloths_list_by_job_18 =[]
# cloths_list_by_job_19 =[]
# cloths_list_by_job_20 =[]

# counter = 0
# for cloth in cloths_list_int:
#     if occupation_list_int[counter] == 0:
#         cloths_list_by_job_0.append(cloth)
#     if occupation_list_int[counter] == 1:
#         cloths_list_by_job_1.append(cloth)
#     if occupation_list_int[counter] == 2:
#         cloths_list_by_job_2.append(cloth)
#     if occupation_list_int[counter] == 3:
#         cloths_list_by_job_3.append(cloth)
#     if occupation_list_int[counter] == 4:
#         cloths_list_by_job_4.append(cloth)
#     if occupation_list_int[counter] == 5:
#         cloths_list_by_job_5.append(cloth)
#     if occupation_list_int[counter] == 6:
#         cloths_list_by_job_6.append(cloth)
#     if occupation_list_int[counter] == 7:
#         cloths_list_by_job_7.append(cloth)
#     if occupation_list_int[counter] == 8:
#         cloths_list_by_job_8.append(cloth)
#     if occupation_list_int[counter] == 9:
#         cloths_list_by_job_9.append(cloth)
#     if occupation_list_int[counter] == 10:
#         cloths_list_by_job_10.append(cloth)
#     if occupation_list_int[counter] == 11:
#         cloths_list_by_job_11.append(cloth)
#     if occupation_list_int[counter] == 12:
#         cloths_list_by_job_12.append(cloth)
#     if occupation_list_int[counter] == 13:
#         cloths_list_by_job_13.append(cloth)
#     if occupation_list_int[counter] == 14:
#         cloths_list_by_job_14.append(cloth)
#     if occupation_list_int[counter] == 15:
#         cloths_list_by_job_15.append(cloth)
#     if occupation_list_int[counter] == 16:
#         cloths_list_by_job_16.append(cloth)
#     if occupation_list_int[counter] == 17:
#         cloths_list_by_job_17.append(cloth)
#     if occupation_list_int[counter] == 18:
#         cloths_list_by_job_18.append(cloth)
#     if occupation_list_int[counter] == 19:
#         cloths_list_by_job_19.append(cloth)
#     if occupation_list_int[counter] == 20:
#         cloths_list_by_job_20.append(cloth)
        
#     counter += 1

# # print(cloths_list_by_job_10)
# # print(cloths_list_by_job_19)
# # print(len(cloths_list_by_job_10))
# # print(len(cloths_list_by_job_19))

# cloths_list_by_job_0.sort()
# job_0_line = freq_col(cloths_list_by_job_0)
# cloths_list_by_job_1.sort()
# job_1_line = freq_col(cloths_list_by_job_1)
# cloths_list_by_job_2.sort()
# job_2_line = freq_col(cloths_list_by_job_2)
# cloths_list_by_job_3.sort()
# job_3_line = freq_col(cloths_list_by_job_3)
# cloths_list_by_job_4.sort()
# job_4_line = freq_col(cloths_list_by_job_4)
# cloths_list_by_job_5.sort()
# job_5_line = freq_col(cloths_list_by_job_5)
# cloths_list_by_job_6.sort()
# job_6_line = freq_col(cloths_list_by_job_6)
# cloths_list_by_job_7.sort()
# job_7_line = freq_col(cloths_list_by_job_7)
# cloths_list_by_job_8.sort()
# job_8_line = freq_col(cloths_list_by_job_8)
# cloths_list_by_job_9.sort()
# job_9_line = freq_col(cloths_list_by_job_9)
# cloths_list_by_job_10.sort()
# job_10_line = freq_col(cloths_list_by_job_10)
# cloths_list_by_job_11.sort()
# job_11_line = freq_col(cloths_list_by_job_11)
# cloths_list_by_job_12.sort()
# job_12_line = freq_col(cloths_list_by_job_12)
# cloths_list_by_job_13.sort()
# job_13_line = freq_col(cloths_list_by_job_13)
# cloths_list_by_job_14.sort()
# job_14_line = freq_col(cloths_list_by_job_14)
# cloths_list_by_job_15.sort()
# job_15_line = freq_col(cloths_list_by_job_15)
# cloths_list_by_job_16.sort()
# job_16_line = freq_col(cloths_list_by_job_16)
# cloths_list_by_job_17.sort()
# job_17_line = freq_col(cloths_list_by_job_17)

# print(job_0_line)
# print(job_10_line)

# ########LINE PLOT########
# ##set up plot data with matplotlib.subplot
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# plt.margins(x=0.0)
# ## add labels
# plt.title("Clothing Items Purchase by Occupation")
# plt.xlabel("Clothing Item")
# plt.ylabel("Tot Purchase")

# # setting ticks for x-axis
# ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# ## generate graph data
# #plt.hist(histo_list, bins, align='left', color=colors, edgecolor='pink')
# plt.plot(job_0_line.keys(), job_0_line.values(), label="Job  0")
# plt.plot(job_4_line.keys(), job_4_line.values(), label="Job  4")
# plt.plot(job_8_line.keys(), job_8_line.values(), label="Job  8")
# plt.plot(job_12_line.keys(), job_12_line.values(), label="Job 12")
# plt.plot(job_16_line.keys(), job_16_line.values(), label="Job 16")
# ## adding legend
# leg = ax.legend();
# ## display graph
# plt.show()



# ########STACKED BARGRAPH########
# ## preparing data to analyze
# gender = extract(rows, 7) ## list of genders
# gender_freq = freq_col(gender) ##freq table for genders
# #print(gender_freq) ##debug out
# ###########
# cloths_list_str = extract(rows,8)
# #print(cloths_list_str) ##debug out
# #converting string list to int list via comprehension
# cloths_list_int = [int(val) for val in cloths_list_str]
# #print(cloths_list_int) ##debug out
# print(max(cloths_list_int), min(cloths_list_int))
# #converting string list to int list via comprehension for M and F
# cloths_list_int_m = [int(val) for val in cloths_list_int if gender[int(val)] == '0']
# cloths_list_int_f = [int(val) for val in cloths_list_int if gender[int(val)] == '1']
# # #sorting string
# cloths_list_int_m.sort()
# cloths_list_int_f.sort()
# # print(cloths_list_int_m)
# # print(cloths_list_int_f)
# ##evaluating frequency (quantity) of each item purchase by gender
# m_cloths_purch = freq_col(cloths_list_int_m)
# f_cloths_purch = freq_col(cloths_list_int_f)
# print(m_cloths_purch)
# print(f_cloths_purch)
# # #########




##set up plot data

## add labels

## generate graph data

## display graph

########HISTOGRAM########
# ##preparing data for histogram
# histo_list = extract(rows,3)
# histo_list.sort()
# ##~~TRY ALTERNATE COLOR~~
# colors = ["#1167B1"]
# bins = 6
# ##set up plot data with matplotlib.subplot
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# plt.margins(x=0.0)
# ## add labels
# plt.title("Age vs Buys")
# plt.xlabel("Age Group")
# plt.ylabel("Purchases")

# ## generate graph data
# plt.hist(histo_list, bins, align='left', color=colors, edgecolor='pink')
# ## display graph
# plt.show()

# ########PIE CHART########
# # ##preparing data for pie chart
# pie_dicto = freq_col(extract(rows,5))
# ##print(pie_dicto) ## debug output
# ## prepare labels
# labels = pie_dicto.keys()
# pie_data = pie_dicto.values()
# colors = ['lightblue', 'lightgreen', 'yellow']

# ## add labels
# plt.title('Purchases by City Type', fontdict={'fontsize': 16}, pad=11)

# ## generate graph data
# patches, texts, autotexts = plt.pie(pie_data,  labels=labels,  autopct='%1.1f%%', 
#         colors=colors, radius = 1.3,
#         wedgeprops={"linewidth": 1, "edgecolor": "black"}, 
#         textprops={'fontsize': 14}, #label size
#         shadow=True, startangle=90)
# ## Inner label style
# plt.setp(autotexts, **{ 'weight':'bold', 'fontsize':13})
# ## and display graph
# plt.show()


# # ########SCATTERPLOT########
# occupation_list_str = extract(rows,4)
# #converting string list to int list via comprehension
# occupation_list_int = [int(val) for val in occupation_list_str]
# #sorting string
# occupation_list_int.sort()
# #creating frequency hast table/dict for occupation types
# occupation_list_int_freq = freq_col(occupation_list_int)
# #print(occupation_list_int ) ## debug output
# # print(occupation_list_int_freq ) ## debug output
# # print(occupation_list_int_freq.keys()) ## debug output
# #extract purchases amounts
# purchase_list = extract(rows,11)
# #print(purchase_list) ## debug output

# #### GROUPING TOTAL PURCHASES BY PROFESSION
# #### THERE MUST BE A BETTER WAY
# tot0, tot1, tot2, tot3, tot4, tot5, tot6, tot7, tot8, tot9, tot10 = 0,0,0,0,0,0,0,0,0,0,0
# tot11, tot12, tot13, tot14, tot15, tot16, tot17, tot18, tot19, tot20 = 0,0,0,0,0,0,0,0,0,0

# for profession in occupation_list_int:
#     if profession == 0:
#         tot0 += int(purchase_list[profession])
#     if profession == 1:
#         tot1 += int(purchase_list[profession])
#     if profession == 2:
#         tot2 += int(purchase_list[profession])
#     if profession == 3:
#         tot3 += int(purchase_list[profession])
#     if profession == 4:
#         tot4 += int(purchase_list[profession])
#     if profession == 5:
#         tot5 += int(purchase_list[profession])
#     if profession == 6:
#         tot6 += int(purchase_list[profession])
#     if profession == 7:
#         tot7 += int(purchase_list[profession])
#     if profession == 8:
#         tot8 += int(purchase_list[profession])
#     if profession == 9:
#         tot9 += int(purchase_list[profession])
#     if profession == 10:
#         tot10 += int(purchase_list[profession])
#     if profession == 11:
#         tot11 += int(purchase_list[profession])
#     if profession == 12:
#         tot12 += int(purchase_list[profession])
#     if profession == 13:
#         tot13 += int(purchase_list[profession])
#     if profession == 14:
#         tot14 += int(purchase_list[profession])
#     if profession == 15:
#         tot15 += int(purchase_list[profession])
#     if profession == 16:
#         tot16 += int(purchase_list[profession])
#     if profession == 17:
#         tot17 += int(purchase_list[profession])
#     if profession == 18:
#         tot18 += int(purchase_list[profession])
#     if profession == 19:
#         tot19 += int(purchase_list[profession])
#     if profession == 20:
#         tot20 += int(purchase_list[profession])
# purchase_tot_by_prof = [tot0, tot1, tot2, tot3, tot4, tot5, tot6, tot7, tot8, tot9, tot10,
#                         tot11, tot12, tot13, tot14, tot15, tot16, tot17, tot18, tot19, tot20]

# #print(purchase_tot_by_prof) # debug output
    
# purchase_max = max(purchase_tot_by_prof)
# purchase_min = min(purchase_tot_by_prof)
# #print(purchase_min, purchase_max) # debug output

# ##set up data for scatterplot
# s = list(map(lambda x: x/2500000, purchase_tot_by_prof))
# n = len(occupation_list_int_freq.keys())
# colors = np.random.uniform(15, 80, n)

# # set up plot
# fig, ax = plt.subplots()
# ## add labels
# plt.title("Purchases by Occupation")
# plt.xlabel("Job Category")
# ## Need to fix ticks - NO FLOAT
# #plt.xticks( range(22), purchase_tot_by_prof )
# plt.ylabel("Purchases in Hundres Milion")

# ax.scatter(occupation_list_int_freq.keys(), purchase_tot_by_prof, 
#             s=s, c=colors)
# # ## and display graph
# plt.show()



########################################
########################################
########################################
########################################
########BOX PLOT########
##plt.style.use('_mpl-gallery')

##preparing data for pie chart

# cloths_list = freq_col(extract(rows,8))
# # ele_list = extract(rows,9)
# # house_list = extract(rows,10)
# # print(cloths_list) ## debug output
# # print(ele_list) ## debug output
# # print(house_list) ## debug output

# #box_data = (cloths_list, ele_list, house_list)
# fig, ax = plt.subplots()

# # # Creating boxplotplot
# # plt.boxplot(cloths_list)
 
# # # show plot
# # plt.show()


# VP = ax.boxplot(cloths_list, positions=[2, 4, 6], widths=1.5, patch_artist=True,
#                 showmeans=False, showfliers=False,
#                 medianprops={"color": "white", "linewidth": 0.5},
#                 boxprops={"facecolor": "C0", "edgecolor": "white",
#                           "linewidth": 0.5},
#                 whiskerprops={"color": "C0", "linewidth": 1.5},
#                 capprops={"color": "C0", "linewidth": 1.5})

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#         ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

# """
# # # add a 'best fit' line SD taken from source
# # y = mlab.normpdf(bins, histo_list, sigma)

# # def find_sum(a_list):
# #     a_sum = 0
# #     for element in a_list:
# #         a_sum += float(element)
# #     return a_sum

# # def find_length(a_list):
# #     length = 0
# #     for element in a_list:
# #         length += 1
# #     return length

# # def mean(data_set, index):
# #     column = extract(data_set, index)
# #     return find_sum(column) / find_length(column)


# ####ALTERNATIVELY, some or all graph could be be plot togethere using 
# """