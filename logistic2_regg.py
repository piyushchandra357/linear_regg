from sklearn import datasets, linear_model, metrics
 
digits = datasets.load_digits()
 
X = digits.data
y = digits.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)
 
reg = linear_model.LogisticRegression()
 
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
 
print("Logistic Regression model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)