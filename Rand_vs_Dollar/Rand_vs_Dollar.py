
# ___________________________Rand vs USD CSV Speadsheet_______________________
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import namedtuple
import math
from decimal import *

#col_types = [str, float, str, str, float, int]

#RnD_df = pd.read_excel("./Rand vs. US Dollar.xlsx")
#print(RnD_df.head())
#current_date = RnD_df["Date"] 
#print(current_date)
#current_xchange = RnD_df["Ratio"] 
#print(current_xchange)

def get_vals():
    with open("./Rand vs. US Dollar.csv") as f:
        f_csv = csv.reader(f, delimiter="\t")
        headings = next(f_csv)
        columns = next(f_csv)
        # values = next(f_csv)
        # values = []
        values = next_value(f_csv)
        Curr_Exch = []
        inc_values = 0
        values = next_value(f_csv)
        for element in values:
            num_of_elem = len(element)                      # 47 elements
            for i in range(0, 100):
                values = next_value(f_csv)
                current_exchange = Curr_Exch.insert(i, element[35:43])
                inc_values += i                             # Row 1 of Values
                if inc_values == 100:
                    inc_values = 0
                    break
            print(element)
            print(Curr_Exch)
            print(inc_values)

def next_value(f_csv):
    values = next(f_csv)
    return values

vals = get_vals()










    #Row = namedtuple('Row', headings)
    #for r in f_csv:
    #    row = Row(*r)
    #    print(row)

    #for row in f_csv:
    #    print(row)
  #      print(column)
        # Date = row[:1]
        # print(Date)
        # for line in row:
        #    print(line)

