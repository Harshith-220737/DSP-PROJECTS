import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# Correlation matrix using numpy

x = [215,325,185,332,406,522,412,614,544,421,445,408]
y = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]

corr1 = np.corrcoef(x,y)
print("Correlation matrix (sales vs temperature)")
print(corr1)
print()


# Age vs glucose correlation

x = [43,21,25,42,57,59]
y = [99,65,79,75,87,81]

corr2 = np.corrcoef(x,y)
print("Correlation matrix (age vs glucose)")
print(corr2)
print()


# Correlation using pandas

data = {
'x':[45,37,42,35,39],
'y':[38,31,26,28,33],
'z':[10,15,17,21,12]
}

df = pd.DataFrame(data)

print("Pandas correlation matrix")
print(df.corr())
print()


# Simple Linear Regression (Boston Housing)

url = "http://lib.stat.cmu.edu/datasets/boston"
raw = pd.read_csv(url, sep=r"\s+", skiprows=22, header=None)

data = np.hstack([raw.values[::2, :], raw.values[1::2, :2]])
target = raw.values[1::2, 2]

columns = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS",
           "RAD","TAX","PTRATIO","B","LSTAT"]

df = pd.DataFrame(data, columns=columns)
df["MEDV"] = target

print("Dataset dimension:", df.shape)
print()

print("Summary")
print(df.describe())
print()

X = df[['LSTAT']]
y = df['MEDV']

plt.scatter(X,y)
plt.xlabel("LSTAT")
plt.ylabel("MEDV")
plt.title("LSTAT vs MEDV")
plt.show()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

model = LinearRegression()
model.fit(X_train,y_train)

print("Intercept:",model.intercept_)
print("Slope:",model.coef_[0])
print()

y_pred = model.predict(X_test)

print("Actual values")
print(y_test.values[:10])

print("Predicted values")
print(y_pred[:10])
print()

print("MAE:",metrics.mean_absolute_error(y_test,y_pred))
print("MSE:",metrics.mean_squared_error(y_test,y_pred))
print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# Multiple Linear Regression

data = {
'year':[2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,
        2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],

'month':[12,11,10,9,8,7,6,5,4,3,2,1,
         12,11,10,9,8,7,6,5,4,3,2,1],

'interest_rate':[2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,
                 2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],

'unemployment_rate':[5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,
                     6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],

'stock_index_price':[1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,
                     1047,965,943,958,971,949,884,866,876,822,704,719]
}

df = pd.DataFrame(data)

X = df[['interest_rate','unemployment_rate']]
y = df['stock_index_price']

plt.scatter(df['interest_rate'],y)
plt.xlabel("interest_rate")
plt.ylabel("stock_index_price")
plt.show()

plt.scatter(df['unemployment_rate'],y)
plt.xlabel("unemployment_rate")
plt.ylabel("stock_index_price")
plt.show()

model = LinearRegression()
model.fit(X,y)

print("Intercept:",model.intercept_)
print("Coefficients:",model.coef_)

print()
print("Regression equation:")
print("stock_index_price = intercept + (coef1 * interest_rate) + (coef2 * unemployment_rate)")