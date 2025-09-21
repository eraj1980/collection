import streamlit as st

st.title("Register Your Support")

first_name = st.text_input("First Name *")
last_name = st.text_input("Last Name *")
mobile = st.text_input("Mobile Number *")
gender = st.radio("Gender *", ("Male", "Female", "Other"))
email = st.text_input("Email Address *")

flat = st.text_input("Flat Number *")
building = st.text_input("Building Number *")
society = st.text_input("Society Name *")
sector = st.text_input("Sector Number *")

consent = st.checkbox("I support")

if st.button("Submit Support"):
    if not all([first_name, last_name, mobile, gender, email, flat, building, society, sector, consent]):
        st.error("Please fill in all required fields and tick the consent box.")
    else:
        # Handle saving data here (e.g., call Google Sheets API or Google Apps Script)
        st.success("Thank you! Your support has been recorded.")
