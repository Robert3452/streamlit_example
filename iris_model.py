# importar las librearias necesarias
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
import pickle

# cargar los datos en un dataset
iris = datasets.load_iris()

X = iris.data
Y = iris.target

# separar datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, Y)

lin_reg = LinearRegression()
log_reg = LogisticRegression(max_iter=1000)
svc_m = SVC()

# entrenar los modelos
lin_regr = lin_reg.fit(x_train, y_train)
log_regr = log_reg.fit(x_train, y_train)
svc_mo = svc_m.fit(x_train, y_train)

with open('lin_reg.pkl', 'wb') as li:
    pickle.dump(lin_regr, li)

with open('log_reg.pkl', 'wb') as lo:
    pickle.dump(log_regr, lo)

with open('svc_m.pkl', 'wb') as sv:
    pickle.dump(svc_mo, sv)
