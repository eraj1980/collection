import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="सकल शिक्षक समाज", layout="centered")

# --- Custom Style for compactness/center ---
st.markdown("""
    <style>
    .block-container {max-width: 580px !important; margin: auto;}
    .css-1kyxreq {padding-top: 12px;}
    .stTextInput > div > input {text-align: left;}
    .stNumberInput input {text-align: left;}
    </style>
""", unsafe_allow_html=True)

# --- Heading and Images ---
st.markdown('<h1 style="color:#cd2d01;font-size:3rem;letter-spacing:1px;text-shadow:2px 2px #222;">सकल शिक्षक समाज</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0a2755; font-size:1.4rem;">मीरा-भाईंदर</h2>', unsafe_allow_html=True)
st.image("banner.png", use_column_width=True)
st.image("content.png", use_column_width=True)
st.write("""
मिरा-भाईंदर शहर दिन प्रतिदिन विकसित होता एक बड़ा उपनगर है। इसके सर्वांगीण विकास में समाज के हर वर्ग के साथ-साथ शिक्षकों का भी महत्वपूर्ण योगदान रहा है।
""")

# --- Compact Support Form ---
st.markdown('<h3 style="margin-top:1em;">आपका समर्थन दर्ज करें</h3>', unsafe_allow_html=True)

with st.form("support_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("नाम:", key="name", max_chars=50)
    with col2:
        age = st.number_input("उम्र:", min_value=18, max_value=120, key="age")

    mobile = st.text_input("मोबाइल नंबर (10 digits):", max_chars=10)
    email = st.text_input("ईमेल आईडी:")

    col3, col4 = st.columns(2)
    with col3:
        flat = st.text_input("फ्लैट नंबर:")
    with col4:
        building = st.text_input("बिल्डिंग नंबर:")

    col5, col6 = st.columns(2)
    with col5:
        society = st.text_input("सोसाइटी का नाम:")
    with col6:
        sector = st.text_input("सेक्टर नंबर:")

    st.markdown("<div style='font-weight:600;text-align:center;'>म Mira Road (East), Thane - 401107</div>", unsafe_allow_html=True)
    consent = st.checkbox("मैं समर्थन करता/करती हूँ (I support)")

    submitted = st.form_submit_button("समर्थन दर्ज करें")
    if submitted:
        if not all([name, age, mobile, email, flat, building, society, sector, consent]):
            st.error("सभी फील्ड भरें और समर्थन दें टिक करें।")
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
            script_url = 'https://script.google.com/macros/s/AKfycbyL5VUyINaVinfQfM1BvxJv7zJafBYxshYB7mN38cMzW7lVp_GXXvDvAOKbpfkqt_yT5Q/exec'
            try:
                res = requests.post(script_url, data=data)
                if res.status_code == 200:
                    st.success("धन्यवाद! आपका समर्थन दर्ज किया गया है।")
                else:
                    st.error(f"Submission failed! Status: {res.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

