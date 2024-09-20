import streamlit as st

def run():
    st.write("### Home Budget Planner")
    st.write("Enter your budget details.")
    income = st.number_input("Monthly Income", min_value=0)
    expenses = st.number_input("Monthly Expenses", min_value=0)
    if income and expenses:
        st.write(f"Budget details: Income: ${income}, Expenses: ${expenses}")
        st.write("Budget planning functionality will be implemented here.")
