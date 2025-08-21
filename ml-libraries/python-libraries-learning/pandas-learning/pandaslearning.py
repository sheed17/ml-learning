import pandas as pd

#series, dataframes
#Math operations with dataframes
#Functions, creating columns, and filling the rows with data
#dropna, fillna, notna
#Iterrating over rows and columns
#Grouping (like grouping by job and based on their job i get their age and then aggregate functions)
#Concatenating, merging, and joining


"""
Series

values = [10, 20, 30, 40, 50]
s = pd.Series(values, index=['a', 'b', 'c', 'd', 'e'])
print(s)

"""

"""
Pd terms that i will be using often for grouping, filtering
df = pd.DataFrame({
    'name' : ['Rasheed', 'Bob', 'Sam'],
    'job': ['Programmer', 'Basketball Player', 'Barista'],
    'age': [21, 24, 36]
})

df = df.set_index('name')
#print(df.iloc[0])
#print(df.iloc[1, 1])
#print(df.at['Rasheed', 'age'])
df.loc['Tim'] = ['Mechanic', 32]
df.loc['Johnny'] = {'job':'Engineer', 'age': 24}
print(df)
print(df.loc['Johnny'])
print(df.at['Rasheed', 'job'])
#print(df.loc['Rasheed'])

"""


""" Math operations with dataframes
df1 = pd.DataFrame({
    'a': [1,2,3]

}, index=[2,1,0])

df2 = pd.DataFrame({
    'a':[3,4,2]
}, index=[0,1,2])

print(df1 + df2)
"""





#manipulating with functions



"""
Functions, creating columns, and filling the rows with data

df = pd.DataFrame({
    'name' : ['Rasheed', 'Bob', 'Sam'],
    'job': ['Programmer', 'Basketball Player', 'Barista'],
    'age': [20, 24, 36]
})

df = df.set_index('name')

def myfunction(x):
    if x % 3 == 0:
        return x
    else:
        return "not divisible by 3"
    
df['age'] = df['age'].apply(myfunction)
print(df['age'])

#adding a column
df['Married'] = df.apply(lambda row: None, axis=1)
df['Married'] = df['Married'].fillna("Unknown")

married_map = {'Rasheed': 'No', 'Bob': 'No', 'Sam': 'Yes'}
df['Married'] = df.index.map(married_map)
print(df)


"""

"""Dropping, filling and notna
dropna, fillna, notna

df = pd.DataFrame({
    'name' : ['Rasheed', 'Bob', 'Sam'],
    'job': ['Programmer', 'Basketball Player', 'Barista'],
    'age': [20, 24, 36]
})

df = df.set_index('name')

df.loc['John'] = ['Butcher', float('nan')]

#df = df.dropna()
df['age'] = df['age'].fillna(df['age'].mean())
print(df)
print(df.notna())
"""


""" 
Iterrating over rows and columns
df = pd.DataFrame({
    'name' : ['Rasheed', 'Bob', 'Sam'],
    'job': ['Programmer', 'Basketball Player', 'Barista'],
    'age': [20, 24, 36]
})
df = df.set_index('name')

for i, rows in df.iterrows():
    print(i)

for i, columns in df.items():
    print(i)

    
"""


"""
Grouping

df = pd.DataFrame({
    'name' : ['Rasheed', 'Bob', 'Sam'],
    'job': ['Programmer', 'Basketball Player', 'Barista'],
    'age': [20, 24, 36]
})

dfGrouping = df.groupby('job').agg({
    'age': ['mean', 'min', 'max']
})

print(dfGrouping)
descending = df.sort_values('age', ascending=False)
print(descending)

"""




"""
Concatenating, merging, and joining

df1 = pd.DataFrame({
    'Item': ['A', 'B', 'C'],
    'Price': [10, 20, 30]
})

df2 = pd.DataFrame({
    'Item': ['D', 'E', 'F'],
    'Price': [40, 50, 60]
})

result = pd.concat([df1, df2])
result = result.reset_index()
result = result.drop('index', axis=1)
print(result)

df3 = pd.DataFrame({
    'Item': ['B', 'C', 'D'],
    'Country': ['USA', 'Columbia', 'Brazil']
})

result = pd.merge(df1, df3, how="left")
print(result)

#Same goes if i were to add new rows and columns such as addinng country and its group or whatever you just concat


df4 = pd.DataFrame({
    'Price': [10, 20, 30]
}, index= ['A', 'B', 'C'])

df5 = pd.DataFrame({
    'Country': ['USA', 'Brazil', 'Jamaica']
}, index=['B', 'C', 'D'])

result = df5.join(df4, how='outer')
print(result)


# rule of thumb merge if there is a match on column, join if there is a match on index, and concat to pretty much add new data to whatever it is that you want to add

"""
print("Done")













