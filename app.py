import streamlit as st
import streamlit.components.v1 as components

# Your full HTML code as a string with inline CSS and JS.
html_code = """
<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>सकल शिक्षक समाज - मीरा-भाईंदर</title>
  <style>
    /* Paste your full CSS from your HTML here */
    /* Example: */
    :root {
      --primary-blue: #002561;
      --accent-blue: #0082f0;
      --bg-light: #f8f9fb;
      --text-dark: #1d1d1f;
      --text-light: #545454;
      --border-light: #dfe2e6;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      background-color: var(--bg-light);
      margin: 0;
      padding: 40px 0;
      color: var(--text-dark);
      line-height: 1.5;
      text-align: center;
      min-height: 100vh;
      box-sizing: border-box;
    }
    /* (Add all the rest of your CSS here exactly as it was in your HTML) */
  </style>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari&display=swap" rel="stylesheet" />
</head>
<body>
  <div class="container">
    <header>
      <img src="banner.png" alt="सकल शिक्षक समाज बैनर" />
      <div class="subtitle">मीरा-भाईंदर</div>
    </header>
    <main>
      <img src="content.png" alt="सकल शिक्षक समाज सामग्री" class="content-image" />
      <form id="supportForm" name="supportForm" class="signature-form">
        <h3>Register Your Support</h3>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required />
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" min="18" max="120" required />
        <label for="mobile">Mobile Number:</label>
        <input type="text" id="mobile" name="mobile" pattern="[0-9]{10}" title="Enter 10 digit mobile number" required />
        <label for="email">Email ID:</label>
        <input type="email" id="email" name="email" required />
        <hr style="margin: 30px 0; border: none; border-top: 1px solid #ccc;" />
        <div class="address-group">
          <div class="field">
            <label for="flat">Flat Number:</label>
            <input type="text" id="flat" name="flat" placeholder="Example: 102" required />
          </div>
          <div class="field">
            <label for="building">Building Number:</label>
            <input type="text" id="building" name="building" placeholder="Example: B-3" required />
          </div>
        </div>
        <label for="society">Society Name:</label>
        <input type="text" id="society" name="society" placeholder="Example: Sai Darshan" required />
        <label for="sector">Sector Number:</label>
        <input type="text" id="sector" name="sector" placeholder="Example: 5" required />
        <div style="margin: 10px 0 20px; font-weight: 600;">
          Mira Road (East), Thane - 401107
        </div>
        <div class="consent-checkbox">
          <input type="checkbox" id="consent" name="consent" required />
          <label for="consent">I support</label>
        </div>
        <button type="submit">Submit Support</button>
        <div class="loader" id="loader"></div>
      </form>
    </main>
  </div>
  <footer>
    &copy; 2025 सकल शिक्षक समाज | मीरा-भाईंदर
  </footer>
  <script>
    const scriptURL = 'https://script.google.com/macros/s/AKfycbyL5VUyINaVinfQfM1BvxJv7zJafBYxshYB7mN38cMzW7lVp_GXXvDvAOKbpfkqt_yT5Q/exec';
    const form = document.forms['supportForm'];
    const loader = document.getElementById('loader');
    form.addEventListener('submit', e => {
      e.preventDefault();
      loader.style.display = 'inline-block';
      fetch(scriptURL, { method: 'POST', body: new FormData(form) })
        .then(response => {
          loader.style.display = 'none';
          if (response.ok) {
            alert('Thank you! Your support has been recorded.');
            form.reset();
          } else {
            alert('Some error occurred, please try again.');
          }
        })
        .catch(error => {
          loader.style.display = 'none';
          alert('Network error: Please try again.');
          console.error('Error!', error.message);
        });
    });
  </script>
</body>
</html>
"""

# Display the HTML in Streamlit with scrolling enabled and enough height
components.html(html_code, height=1200, scrolling=True)
