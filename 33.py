import streamlit as st
st.title("Shopping bill")
salary=st.number_input("Enter your Basic Salary:",min_value=0,step=1000)
bill1 = st.number_input("Enter the shopping bill number 1:", min_value=0)
bill2 = st.number_input("Enter the shopping bill number 2:", min_value=0)
bill3 = st.number_input("Enter the shopping bill number 3:", min_value=0)
total_bill = bill1 + bill2 + bill3
st.write(f"Total amount spent on shopping: {total_bill}")
if salary>0:
    percentage_spent = (total_bill * 100) / salary
    st.write(f"The percentage of salary spent on shopping is: {percentage_spent:.2f}%")
else:
    st.write("value should be greater than zero")