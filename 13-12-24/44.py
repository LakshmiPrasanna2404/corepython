import streamlit as st
project=st.number_input("Enter project marks: ")
internal=st.number_input("Enter internal marks: ")
external=st.number_input("Enter external marks: ")
st.button("Calculate Grade")

if project>50 and internal>50 and external>50:
    total_marks = (70/100)*project+(10/100)*internal+(20/100)*external
    if total_marks>90:
        st.success("A grade")
    elif 80<total_marks<90:
        st.success("B grade")
    else:
        st.success("C grade")
else:
    if project<50:
        st.error("Failed in project")
    if internal<50:
        st.error("Failed in internal")
    if external<50:
        st.error("Failed in external")
