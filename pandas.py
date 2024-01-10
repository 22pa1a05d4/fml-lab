# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZ85Mnzpae5P3mNVegy_9XdpcEEDw4vO
"""

import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3,4])
print(s1)

fruits = np.array(['apple','orange','mango','pear'])
series2 = pd.Series(fruits)
print(series2)

df1 = pd.DataFrame({
    "C1": [1, 4, 8, 7, 9],
    "C2": ['a', 'column', 'with', 'a', 'string'],
    "C3": [1.23, 23.5, 45.6, 32.1234, 89.453],
    "C4": [True, False, True, False, True]
})

print(df1)

mylist = [4, 8, 12, 16, 20]
df2 = pd.DataFrame(mylist)
print(df2)

items = [['Phone', 2000], ['TV', 1500], ['Radio', 800]]
df3 = pd.DataFrame(items)
print(df3)

items = [['Phone', 2000], ['TV', 1500], ['Radio', 800]]
df4 = pd.DataFrame(items, columns=['Item', 'Price'], dtype=float)
print(df4)

df4.describe()

"""# importing data"""

data = pd.read_csv('/content/sample_data/mnist_test.csv')
print(data)

data.head()

data.tail()

data.head(3)

data['7']

data=pd.read_csv('/content/sample_data/mnist_train_small.csv')
print(data)

"""# Data Wrangling"""

d1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'student_name': ['John', 'Emily', 'Kate', 'Joseph', 'Dennis']
}

d2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'student_name': ['Brian', 'William', 'Lilian', 'Grace', 'Caleb']
}

df1 = pd.DataFrame(d1, columns=['subject_id', 'student_name'])
df2 = pd.DataFrame(d2, columns=['subject_id', 'student_name'])

df1

df2

pd.merge(df1,df2,on='subject_id')

raw = {
    'Name': ['John', 'John', 'Grace', 'Grace', 'Benjamin', 'Benjamin', 'Benjamin',
        'Benjamin', 'John', 'Alex', 'Alex', 'Alex'],
    'Position': [2, 1, 1, 4, 2, 4, 3, 1, 3, 2, 4, 3],
    'Year': [2009, 2010, 2009, 2010, 2010, 2010, 2011, 2012, 2011, 2013, 2013, 2012],
    'Marks':[408, 398, 422, 376, 401, 380, 396, 388, 356, 402, 368, 378]
}
df3 = pd.DataFrame(raw)

df3

group=df3.groupby('Year')
group

group

group.get_group(2010)

print(pd.concat([df1,df2]))

pd.concat([df1,df2], axis=1)

"""Descriptivve statistics"""

data = {
    'Name': ['John', 'Alice', 'Joseph', 'Alex'],
    'English': [64, 78, 68, 58],
    'Maths': [76, 54, 72, 64]
}

df = pd.DataFrame(data)
df.describe()