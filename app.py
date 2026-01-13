import streamlit as st
import base64

# -----------------------------
# Paths to your images on your PC
# Example: "C:/Users/YourName/Pictures/left.png"
# -----------------------------
left_image_path = ""d:\Users\Admin\Pictures\WhatsApp Image 2025-02-18 at 5.44.32 PM.jpeg""   # replace with your path
right_image_path = ""d:\Users\Admin\Pictures\WhatsApp Image 2025-02-18 at 5.44.32 PM.jpeg"" # replace with your path

# Function to convert local image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Convert images
left_base64 = image_to_base64(left_image_path)
right_base64 = image_to_base64(right_image_path)

# Add CSS to show images in corners
st.markdown(f"""
<style>
#left-corner {{
    position: fixed;
    top: 0;
    left: 0;
    width: 150px;
    height: 150px;
    background-image: url("data:image/png;base64,{left_base64}");
    background-size: contain;
    background-repeat: no-repeat;
    z-index: 0;
}}

#right-corner {{
    position: fixed;
    top: 0;
    right: 0;
    width: 150px;
    height: 150px;
    background-image: url("data:image/png;base64,{right_base64}");
    background-size: contain;
    background-repeat: no-repeat;
    z-index: 0;
}}

.stApp > * {{
    position: relative;
    z-index: 1;
}}
</style>

<div id="left-corner"></div>
<div id="right-corner"></div>
""", unsafe_allow_html=True)








import streamlit as st
import datetime
import random

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="❤️ Birthday Wishes for Munish",
    page_icon="🎉",
    layout="centered"
)

# -----------------------------
# Custom CSS for Background & Black Text
# -----------------------------
st.markdown("""
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(to right, #FFF5EE, #FFE4C4);  /* Light, warm colors for contrast */
    color: black; /* Default text color */
}

/* Header */
h1, h2, p, div.stInfo, div.stSuccess {
    color: black !important;
}

/* Header */
h1 {
    text-align: center;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Caption */
p.caption {
    text-align: center;
    font-size: 18px;
}

/* Message boxes */
div.stInfo, div.stSuccess {
    border-radius: 15px;
    padding: 20px;
    font-size: 18px;
    background-color: #FFF8F0;  /* Slightly off-white for visibility */
    color: black !important;
}

/* Button */
div.stButton button {
    background-color: #FFB6C1;
    color: black;
    border-radius: 10px;
    padding: 8px 16px;
    font-weight: bold;
}

/* Surprise message */
.surprise {
    color: black;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<h1>Daily Love Wish for Munish ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p class='caption'>A heartfelt message every day until Feb 4, 2026</p>", unsafe_allow_html=True)

# -----------------------------
# Pre-written Daily Messages
# -----------------------------
daily_messages = [
    "Good morning, Munish! 🌞 Just a reminder: You are the most special part of my life.",
    "Hey love, thinking of you makes my day brighter. ❤️",
    "Munish, your smile is my favorite thing in the world. 😘",
    "Every moment with you is magical. Love you endlessly! 💖",
    "Munish, you are my dream come true. I cherish you always.",
    "Hey sweetheart, your love completes me. 🌹",
    "Every day I love you more than yesterday. 💕",
    "Munish, you are my heart and soul. Never forget that. ❤️",
    "Hey love, your laughter is my favorite melody. 🎶",
    "You are my strength and happiness, Munish. I adore you.",
]

# -----------------------------
# Special Birthday Message
# -----------------------------
special_birthday_message = """
<h2 style='text-align:center;'>🎉 HAPPY BIRTHDAY MUNISH! 🎂❤️</h2>
<p style='text-align:center; font-size:20px;'>
Today is YOUR special day, my love! 💖<br>
Munish, you are my everything, my reason to smile, my heart's home.<br>
May this year bring you endless joy, love, and all your dreams come true.<br>
I promise to make every moment with you unforgettable. 🤍<br>
I love you more than words can ever express. ❤️
</p>
"""

# -----------------------------
# Today's Date
# -----------------------------
today = datetime.date.today()
birthday = datetime.date(2026, 2, 4)
days_left = (birthday - today).days

# -----------------------------
# Display Today's Wish
# -----------------------------
st.subheader("📅 Today's Wish")

if today == birthday:
    st.success("🎉 TODAY IS MUNISH'S BIRTHDAY! 🎉")
    st.markdown(special_birthday_message, unsafe_allow_html=True)
else:
    # Cycle through messages daily
    index = (today - datetime.date(today.year, 1, 1)).days % len(daily_messages)
    message = daily_messages[index]
    st.info(f"{message}")
    st.markdown(f"<p style='color:black; font-weight:bold;'>⏳ Days left until Feb 4, 2026: <b>{days_left} days</b></p>", unsafe_allow_html=True)

# -----------------------------
# Extra Surprise Message
# -----------------------------
st.divider()
st.subheader("🔮 Surprise Another Message")
if st.button("Generate Extra Message"):
    extra_messages = [
        "Thinking of you always makes me smile, Munish. ❤️",
        "Every heartbeat whispers your name, my love. 💖",
        "You are my sunshine on every cloudy day. ☀️",
        "Munish, you are my forever favorite. 💕",
        "Love you endlessly, today and always. 🌹"
    ]
    surprise_message = random.choice(extra_messages)
    st.markdown(f"<p class='surprise'>{surprise_message}</p>", unsafe_allow_html=True)
