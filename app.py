import streamlit as st
import requests

# Page title and images
st.title("सकल शिक्षक समाज")
st.image("banner.png")
st.markdown("### मीरा-भाईंदर")
st.image("content.png")

st.header("Register Your Support")

# Collect input fields similar to your HTML form
name = st.text_input("Name:", "")
age = st.number_input("Age:", min_value=18, max_value=120)
mobile = st.text_input("Mobile Number (10 digits):", "")
email = st.text_input("Email ID:", "")

flat = st.text_input("Flat Number:", "")
building = st.text_input("Building Number:", "")
society = st.text_input("Society Name:", "")
sector = st.text_input("Sector Number:", "")

consent = st.checkbox("I support")

# Submit button sends data to Google Sheets via Google Apps Script
if st.button("Submit Support"):
    if not all([name, age, mobile, email, flat, building, society, sector, consent]):
        st.error("Please fill all fields and check consent.")
    else:
        data = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "email": email,
            "flat": flat,
            "building": building,
            "society": society,
            "sector": sector,
            "consent": "Yes"
        }
        script_url = 'YOUR_GOOGLE_APPS_SCRIPT_WEBAPP_URL'  # replace with actual URL
        try:
            res = requests.post(script_url, data=data)
            if res.status_code == 200:
                st.success("Thank you! Your support has been recorded.")
            else:
                st.error(f"Submission failed. Status: {res.status_code}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
