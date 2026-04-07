import pandas as pd
#Create a DataFrame from a Dictionary
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#Series is a one-dimensional array that can hold any data type. It is similar to a column in a table.
a = [1, 7, 2]

myvar = pd.Series(a)

print(f"\n{myvar}")

#Lables in series

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(f"\n{myvar}")
print(f"\n{myvar['y']}")

#Key/Value Objects
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

#Data Frames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

#Locate Row
print(df.loc[0])

#Named Indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#Reading a CSV File

df = pd.read_csv('C:\\Learning\\Week-01(Python & OOP)\\Learning-Curve\\Week-1\\Day-4\\data.csv')

print(df.to_string()) 
#Checking the System's maximum number of rows to display
print(pd.options.display.max_rows) 

pd.options.display.max_rows = 9999

df = pd.read_csv('C:\\Learning\\Week-01(Python & OOP)\\Learning-Curve\\Week-1\\Day-4\\data.csv')

print(df) 

print(df.info()) 
#Dropping Missing Values
new_df = df.dropna()

print(new_df.to_string())

#Replacing Missing Values using the fillna() Method
df.fillna(130, inplace = True)

#Calculate the mean of the "Calories" column and replace missing values with the mean
x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)
#Calculate the MEDIAN, and replace any empty values with it:

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

#Calculate the MODE, and replace any empty values with it:

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

df.corr()