# importar las librerias
import streamlit as st
import pickle
import pandas as pd

with open('lin_reg.pkl', 'rb') as li:
    lin_reg = pickle.load(li)

with open('log_reg.pkl', 'rb') as lo:
    log_reg = pickle.load(lo)

with open('svc_m.pkl', 'rb') as sv:
    svc_mo = pickle.load(sv)


# función para clasificar las plantas
def classify(num):
    if num == 0:
        return 'Setosa'
    elif num == 1:
        return 'Versicolor'
    else:
        return 'Virginica'


def main():
    st.title('Modelamiento de Iris por @killjoy3452')
    st.sidebar.header('User input Parameters')

    def user_input_parameters():
        sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_parameters()

    option = ['Linear regression', 'Logistic regression', 'Super vector machine']
    model = st.sidebar.selectbox('Which model you want to use', option)

    st.subheader('User Input Parameters')
    st.subheader(model)
    st.write(df)

    if st.button('RUN'):
        if model == 'Linear regression':
            st.success(classify(lin_reg.predict(df)))
        elif model == 'Logistic regression':
            st.success(classify(log_reg.predict(df)))
        else:
            st.success(classify(svc_mo.predict(df)))


if __name__ == '__main__':
    main()
