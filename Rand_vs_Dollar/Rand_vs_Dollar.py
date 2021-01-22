
# ___________________________Rand vs USD CSV Speadsheet_______________________
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#col_types = [str, float, str, str, float, int]

#RnD_df = pd.read_excel("./Rand vs. US Dollar.xlsx")
#print(RnD_df.head())
#current_date = RnD_df["Date"] 
#print(current_date)
#current_xchange = RnD_df["Ratio"] 
#print(current_xchange)

with open("./Rand vs. US Dollar.xlsx") as f:
    f_csv = csv.reader(f, delimiter=",")
    print(f_csv)
    for rows in f_csv:
        rows = tuple(f_csv[0:])
        print(rows)

