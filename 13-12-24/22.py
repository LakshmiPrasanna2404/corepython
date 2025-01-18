import streamlit as st
st.title("Gross salary Calculator")
basic_salary=st.number_input("Enter your Basic Salary:",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
    HRA=0
    DA=0

    if basic_salary<10000:
        HRA=(67/100)*basic_salary
        DA=(73/100)*basic_salary
    elif(basic_salary>10000 and basic_salary<20000):
        HRA = (69/100)*basic_salary
        DA = (76/100)*basic_salary
    else:
        HRA = (73/100)*basic_salary
        DA = (89/100)*basic_salary
    GS=HRA+DA+basic_salary
    print(f"Gross Salary:{GS}")