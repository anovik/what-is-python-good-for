import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import tree  
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
  
import warnings
warnings.filterwarnings('ignore')

iris = sns.load_dataset('iris')
print(iris.head())

print(iris.info())

fig, axes = plt.subplots(2, 2)

ax = sns.boxplot(x="species", y="sepal_length", data=iris, orient='v', 
    ax=axes[0, 0])
ax = sns.boxplot(x="species", y="sepal_width", data=iris, orient='v', 
    ax=axes[0, 1])
ax = sns.boxplot(x="species", y="petal_length", data=iris, orient='v', 
    ax=axes[1, 0])
ax = sns.boxplot(x="species", y="petal_width", data=iris, orient='v', 
    ax=axes[1, 1])

plt.show()

X = iris.iloc[:, :-1]
y = iris.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                       test_size=0.3,
                                       random_state = 105)


dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

plt.figure(figsize=(15, 10))
tree.plot_tree(dt, filled=True)
plt.show()

y_pred = dt.predict(X_test)

print(accuracy_score(y_pred, y_test))
print(classification_report(y_pred, y_test))


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train)

y_pred = kmeans.predict(X_test)

y_test.replace({'setosa': 0, 'versicolor':2, 'virginica':1}, inplace=True)

print(classification_report(y_test, y_pred))
