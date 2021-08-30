# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB


# %%
df = pd.read_csv('titanic.csv',sep=',')

df


# %%
df.drop(['PassengerId','Name','Ticket','Cabin','Embarked','Parch' ], axis=1, inplace=True)

df


# %%
df = df.replace({'Sex': {'male': 1, 'female': 0}})


# %%

x = pd.DataFrame({
    "AgeRev": ~ df["Age"].notnull(),
    "Pclass": df["Pclass"],
    "Pclass3": (df["Pclass"] == 3) & ( ~ (df["Age"].notnull())),
    "Pclass2": (df["Pclass"] == 2) & ( ~ (df["Age"].notnull())),
    "Pclass1": (df["Pclass"] == 1) & ( ~ (df["Age"].notnull())),
})

df["Age"].where((~ x["Pclass3"]), 20, inplace=True)
df["Age"].where((~ x["Pclass2"]), 30, inplace=True)
df["Age"].where((~ x["Pclass1"]), 40, inplace=True)

df


# %%
df = np.array(df)
x_train, x_test, y_train, y_test = train_test_split(df[:,0:4], df[:,4], test_size = .3, random_state=25)
# print ("x_train: ", x_train)
# print ("y_train: ", y_train)
# print("x_test: ", x_test)
# print ("y_test: ", y_test)


# %%
LogReg = LogisticRegression().fit(x_train, y_train)


# %%
y_pred = LogReg.predict(x_test)

print(y_test)
y_pred


# %%
print(classification_report(y_test, y_pred))


# %%
gnb = GaussianNB().fit(x_train, y_train)


# %%
print(classification_report(y_test, y_pred))


