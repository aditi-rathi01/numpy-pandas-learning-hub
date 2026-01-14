import pandas as pd

data = [("Delhi", 35, 10),
        ("Delhi", 33, 8),
        ("Delhi", 38, 7),
        ("Delhi", 35,10),
        ("Pune", 49, 15),
        ("Pune", 50, 12),
        ("Pune", 44, 11),
        ("Pune", 48, 13)]

df = pd.DataFrame(data, columns=["City", "Temp", "Wind"])
print(df)

# ------ Aggregate Functions on Data Frames --------

# min(), max(), mean(), median(), sum(), prod(), mod(), std(), count() etc. are called aggregate fuctions since they works on 
# groups of rows. These fuctions can be applied on normal data frames with the help of agg() method. 

# For example, to find maximum tempreature and windspeed and count the  number of rows in dataframes, we can write :

print(df.agg(["max", "count"]))


# Suppose, we want to find the mininum and maximum temperature in the total data frames, we can write:

print("Lowest and Highest Temperature of city")
print(df["Temp"].agg(["max", "min"]))

# To find minimum and maximum values of tempreature along with mean and medians value of windspeed, we can pass a dictionary
# to agg() method as:

print("Min and Max tempreature along with mean and medium of windspeed.")
print(df.agg({"Temp": ["max","min"], "Wind": ["mean", "median"]}))

