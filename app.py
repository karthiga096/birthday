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
# Custom CSS (Background, Colors, Cards)
# -----------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(to right, #FFF0F5, #FFE4E1);
}

/* Header */
h1 {
    text-align: center;
    color: black;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Caption */
p.caption {
    text-align: center;
    color: black;
    font-size: 18px;
}

/* Message cards */
div.stInfo, div.stSuccess {
    border-radius: 15px;
    padding: 20px;
    font-size: 18px;
    background-color: #FFF8F8;
    color: black !important;
}

div.stButton button {
    background-color: #FFB6C1;
    color: black;
    border-radius: 10px;
    padding: 8px 16px;
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
<h2 style='text-align:center; color:black;'>🎉 HAPPY BIRTHDAY MUNISH! 🎂❤️</h2>
<p style='text-align:center; color:black; font-size:20px;'>
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
    # Add random love emoji
    emojis = ["❤️","💖","💘","😍","🌹","💌","😘","💝"]
    emoji = random.choice(emojis)
    st.info(f"{emoji} {message} {emoji}")
    st.markdown(f"<p style='color:black;'>⏳ Days left until Feb 4, 2026: <b>{days_left} days</b></p>", unsafe_allow_html=True)

# -----------------------------
# Extra Features: Surprise Message & Daily Quote
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
    emoji = random.choice(emojis)
    st.write(f"{emoji} {random.choice(extra_messages)} {emoji}")

# Optional: Daily Quote
daily_quotes = [
    "“You are my today and all of my tomorrows.” – Leo Christopher",
    "“I fell in love with you because of all the little things you do.”",
    "“You are the finest, loveliest, tenderest, and most beautiful person I have ever known.”",
    "“Every love story is beautiful, but ours is my favorite.”",
    "“You are my heart, my life, my one and only thought.”"
]

st.divider()
st.subheader("💌 Daily Love Quote")
quote = random.choice(daily_quotes)
st.markdown(f"<p style='text-align:center; color:black; font-size:18px;'>{quote}</p>", unsafe_allow_html=True)
