import streamlit as st
import streamlit.components.v1 as components
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

# Banner and Mira-Bhayandar
st.image("banner.png", use_container_width=True)
st.markdown('<div class="center-big">मीरा-भाईंदर</div>', unsafe_allow_html=True)
st.markdown('<hr class="thick-line">', unsafe_allow_html=True)
st.image("content.png", use_container_width=True)

st.markdown('<h3 style="text-align:center;margin-top:1em;">Register Your Support</h3>', unsafe_allow_html=True)

# Collect other fields with Streamlit widgets
first_name = st.text_input("First Name")
surname = st.text_input("Surname")
mobile = st.text_input("Mobile Number (10 digits)")
age = st.number_input("Age", min_value=18, max_value=120)
email = st.text_input("Email Address")
flat = st.text_input("Flat Number")
building = st.text_input("Building Number")
society = st.text_input("Society Name")
sector = st.text_input("Sector Number")

st.markdown("<div style='font-weight:600;text-align:center;'>Mira Road (East), Thane - 401107</div>", unsafe_allow_html=True)

# Custom HTML block for horizontal radio and centered checkbox + submit button
html_code = """
<div style="text-align:center; margin-top: 20px;">
  <label style="font-weight:600;">Gender</label><br>
  <input type="radio" id="male" name="gender" value="Male" checked>
  <label for="male" style="margin-right:15px;">Male</label>
  <input type="radio" id="female" name="gender" value="Female">
  <label for="female" style="margin-right:15px;">Female</label>
  <input type="radio" id="other" name="gender" value="Other">
  <label for="other">Other</label>

  <br><br>
  <input type="checkbox" id="consent" name="consent" style="display:inline-block; vertical-align:middle; width: auto;">
  <label for="consent" style="font-weight:600; display:inline-block; vertical-align:middle;">I support</label>

  <br><br>
  <button id="submitBtn" style="
    background-color:#0a2755; 
    color:white; 
    font-weight:bold; 
    border:none; 
    padding: 12px 35px; 
    border-radius:8px; 
    cursor:pointer;
    font-family: Arial, sans-serif;
    font-size: 1rem;
  ">Submit Support</button>
</div>

<script>
  const submitBtn = document.getElementById('submitBtn');
  submitBtn.addEventListener('click', () => {
    const genderElems = document.getElementsByName('gender');
    let gender = null;
    for (const elem of genderElems) {
      if (elem.checked) { gender = elem.value; break; }
    }
    const consentChecked = document.getElementById('consent').checked;

    if (!gender) {
      alert('Please select gender.');
      return;
    }
    if (!consentChecked) {
      alert('Please check "I support" checkbox.');
      return;
    }

    // send data back to Streamlit via window.parent.postMessage
    window.parent.postMessage({
      isFromStreamlit: true,
      genderSelected: gender,
      consentChecked: consentChecked,
      clickedSubmit: true
    }, '*');
  });
</script>
"""

# Embed the HTML component
msg = components.html(html_code, height=160)

# Sync values back from HTML via Streamlit's onMessage
gender = st.session_state.get("gender", None)
consent = st.session_state.get("consent", False)

# Listen for messages from HTML (handled below when used in Streamlit sharing)

# Process form submission combining HTML + Streamlit inputs
def handle_submit():
    if not all([first_name, surname, mobile, age, email, flat, building, society, sector, consent]):
        st.error("Fill all fields and check the consent box.")
        return
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
        "consent": "Yes" if consent else "No"
    }
    script_url = 'YOUR_GOOGLE_APPS_SCRIPT_WEBAPP_URL'
    try:
        res = requests.post(script_url, data=data)
        if res.status_code == 200:
            st.success("Thank you! Your support has been recorded.")
        else:
            st.error(f"Submission failed! Status: {res.status_code}")
    except Exception as e:
        st.error(f"Error sending data: {str(e)}")

# Button to handle submission after receiving events from HTML (could be triggered from JS)
st.button("Finalize Submit", on_click=handle_submit)
