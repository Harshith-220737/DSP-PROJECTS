import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


# -------------------- SIMPLE LINEAR REGRESSION --------------------

size = np.array([600,750,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]).reshape(-1,1)
price = np.array([90000,110000,120000,135000,150000,165000,180000,200000,210000,225000,240000,250000,265000,280000,300000])

model = LinearRegression()
model.fit(size, price)

pred_price = model.predict([[2100]])
print("Predicted price for 2100 sqft:", pred_price[0])

plt.scatter(size, price)
plt.plot(size, model.predict(size))
plt.title("House Price Prediction")
plt.show()

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)


# -------------------- ADVERTISING VS SALES --------------------

ad = np.array([5,7,8,10,12,15,18,20,22,25,27,30]).reshape(-1,1)
sales = np.array([25,30,34,40,48,55,60,70,75,82,90,100])

model2 = LinearRegression()
model2.fit(ad, sales)

print("Sales for budget 35:", model2.predict([[35]])[0])

plt.scatter(ad, sales)
plt.plot(ad, model2.predict(ad))
plt.title("Advertising vs Sales")
plt.show()

print("Slope:", model2.coef_[0])


# -------------------- POLYNOMIAL REGRESSION --------------------

level = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
salary = np.array([30000,35000,40000,50000,65000,80000,100000,130000,170000,220000])

lin = LinearRegression()
lin.fit(level, salary)

poly = PolynomialFeatures(degree=3)
level_poly = poly.fit_transform(level)

lin2 = LinearRegression()
lin2.fit(level_poly, salary)

print("Salary for level 11:", lin2.predict(poly.transform([[11]]))[0])

plt.scatter(level, salary)
plt.plot(level, lin.predict(level))
plt.plot(level, lin2.predict(level_poly))
plt.title("Polynomial Regression")
plt.show()


# -------------------- MULTIPLE LINEAR REGRESSION --------------------

data = pd.DataFrame({
    "study":[2,3,3,4,5,6,6,7,8,9,10],
    "sleep":[6,7,6,7,6,7,8,7,7,8,8],
    "att":[70,75,80,85,88,90,92,94,95,97,98],
    "score":[55,60,62,68,72,78,82,86,90,94,96]
})

X = data[["study","sleep","att"]]
y = data["score"]

model3 = LinearRegression()
model3.fit(X,y)

print("Predicted score:", model3.predict([[7,7,90]])[0])
print("Coefficients:", model3.coef_)


# -------------------- LOGISTIC REGRESSION (SPAM) --------------------

spam_data = pd.DataFrame({
    "len":[120,80,200,60,300,150,90,70,250,100,180,85],
    "links":[1,0,1,0,1,1,0,0,1,0,1,0],
    "spam":[1,0,1,0,1,1,0,0,1,0,1,0]
})

X = spam_data[["len","links"]]
y = spam_data["spam"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train,y_train)

pred = clf.predict(X_test)
print("Spam predictions:", pred)


# -------------------- LOAN APPROVAL --------------------

loan = pd.DataFrame({
    "income":[30000,40000,50000,25000,45000,32000,60000,70000,20000,52000],
    "credit":[650,700,720,600,680,640,750,780,580,710],
    "approve":[0,1,1,0,1,0,1,1,0,1]
})

X = loan[["income","credit"]]
y = loan["approve"]

model4 = LogisticRegression()
model4.fit(X,y)

print("Loan approval:", model4.predict([[48000,690]])[0])


# -------------------- EVALUATION METRICS --------------------

heart = pd.DataFrame({
    "age":[45,50,30,25,60,55,35,40,65,28],
    "bp":[130,140,120,110,150,145,125,128,155,115],
    "chol":[200,220,180,170,240,230,190,195,250,175],
    "disease":[1,1,0,0,1,1,0,0,1,0]
})

X = heart[["age","bp","chol"]]
y = heart["disease"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model5 = LogisticRegression()
model5.fit(X_train,y_train)

y_pred = model5.predict(X_test)

print("Accuracy:", accuracy_score(y_test,y_pred))
print("Precision:", precision_score(y_test,y_pred))
print("Recall:", recall_score(y_test,y_pred))
print("F1:", f1_score(y_test,y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test,y_pred))