
# ===== Handling Missing Data ======


# In many case, the data we recieve from various source may be not be perfect. that means there is some missing data.

import pandas as pd
import numpy as np

empdata = {
    "empid": [1001, 1002, 1003, 1004, 1005, 1006 ],
    "Name": ["Ganesh rao", "Anil Kumar", np.nan , "Hema Chandra", "Laxmi Prasaana","Anant Nag"],
    "sal" :[ 10000, 230000.5, 18000.33, np.nan, 12000.75, 9999.99],
    "dob" : ["10-10-00","03-03-02", "03-03-02", np.nan, "10-08-00", "09-09-99"]
} 

df = pd.DataFrame(empdata)                         # (NAN:- Not a Number)
print(df)

df.to_excel("emp_data.xlsx", index= False)


# We can use fillna() method to replace the Na or NaN values by specified value.

df1 = df.fillna(0)
print(df1)

# Better, Option to this filling 0 is we can fill each coloumn with a different value by passing the columns name
# and the values to be used to fill in the column.

df2 = df.fillna({"Name": "Missing Name", "sal": 0.0, "dob": "00-00-00"})
print(df2)


# If we do not want the missing data and want to remove those rows having NaN or Na Values, then we can use dropna() method as:

df3 = df.dropna()
print(df3)


# ====== Series Object =======

# A series Object indicates only 1 column. When there are more than 1 coulmns, it becomes a table and hence it can be treated 
# as DataFrame. 


empdata = {
    "empid": [1001, 1002, 1003, 1004, 1005, 1006 ],
    "Name": ["Ganesh rao", "Anil Kumar", np.nan , "Hema Chandra", "Laxmi Prasaana","Anant Nag"],
    "sal" :[ 10000, 230000.5, 18000.33, np.nan, 12000.75, 9999.99],
    "dob" : ["10-10-00","03-03-02", "03-03-02", np.nan, "10-08-00", "09-09-99"]
} 

df = pd.DataFrame(empdata)                         
print(df)

ser = pd.Series(df["Name"])
print(ser)

ser1 = pd.DataFrame(df["sal"])
print(ser1)

# // // Creating DataFrame from series.

df4 = pd.concat([ser, ser1], axis= 1)
print(df4)


# // //  Creating series from NumPy Array

from numpy import *
arr = array([10,20,30,40,50])
ser2 = pd.Series(arr)
print(ser2)

# // // Converting Series into Numpy Array

a = ser2.values
print(a)

# // // Create Series from Dictionary

my_dict = {
    "name": ["a","b","c","d","e"],
    "age": [10,20,30,40,50],
    "Dedignation": ["CEO", "VP","SVP","AM","DEV"]
}

ser3 = pd.Series(my_dict)
print(ser3)

# // // Accessing Elements of a Series.

names = ser3["name"]
print(names)

names1 = ser3["name"][2]
print(names1)