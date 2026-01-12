# ===== ADVANCED PANDAS =====

# ------- Joining the DataFrames. ---------

# when we have data spread in various data Frames, we can combine that data into one data frame that can provide overall
# view of data.

import pandas as pd

data1 = {
    "Player Name": ["Rahul Dravid", "Virat Khole", "Vinod Kamble"],
    "Age": [30,24,22]
}
df1 = pd.DataFrame(data1)
print(df1)

data2 = {
    "Player Name": ["Rahul Dravid","Virat Khole", "Harbajan Shingh"],
    "Salary(in lakhs)" : [45,60,44]
}

df2 = pd.DataFrame(data2)
print(df2)


# There are four types of joins.

# 1.) // // Inner Join: This will gives intersection of rows of both DataFrames.

df3 = pd.merge(df1, df2, on= "Player Name", how= "inner")
print("Inner joining of two data frames")
print(df3)


# 2.) // // Left Join : Return all rows from left table + matching rows from right table.

df4 = pd.merge(df1, df2, on="Player Name", how = "left")
print("Left Joing of Two Dataframes:")
print(df4)


# 3.) // // Right Join : Return all rows from right table + matching rows from the left table.

df5 = pd.merge(df1,df2, on= "Player Name", how= "right")
print("Right Joing of two DataFrames:")
print(df5)

# 4.) // // Returns all rows from both tables.

df6 = pd.merge(df1, df2, on= "Player Name", how= "outer")
print(df6)


# // // How to Join when There is no common column..

data3 = {
    "Player_Name": ["Rahul Dravid", "Virat Kohli","Vinod Kamble"],
    "age": [30,24,22]
}
df7 = pd.DataFrame(data3)

data4 = {
    "Sports Person": ["Rahul Dravid","Virat Kohli","Harbajan singh"],
    "Sakary(in lakhs)":[45, 60,44]
}

df8 = pd.DataFrame(data4)

print("Merging of dataframe with no common name:")
df9 = pd.merge(df7, df8, left_on="Player_Name", right_on="Sports Person")
print(df9)


# Note: Remeber that, "inner joining" is a default join for merge() fuction. hence we don't mention how = "inner" attribiute.

df10 = pd.merge(df7,df8, left_on="Player_Name", right_on= "Sports Person", how= "left")
print("Left Merging of two dataframe:")
print(df10)


# Important Difference: 

# merge() in pandas: Used to combine Dataframe using common column(key).
# concation in pandas: No mathching column(key) needed.


# ----- Concatenation of Tables. ---------

# sometimes, we can attach the columns of two dataFrames side by side. This is called 'concatenation' or 'Union'.

print("Concatenation of two DataFrames:")
df11 = pd.concat([df7,df8])
print(df11)

# Note: Observe, that in the output of "df11" index are shown in the form like (0,1,2,0,1,2). we want to generate the index
# values properly as: 0,1,2,3,4,5. For this purpose we should ignore the existing index values and regenrate them using 
# ignore_index = True.

df12 = pd.concat([df7, df8 ],  ignore_index= True)
print(df12)

# we can also use axis = 1. attribute. To remove NaN from dataframe df12. 

df13 = pd.concat([df7,df8], axis= 1)
print(df13)

# ------ Where() Method -------

# where() is used to keep values where a condition is TRUE and replace the rest with NaN or another value.
#  if condition is true -->  Keep the value.
# if condition is false -->  replace it.

data5 = {
    "Name": ["Vinay","Anil","Gopal","Nani"],
    "Test1" : [15,45,60,76],
    "Test2" : [45,56,78,80],
    "Test3": [89,90,45,40]
}

df14 = pd.DataFrame(data5)
print(df14)
df14.set_index("Name", inplace=True)
print(df14)

print(df14.where(df14<60, "First"))

print(df14)

# // // Lambda fuction

print(df14.where(lambda x: x<80, "Excellent"))

# Let's take another example. for example, even after addding 10 matks. if marks are still < 30, then we want to display 
# "poor" in the place of those marks. see the code:-

print(df14.where(lambda x: x + 10>= 30, "poor"))


# ------ Group Method -------

# groupby() Method is used to split data into groups based on one or  more column.

climate = [("delhi", 33, 8),
           ("delhi", 33,8),
           ("delhi", 38, 7),
           ("delhi", 35,10),
           ("Pune", 49,15),
           ("Pune", 44,11),
           ("Pune",48, 13),
           ("Pune", 45,12)]

df15 = pd.DataFrame(climate, columns= ["City","Temp","Wind"])
print(df15)

# Now, the data frame is ready. It conatins rows of two cities namely, "delhi","Pune". If we want to do opreation on just
# one, the we have to divide all those into two groups on the "city". this can be done by group("City").

df16 = df15.groupby("City")
for City, rows in df16:
    print(City)
    print(rows)



# From the above output, we can observe two groups under the names "Delhi", and "Pune". suppose, we want to do any opreation
# only one group, that can be retrieve only one group, that can be retrieved using get_group() method. 
# Let's retrieve only "Pune " group as:

df17 = df16.get_group("Pune")
print(df17)
print(df16.get_group("Pune").max())


