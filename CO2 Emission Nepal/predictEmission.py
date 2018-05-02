import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression



record = pd.read_csv('Carbon dioxide emissions in Nepal.csv')
record = pd.DataFrame(record)
record = record.as_matrix()
X = record[1:-3,0].reshape(-1,1)
y = record[1:-3,2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#Choose the model.
model = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=1)

#Fit the model.
model.fit(X_train, y_train)

#Save the model.
joblib.dump(model, 'CO2 Emission.pkl')

#Evaluate the error. Mean absolute error to evaluate the accuracy of the model.
mse = mean_absolute_error(y_train, model.predict(X_train))
print ("Training Set Mean Absolute Error: %.2f" % mse)

#difference between the model’s expected predictions and the actual values.
mse = mean_absolute_error(y_test, model.predict(X_test))
print ("Test Set Mean Absolute Error: %.2f" % mse)
print(model.predict(1998))
