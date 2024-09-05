import streamlit as st

# Configure Streamlit page settings
st.set_page_config(
    page_title="Savings Budget Calculator",
    page_icon="💸",
    layout="centered",
)

# Title of the app
st.title("Savings Budget Calculator 💰")

# Introduction text
st.write("""
Plan your savings by inputting your monthly income, expenses, and savings goals. 
This calculator will help you determine how much you can save and whether you're on track with your financial goals.
""")

# User input for monthly income
income = st.number_input("Enter your monthly income ($)", min_value=0.0, step=100.0, value=3000.0)

# User input for expenses
housing_expense = st.number_input("Enter your monthly housing expenses ($)", min_value=0.0, step=50.0, value=1000.0)
food_expense = st.number_input("Enter your monthly food expenses ($)", min_value=0.0, step=50.0, value=300.0)
transport_expense = st.number_input("Enter your monthly transport expenses ($)", min_value=0.0, step=50.0, value=150.0)
other_expense = st.number_input("Enter other monthly expenses ($)", min_value=0.0, step=50.0, value=200.0)

# Total monthly expenses calculation
total_expenses = housing_expense + food_expense + transport_expense + other_expense

# Display total expenses
st.write(f"### Total Monthly Expenses: ${total_expenses:,.2f}")

# User input for savings goal
savings_goal = st.number_input("Enter your monthly savings goal ($)", min_value=0.0, step=100.0, value=500.0)

# Calculate potential savings
potential_savings = income - total_expenses

# Display potential savings
if potential_savings >= savings_goal:
    st.success(f"Great! You can meet your savings goal. You can save ${potential_savings:,.2f} this month!")
else:
    st.warning(f"Your current expenses exceed your savings goal. You can only save ${potential_savings:,.2f} this month.")

# Provide advice if expenses are too high
if potential_savings < savings_goal:
    st.write("You may want to reduce some expenses or increase your income to meet your savings goal.")
