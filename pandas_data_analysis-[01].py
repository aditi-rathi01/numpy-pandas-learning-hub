#   ===== Data Frame =====

# Data Frame is an object that is useful in representing data in the form of rows and columns.


# -------- Creating Data Frame from an Excel spreadsheet ----------

import pandas as pd

data = {
    "empid": [1001,1002,1003,1004,1005,1006],
    "ename": ["Ganesh rao", "Anil kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna","Anant Nag"],
    "sal" :[10000, 23000.5, 18000.33, 16500.5, 12000.75, 9999.99],
    "dob" :["10-10-2000", "3-20-2002", "9-10-2000", "3-3-2002","10-8-2000", "9-9-1999"]
}

df = pd.DataFrame(data)
df.to_excel("sample_pandas-excel.xlsx", index= False)      # An excel sheet that contain data same as df will be saved.
print(df)

import os
print(os.getcwd())                 # To get the location where excel sheet is saved.


# ------- Creating Data Frame from .csv Files -------

import pandas as pd
data = {
     "empid": [1001,1002,1003,1004,1005,1006],
    "ename": ["Ganesh rao", "Anil kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna","Anant Nag"],
    "sal" :[10000, 23000.5, 18000.33, 16500.5, 12000.75, 9999.99],
    "dob" :["10-10-2000", "3-20-2002", "9-10-2000", "3-3-2002","10-8-2000", "9-9-1999"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index= False)


# ------ Creating DataFrame from a Python list of Tuples -------

empdata = [(1001, "Ganesh rao", 10000.00, "10-10-2000"),
           (1002, "Anil kumar", 23000.5, "03-20-2002"),
           (1003, "Gaurav Gupta", 18000.33, "9-10-2000"),
           (1004, "Hema Gupta", 16500.5, "3-3-2002"),
           (1005, "Laxmi prasanna", 12000.75, "10-8-2000"),
           (1006, "Anant Nag",9999.99,"09-09-1999")]

df = pd.DataFrame(empdata, columns= ["id_no.", "emp_name","emp_salary","emp_dob"])
print(df)


# ------ Viewing Data frame using loc() and iloc()------

# loc is a function(locate) useful to view rows and columns based on column label(or names).
# iloc is a fuction useful to view data based on integer index.

df1 = df.loc[:,["emp_name","emp_dob"]]
print(df1)

# To view only 0 to 3rd rows of "name" and "dob ". columns.
df2 = df.loc[:3,["emp_name","emp_dob"]]     
print(df2)                                    # Print, Column zero to Three(that is 0,1,2 and 3)

# Now, the same thing done by iloc() method.
df3 = df.iloc[:3,[1,3]]
print(df3)


# Note : Observe that the silicing opreation iloc[0:3] gives 0th to 2nd row only.
# And, In case of loc[0:3] opreations gives 0th to 3rd row.

print(df.loc[:3,:])
print(df.iloc[:3,:])


# To view, 3rd row to 0th row with all columns, we can use loc() as:
df4 = df.loc[3:0:-1, :]
print(df4)

# Same thing can be done through iloc() function:

df5 = df.iloc[3:0:-1, :]
print(df5)

# suppose, we want to display only last row, we can use iloc() with -1. Not possible with loc() function.
df6 = df.iloc[-1]
print(df6)


# We can use loc() to display the last column label as:
df7 = df.loc[:, "emp_name"]
print(df7)

# The same thing can be done using iloc() function.
df8 = df.iloc[:,-1]
print(df8)


# ====== Opreations on DataFrame ========

# These opreations helps to analyize the data or manipulation the data.

# As, we created a DataFrame previosly called sample_data. so, read that file.

df9 = pd.read_csv("sample_data.csv")
print(df9)


# // // Knowing, Number of rows and columns.
print(df9.shape)

# Suppose, We want to to retrieve only rows or columns, we can read number as:

r,c = df9.shape
print(r)
print(c)

# Retrieving a Range of Rows

# The method head() gives the first five rows and the method tail() returns the last five rows.
print(df.head())
print(df.tail())

# To display first 3 rows, we can use head() method by passing 3 to it as:
print(df9.head(3))
print(df9.head(4))
print(df9.tail(2))

# // // Retrive a Range of Rows.

# We can treat DataFrame as an object and retrieve the rows from it using slicing method.
print(df9[2:5])
print(df9[0::2])
print(df9[5:0:-1])          # Here, silicing return index no. upto '1'.


# // // To Retrieve Column names from the Data Frame.

# To retrieve column names from the Data Frame, we can use columns attribute as:
print(df9.columns)

# To Retrive column Data Frame.
print(df["emp_name"])

# To, Retrieving Data from Multiple columns.

print(df9[['ename','sal']])

# // // Finding Maximum and Minimum Values.

# It is possible to find maximum and minimum using max() and min() function respectively.

print(df9["sal"].max())
print(df9["sal"].min())


# // // Display statistical Infomation.

# We have describe() method that display very important information like number of values, average, standard deviation.

print(df9.describe())


# // // Perfoming Queries on Data.

# we can retrieve rows based on a query.
print(df9[df9.sal>10000])

# To, retrive the row where salary is maximum, we can write:
print(df9[df9.sal == df9.sal.max()])

# Suppose, we want to show emp_id, emp_sal, emp_name which have less than salary of 17000.
print(df9[df9.sal < 17000])

# // // Setting a Column as Index.

# As we know that index column is automatically generated. If a we don't want that column and we want to set a column
# from our data as index columnm, that is possible using set_index().

df9 = df9.set_index("empid")
print(df9)


# Note:-
# df9.set_index("empid", inplace= True)                       Here, output gives the error. No "empid" column exist.
                                                # Because, "empid" is removed from column. It becomes an index now.

# Once emp_id is used as index number, It is possible to display data of employee by passing empolyee id number to loc attribute.

print(df9.loc[1003])

# // // Resetting the Index

# To reset the index value from "empid " to original auto - genereated index number, we can use reset_index() method.
df9 = df9.reset_index()
print(df9)

# // // Sorting the data.

df9 = df9.sort_values("dob")
df9 = df9.sort_values("sal")
df9 = df9.sort_values("ename")
print(df9)