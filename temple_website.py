import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Temple Website", page_icon="🕉️", layout="wide")

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4caf50;
            color: white;
            text-align: center;
            padding: 1rem 0;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
        }
        .gallery img {
            background-size: cover;
            width: 300px;
            height: 100%;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        button {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            margin: 10px;
            margin-bottom: 90px;
        }
        button:hover {
            background-color: #45a049;
        }
        .popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            border: 2px solid #4caf50;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
        }
        .popup img {
            width: 100%;
            height: auto;
            max-width: 400px;
            border-radius: 8px;
        }
        .popup button {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 10px;
        }
        .popup button:hover {
            background-color: #45a049;
        }
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            z-index: 999;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to  Varala Varahi Gayatri Devi Temple Website 🕉️</h1>
    </header>
    <div class="content">
        <h2>వారాహి గాయత్రీ మంత్రం</h2>
        <p>ఓం మహిషధ్వజాయై విద్మహే
దండహస్తాయై ధీమహి
తన్నో వారాహి ప్రచోదయాత్ ||</p>
        <h2>Temple Gallery</h2>
        <div class="gallery">
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731824180/WhatsApp_Image_2024-11-15_at_09.32.32_f6373d2c_a1vodq.jpg" alt="Temple View 1" >
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823653/WhatsApp_Image_2024-11-04_at_10.26.12_3255f236_vabw9h.jpg" alt="Temple View 2">
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823652/WhatsApp_Image_2024-11-04_at_10.28.44_6b644b0b_q0u4jo.jpg" alt="Temple View 3">
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823654/WhatsApp_Image_2024-11-15_at_09.32.32_f18e77ee_cgrccr.jpg" alt="Temple View 4" >
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823652/WhatsApp_Image_2024-11-15_at_09.32.31_13b0cb46_vr1mmx.jpg" alt="Temple View 5">
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823653/WhatsApp_Image_2024-11-15_at_09.32.32_b03c0278_ulcctq.jpg" alt="Temple View 6">
            <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823654/WhatsApp_Image_2024-11-15_at_09.34.46_ad802429_rgihvk.jpg" alt="Temple View 6">
        </div>
        <h2>Support Our Temple</h2>
        <button onclick="openPopup()">Donate Now</button>
    </div>
    <div class="overlay" id="overlay" onclick="closePopup()"></div>
    <div class="popup d-flex flex-column justify-content-center" id="popup">
        <img src="https://res.cloudinary.com/dtqlzgvy3/image/upload/v1731823927/WhatsApp_Image_2024-11-15_at_09.34.45_456d030a_psczqq.jpg" alt="Thank You">
        <button onclick="closePopup()">Close</button>
    </div>
    <footer>
        <p>© 2024 Varala Varahi Gayatri Devi. All Rights Reserved.</p>
    </footer>
    <script>
        function openPopup() {
            document.getElementById('popup').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        }
        function closePopup() {
            document.getElementById('popup').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        }
    </script>
</body>
</html>
"""

# Embed the HTML into Streamlit
components.html(html_content, height=800, scrolling=True)
