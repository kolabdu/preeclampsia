import streamlit as st
import joblib





with open('rf_model.joblib','rb') as file:
    model = joblib.load(file)

st.title('Preeclampsia Risk Level Checker')
def predict(age, sys,dia, bs, temp, heart):
    prediction = model.predict([[age, sys,dia, bs, temp, heart]])
    return prediction


def main():
    age = st.text_input('Age')
    sys = st.text_input('Systolic BP')
    dia = st.text_input('Diastolic BP')
    bs = st.text_input('Blood Suagr')
    temp = st.text_input('Body Tempareture')
    heart = st.text_input('Heart Rate')
    result = ''
    risk = ''

    if st.button('Check Risk Level'):
        result = predict(age, sys, dia, bs, temp, heart)
        for i in range(len(result)):

            if result[i] ==0:
                risk ='Low'
            elif result[i] == 1:
                risk = 'midium'
            elif result[i]  == 2:
                risk = 'HIGH'
            else:
                risk ='The input you enter are not valid'
            st.success(f'Your risk Level is: {risk}')
        # print()


if __name__ == '__main__':
    main()
