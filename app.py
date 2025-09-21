import streamlit as st
import requests

st.set_page_config(page_title="Sakal Shikshak Samaj", layout="centered")

st.markdown("""
<style>
.block-container {
    max-width: 580px !important;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 style="color:#cd2d01;font-size:3rem;letter-spacing:1px;text-shadow:2px 2px #222;">Sakal Shikshak Samaj</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0a2755; font-size:1.4rem; margin-bottom:20px;">Meera-Bhayandar</h2>', unsafe_allow_html=True)
st.image("banner.png", use_container_width=True)
st.image("content.png", use_container_width=True)

st.write(
    "Meera-Bhayandar city is rapidly developing into a big suburb. "
    "Its comprehensive development has seen important contributions from all social classes including teachers."
)

# Centered form title
st.markdown('<h3 style="text-align:center;margin-top:1em;">Register Your Support</h3>', unsafe_allow_html=True)

# Form
with st.form("support_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", max_chars=50)
    with col2:
        age = st.number_input("Age", min_value=18, max_value=120)

    mobile = st.text_input("Mobile Number (10 digits)", max_chars=10)
    email = st.text_input("Email ID")

    col3, col4 = st.columns(2)
    with col3:
        flat = st.text_input("Flat Number")
    with col4:
        building = st.text_input("Building Number")

    col5, col6 = st.columns(2)
    with col5:
        society = st.text_input("Society Name")
    with col6:
        sector = st.text_input("Sector Number")

    st.markdown("<div style='font-weight: 600; text-align: center;'>Mira Road (East), Thane - 401107</div>", unsafe_allow_html=True)

    consent = st.checkbox("I support")

    submitted = st.form_submit_button("Submit Support")
    if submitted:
        if not all([name, age, mobile, email, flat, building, society, sector, consent]):
            st.error("Please fill in all fields and check the I support box.")
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
            script_url = 'YOUR_GOOGLE_APPS_SCRIPT_WEBAPP_URL'
            try:
                res = requests.post(script_url, data=data)
                if res.status_code == 200:
                    st.success("Thank you! Your support has been recorded.")
                else:
                    st.error(f"Submission failed with status: {res.status_code}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
