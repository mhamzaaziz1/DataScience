
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import load_iris
from sklearn import cross_validation
from sklearn import metrics

iris = load_iris()

X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.10, random_state=111)

logClassifier = linear_model.LogisticRegression( random_state=111)

logClassifier.fit(X_train, y_train)

predicted = logClassifier.predict(X_test)

print("\n Predicted Array: ", predicted)
#predictedarray([0, 0, 2, 2, 1, 0, 0, 2, 2, 1, 2, 0, 2, 2, 2])
print("\n Y_Test Array: \t ", y_test)
#y_testarray([0, 0, 2, 2, 1, 0, 0, 2, 2, 1, 2, 0, 2, 2, 2])

print("\n Accuracy Score: ", metrics.accuracy_score(y_test, predicted))
