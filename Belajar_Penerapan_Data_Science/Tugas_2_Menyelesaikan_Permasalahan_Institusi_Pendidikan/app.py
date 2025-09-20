import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Student Performance Analysis')

data = pd.DataFrame()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Application_mode = st.selectbox('Application mode', ['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)'], index=None)
    data['Application_mode'] = [Application_mode]

with col2:
    Debtor = st.selectbox('Debtor', ['yes', 'no'], index=1)
    data['Debtor'] = [Debtor]

with col3:
    Tuition_fees_up_to_date = st.selectbox('Tuition fees up to date', ['yes', 'no'], index=None)
    data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]

with col4:
    Gender = st.selectbox('Gender', ['male', 'female'], index=None)
    data['Gender'] = [Gender]

with col5:
    Scholarship_holder = st.selectbox('Scholarship holder',['yes', 'no'], index=None)
    data['Scholarship_holder'] = [Scholarship_holder]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Age_at_enrollment = st.number_input('Age at enrollment', min_value=15, max_value=70, value=15)
    data['Age_at_enrollment'] = [Age_at_enrollment]

with col2:
    Curricular_units_1st_sem_approved = st.number_input('Curricular units 1st sem approved', min_value=0, max_value=60, value=0)
    data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]

with col3:
    Curricular_units_1st_sem_grade = st.number_input('Curricular units 1st sem grade', min_value=0, max_value=60, value=0)
    data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]

with col4:
    Curricular_units_2nd_sem_approved = st.number_input('Curricular units 2nd sem approved', min_value=0, max_value=60, value=0)
    data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]

with col5:
    Curricular_units_2nd_sem_grade = st.number_input('Curricular units 2nd sem grade', min_value=0, max_value=60, value=0)
    data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]

if st.button('Predict'):
    new_data = data
    st.write("Results:")
    st.write("Dropout")
