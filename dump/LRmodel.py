from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4, random_state=1)

# print(x_train.shape)
# print(x_test.shape)

# print(y_train.shape)
# print(y_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

from sklearn import metrics
print("kNN model accoracy",metrics.accuracy_score(y_test,y_pred))

sample = [[3,5,4,2],[2,3,5,4]]
preds = knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("\nPredictions",pred_species)

import joblib
joblib.dump(knn,'iris_knn.pkl')