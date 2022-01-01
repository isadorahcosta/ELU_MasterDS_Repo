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


# ########SCATTERPLOT########
occupation_list_str = extract(rows,4)
#converting string list to int list via comprehension
occupation_list_int = [int(val) for val in occupation_list_str]
#sorting string
occupation_list_int.sort()
#creating frequency hast table/dict for occupation types
occupation_list_int_freq = freq_col(occupation_list_int)
#print(occupation_list_int ) ## debug output
# print(occupation_list_int_freq ) ## debug output
# print(occupation_list_int_freq.keys()) ## debug output
#extract purchases amounts
purchase_list = extract(rows,11)
#print(purchase_list) ## debug output

#### GROUPING TOTAL PURCHASES BY PROFESSION
#### THERE MUST BE A BETTER WAY
tot0, tot1, tot2, tot3, tot4, tot5, tot6, tot7, tot8, tot9, tot10 = 0,0,0,0,0,0,0,0,0,0,0
tot11, tot12, tot13, tot14, tot15, tot16, tot17, tot18, tot19, tot20 = 0,0,0,0,0,0,0,0,0,0

for profession in occupation_list_int:
    if profession == 0:
        tot0 += int(purchase_list[profession])
    if profession == 1:
        tot1 += int(purchase_list[profession])
    if profession == 2:
        tot2 += int(purchase_list[profession])
    if profession == 3:
        tot3 += int(purchase_list[profession])
    if profession == 4:
        tot4 += int(purchase_list[profession])
    if profession == 5:
        tot5 += int(purchase_list[profession])
    if profession == 6:
        tot6 += int(purchase_list[profession])
    if profession == 7:
        tot7 += int(purchase_list[profession])
    if profession == 8:
        tot8 += int(purchase_list[profession])
    if profession == 9:
        tot9 += int(purchase_list[profession])
    if profession == 10:
        tot10 += int(purchase_list[profession])
    if profession == 11:
        tot11 += int(purchase_list[profession])
    if profession == 12:
        tot12 += int(purchase_list[profession])
    if profession == 13:
        tot13 += int(purchase_list[profession])
    if profession == 14:
        tot14 += int(purchase_list[profession])
    if profession == 15:
        tot15 += int(purchase_list[profession])
    if profession == 16:
        tot16 += int(purchase_list[profession])
    if profession == 17:
        tot17 += int(purchase_list[profession])
    if profession == 18:
        tot18 += int(purchase_list[profession])
    if profession == 19:
        tot19 += int(purchase_list[profession])
    if profession == 20:
        tot20 += int(purchase_list[profession])
purchase_tot_by_prof = [tot0, tot1, tot2, tot3, tot4, tot5, tot6, tot7, tot8, tot9, tot10,
                        tot11, tot12, tot13, tot14, tot15, tot16, tot17, tot18, tot19, tot20]

#print(purchase_tot_by_prof) # debug output
    
purchase_max = max(purchase_tot_by_prof)
purchase_min = min(purchase_tot_by_prof)
#print(purchase_min, purchase_max) # debug output

n = len(occupation_list_int_freq.keys())
# print(n)
# # size and color:

area = np.pi * (15 * np.random.rand(n))**2  # 0 to 15 point radii
colors = np.random.uniform(15, 80, n)

# plot
fig, ax = plt.subplots()

# ax.set(xlim=(0, 21), xticks=np.arange(0, 21),
#         ylim=(0, 8), yticks=np.arange(purchase_min, purchase_max))

ax.scatter(occupation_list_int_freq.keys(), purchase_tot_by_prof, 
           s=area, c=colors)

plt.show()
sss





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

"""
# # add a 'best fit' line SD taken from source
# y = mlab.normpdf(bins, histo_list, sigma)

# def find_sum(a_list):
#     a_sum = 0
#     for element in a_list:
#         a_sum += float(element)
#     return a_sum

# def find_length(a_list):
#     length = 0
#     for element in a_list:
#         length += 1
#     return length

# def mean(data_set, index):
#     column = extract(data_set, index)
#     return find_sum(column) / find_length(column)


####ALTERNATIVELY, some or all graph could be be plot togethere using 
"""