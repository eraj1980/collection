import streamlit as st
import requests

st.set_page_config(layout="centered")

st.markdown("""
    <style>
    .block-container {max-width: 580px !important; margin: auto;}
    .center-big {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 700;
        color: #114688;
        letter-spacing: 2px;
        margin: 20px 0 12px 0;
    }
    .thick-line {
        border: none;
        border-top: 4px solid #0a2755;
        margin-bottom: 22px;
        margin-top: 4px;
        width: 90%;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Banner image
st.image("banner.png", use_container_width=True)

# Large centered Mira-Bhayandar below banner
st.markdown('<div class="center-big">मीरा-भाईंदर</div>', unsafe_allow_html=True)
st.markdown('<hr class="thick-line">', unsafe_allow_html=True)

# Single content image (no extra duplicated text)
st.image("content.png", use_container_width=True)

# Survey form
st.markdown('<h3 style="text-align:center;margin-top:1.2em;">Register Your Support</h3>', unsafe_allow_html=True)

with st.form("support_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        age = st.number_input("Age", min_value=18, max_value=120)

    mobile = st.text_input("Mobile Number (10 digits)")
    email = st.text_input("Email Address")

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

    st.markdown("<div style='font-weight:600;text-align:center;'>Mira Road (East), Thane - 401107</div>", unsafe_allow_html=True)

    consent = st.checkbox("I support")

    submitted = st.form_submit_button("Submit Support")
    if submitted:
        if not all([name, age, mobile, email, flat, building, society, sector, consent]):
            st.error("Please fill in all fields and check the 'I support' box.")
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
                    st.error(f"Submission failed! Status: {res.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
