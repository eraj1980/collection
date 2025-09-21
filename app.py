import streamlit as st
import requests

st.set_page_config(layout="centered")

# ---- Custom CSS for centering, color, font, spacing ----
st.markdown("""
<style>
.block-container { max-width: 480px !important; margin: auto; }
.bigtitle {text-align:center; font-size:2.2rem; font-weight:700; color:#114688; letter-spacing:1px; margin-bottom:0.6em;}
.thick-line {border:none; border-top:4px solid #0a2755; margin-bottom:18px; width:90%; margin-left:auto; margin-right:auto;}
.compact-input input, .compact-input select { height:36px; font-size:1rem; }
.radio-row div[role=radiogroup] { display:flex !important; gap:38px; justify-content:center; }
.center-row {display:flex; justify-content:center; align-items:center; gap:18px;}
.stButton > button {background-color:#0a2755; color:white; font-weight:700; font-family: Arial,sans-serif; border:none; width:200px; height:42px; border-radius:8px; margin:8px auto;}
.stButton > button:hover {background-color:#1842a7;}
</style>
""", unsafe_allow_html=True)

# ---- Top Hindi Banner and Heading (centered) ----
st.image("banner.png", use_container_width=True)
st.markdown('<div class="bigtitle">मीरा-भाईंदर</div>', unsafe_allow_html=True)
st.markdown('<hr class="thick-line">', unsafe_allow_html=True)

st.image("content.png", use_container_width=True)

# ---- English Survey Form Compact and Grouped ----
st.markdown('<h3 style="text-align:center;margin-top:0.2em;margin-bottom:0.8em;">Register Your Support</h3>', unsafe_allow_html=True)

with st.form("support_form"):
    # Name row
    fn_col, sn_col = st.columns([1,1])
    with fn_col:
        first_name = st.text_input("First Name")
    with sn_col:
        surname = st.text_input("Surname")

    # Gender row, horizontal radio
    st.markdown('<div class="radio-row">', unsafe_allow_html=True)
    gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Mobile, age
    mob_col, age_col = st.columns([2,1])
    with mob_col:
        mobile = st.text_input("Mobile Number (10 digits)")
    with age_col:
        age = st.number_input("Age", min_value=18, max_value=120)

    email = st.text_input("Email Address")

    # Flat + Building row
    flat_col, build_col = st.columns([1,1])
    with flat_col:
        flat = st.text_input("Flat Number")
    with build_col:
        building = st.text_input("Building Number")

    # Society + Sector row
    soc_col, sec_col = st.columns([1,1])
    with soc_col:
        society = st.text_input("Society Name")
    with sec_col:
        sector = st.text_input("Sector Number")

    st.markdown("<div style='font-weight:600;text-align:center;margin-top:10px;'>Mira Road (East), Thane - 401107</div>", unsafe_allow_html=True)

    # Consent checkbox and submit button centered together
    col_c1, col_c2, col_c3 = st.columns([1,2,1])
    with col_c2:
        consent = st.checkbox("I support")
        submitted = st.form_submit_button("Submit Support")

    if submitted:
        if not all([first_name, surname, gender, mobile, age, email, flat, building, society, sector, consent]):
            st.error("Please fill in all fields and check the 'I support' box.")
        else:
            data = {
                "first_name": first_name,
                "surname": surname,
                "gender": gender,
                "mobile": mobile,
                "age": age,
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
