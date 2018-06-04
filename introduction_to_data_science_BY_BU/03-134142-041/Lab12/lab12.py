
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io

"""# UPLOADING DATASET"""

from google.colab import files
uploadfile = files.upload()

dataset = pd.read_csv(io.StringIO(uploadfile['iris.csv.txt'].decode('utf-8')))

dataset.head()

import seaborn as s
import matplotlib.pyplot as plt

# %matplotlib inline
plt.figure(figsize=(4,8))
ax=s.countplot(x=dataset.iloc[:, -1],data=dataset )
for p in ax.patches:
        ax.annotate('{:}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+50))

s.pairplot(dataset, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='hist', markers=None, size=2.5, aspect=1, dropna=True, plot_kws=None, diag_kws=None, grid_kws=None)

X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values



"""# Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""# Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state = 0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test, y_pred)
pd.crosstab(y_test, y_pred, rownames = ['Actual'], colnames = ['Predicted'])

from sklearn.metrics import classification_report 

print("Model evaluation\n"+classification_report(y_test,y_pred))

print(__doc__)

import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold

# Create the RFE object and compute a cross-validated score.
# The "accuracy" scoring is proportional to the number of correct
# classifications
rfecv = RFECV(estimator=clf, step=1, cv=10, scoring='accuracy')
rfecv.fit(X_train, y_train)
# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.title('RFECV')
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(clf, X_test, y_test, cv=10, scoring='accuracy')
print("Accuracy: %0.5f (+/- %0.5f)" % (accuracy.mean(), accuracy.std() * 2))

"""Principla Component Analysis

# Applying PCA
"""

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

"""# Fitting Logistic Regression to the Training set"""

from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train)

"""# Predicting the Test set results"""

y_pred = classifier.predict(X_test)
print (y_pred)

"""# Making the Confusion Matrix"""

from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test, y_pred)
pd.crosstab(y_test, y_pred, rownames = ['Actual'], colnames = ['Predicted'])

print("Model evaluation\n" + classification_report(y_test,y_pred))

print(__doc__)

import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold

# Create the RFE object and compute a cross-validated score.
# The "accuracy" scoring is proportional to the number of correct
# classifications
rfecv = RFECV(estimator=classifier, step=1, cv=10, scoring='accuracy')
rfecv.fit(X_train, y_train)
# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.title('RFECV')
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(clf, X_test, y_test, cv=10, scoring='accuracy')
print("Accuracy: %0.5f (+/- %0.5f)" % (accuracy.mean(), accuracy.std() * 2))

