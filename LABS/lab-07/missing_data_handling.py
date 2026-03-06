# Missing Data Handling, Duplicates, Data Cleaning Lab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


# PART 1 : Missing Data Handling

data1 = {
    'Name': ['Asha', 'Ravi', 'Kiran', 'Meena', 'John', 'Priya'],
    'Age': [20, 21, None, 22, 20, None],
    'Marks': [85, None, 78, 90, None, 88],
    'City': ['Hyderabad', 'Chennai', None, 'Mumbai', 'Delhi', 'Hyderabad']
}

df1 = pd.DataFrame(data1)

print("\nPART 1 - Original Data")
print(df1)

print("\nMissing values")
print(df1.isnull())

print("\nMissing count")
print(df1.isnull().sum())

df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
df1['Marks'] = df1['Marks'].fillna(df1['Marks'].median())
df1['City'] = df1['City'].fillna(df1['City'].mode()[0])

df1 = df1.dropna(subset=['Marks'])

print("\nAfter Cleaning")
print(df1)


# PART 2 : Duplicate Handling

data2 = {
    'Emp_ID': [101,102,103,101,104,105,102],
    'Name': ['Ravi','Asha','John','Ravi','Kiran','Meena','Asha'],
    'Salary': [50000,60000,55000,50000,52000,58000,60000]
}

df2 = pd.DataFrame(data2)

print("\nPART 2 - Duplicates")
print(df2.duplicated())

print("Rows before:", len(df2))

df2 = df2.drop_duplicates(keep='first')

print("Rows after:", len(df2))
print(df2)


# PART 3 : Data Type Conversion

data3 = {
    'Product': ['A','B','C','D'],
    'Price': ['100','200','150','300'],
    'Date': ['01-01-2024','02-01-2024','03-01-2024','04-01-2024']
}

df3 = pd.DataFrame(data3)

print("\nPART 3 - Before Conversion")
print(df3.dtypes)

df3['Price'] = pd.to_numeric(df3['Price'])
df3['Date'] = pd.to_datetime(df3['Date'], format='%d-%m-%Y')

print("\nAfter Conversion")
print(df3.dtypes)


# PART 4 : Outlier Detection

sales = np.array([100,120,130,115,5000,140,125,110])

Q1 = np.percentile(sales,25)
Q3 = np.percentile(sales,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = sales[(sales < lower) | (sales > upper)]
print("\nPART 4 - Outliers:", outliers)

clean_sales = sales[(sales >= lower) & (sales <= upper)]

print("Mean before:", np.mean(sales))
print("Mean after:", np.mean(clean_sales))


# PART 5 : Normalization & Standardization 

marks = np.array([50,60,70,80,90])

min_val = marks.min()
max_val = marks.max()

minmax = (marks - min_val) / (max_val - min_val)

mean = marks.mean()
std = marks.std()

zscore = (marks - mean) / std

print("\nPART 5 - MinMax:", minmax)
print("ZScore:", zscore)


# PART 6 : String Cleaning

data6 = {
    'Email': [' test@gmail.com ', 'RAVI@GMAIL.COM', 'john123 @gmail.com', None]
}

df6 = pd.DataFrame(data6)

df6['Email'] = df6['Email'].str.strip()
df6['Email'] = df6['Email'].str.lower()
df6['Email'] = df6['Email'].str.replace(" ", "")
df6['Email'] = df6['Email'].fillna("unknown@gmail.com")

print("\nPART 6 - Cleaned Emails")
print(df6)


# PART 7 : Binning

ages = [18,22,25,30,35,40,45,50]

bins = [18,25,40,60]
labels = ['Young','Adult','Senior']

df7 = pd.DataFrame({'Age':ages})
df7['Category'] = pd.cut(df7['Age'], bins=bins, labels=labels)

print("\nPART 7 - Binning")
print(df7)
print(df7['Category'].value_counts())


# PART 8 : Correlation

data8 = {
    'Hours_Studied': [2,4,6,8,10],
    'Marks': [40,50,65,80,95]
}

df8 = pd.DataFrame(data8)

corr = df8['Hours_Studied'].corr(df8['Marks'])

print("\nPART 8 - Correlation:", corr)

plt.scatter(df8['Hours_Studied'], df8['Marks'])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study vs Marks")
plt.show()


# PART 9 : Large Dataset

data9 = {
'Customer_ID':[1,2,3,3,4],
'Age':[22,25,None,30,28],
'Income':[50000,60000,None,70000,65000],
'Gender':['Male','Female','Female','Female','Male'],
'Purchase_Amount':[200,300,10000,250,270],
'City':['Hyderabad','Delhi','Delhi','Delhi','Mumbai']
}

df9 = pd.DataFrame(data9)

print("\nPART 9 - Null values")
print(df9.isnull().sum())

df9['Income'] = df9['Income'].fillna(df9['Income'].median())

df9 = df9.drop_duplicates()

Q1 = df9['Purchase_Amount'].quantile(0.25)
Q3 = df9['Purchase_Amount'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

df9 = df9[(df9['Purchase_Amount'] >= lower) & (df9['Purchase_Amount'] <= upper)]

scaler = StandardScaler()
df9['Income'] = scaler.fit_transform(df9[['Income']])

df9['Gender'] = df9['Gender'].map({'Male':0,'Female':1})

print("\nCorrelation")
print(df9[['Income','Purchase_Amount']].corr())

df9['Age_Group'] = pd.cut(df9['Age'], bins=[18,30,50], labels=['Young','Adult'])

df9.to_csv("cleaned_dataset.csv", index=False)

print("\nFinal Dataset")
print(df9)