
# ___________________________Rand vs USD CSV Reader_______________________
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import namedtuple
import math
from decimal import *
from datetime import datetime
import import_json

#col_types = [str, float, str, str, float, int]

#RnD_df = pd.read_excel("./Rand vs. US Dollar.xlsx")
#print(RnD_df.head())
#current_date = RnD_df["Date"] 
#print(current_date)
#current_xchange = RnD_df["Ratio"] 
#print(current_xchange)

# 31032021

#def get_vals():
#    with open("./Rand vs. US Dollar.csv") as f:
#        f_csv = csv.reader(f, delimiter="\t")
#        headings = next(f_csv)
#        columns = next(f_csv)
#        values = []
#        # values = next_value(f_csv)
#        curr_exch = []
#        exch_date = []
#        inc_values = 0
#        values = next_value(f_csv)
#        for i in range(0, 100):
#            values = next_value(f_csv)
#            for element in values:
#                num_of_elem = len(element)                  # 47 elements
#                curr_exch.insert(i, element[35:43])
#                exch_date.insert(i, element[0:10])
#                inc_values += i                             # Row 1 of Values
#            if i == 28:
#                break
#            print(headings)
#            print(columns)
#            print(element)
#            print(curr_exch)
#            print(inc_values)
#            print(exch_date)
#        Plot(exch_date, curr_exch)

#def next_value(f_csv):
#    values = next(f_csv)
#    return values

#def Plot(x, y):
#    x_value = x
#    y_value = y
#    plt.plot(x_value, y_value)
#    plt.title("Rand Dollar Ratio")
#    plt.xlabel("Date")
#    plt.ylabel("Ratio")
#    plt.show()

#vals = get_vals()

curr_exch = []
exch_date = []

for i in range(0, 10):
    curr_exch.insert(i, import_json.RnD_Val)
    exch_date.insert(i, import_json.RnD_Date)
    #print(len(curr_exch))
    if curr_exch is not curr_exch:
        curr_exch.insert(i, import_json.RnD_Val)
        exch_date.insert(i, import_json.RnD_Date)
    else:
        break

    #if i == len(curr_exch):
    #    break
    
print(curr_exch)
print(exch_date)

