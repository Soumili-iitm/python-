import streamlit as st

def largest_number(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

st.title("Find the largest among 3 numbers")

num1 = st.number_input("Enter number 1:")
num2 = st.number_input("Enter number 2:")
num3 = st.number_input("Enter number 3:")

if st.button("Find largest"):
    result = largest_number(num1, num2, num3)
    st.write("The largest number is:", result)
