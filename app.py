bg_url = "https://raw.githubusercontent.com/your-username/your-repo/main/bg.png"

st.markdown(f"""
    <style>
    body {{
      background-image: url('{bg_url}');
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}
    .form-panel {{
      background-color: rgba(255,255,255,0.97);
      padding: 2rem 1.4rem 1.2rem 1.4rem;
      border-radius: 15px;
      box-shadow: 0 0 22px rgba(0,0,0,0.12);
      max-width: 500px;
      margin: 48px auto 32px auto;
    }}
    div.stButton > button:first-child {{
      background-color:#0a2755;
      color:white;
      font-weight:700;
      font-family:Arial,sans-serif;
      font-size:1.18rem;
      border:none;
      width:220px;
      height:45px;
      border-radius:8px;
      display:block;
      margin:0px auto 10px auto;
    }}
    div.stButton > button:first-child:hover {{
      background-color:#114688;
    }}
    </style>
""", unsafe_allow_html=True)
