import streamlit as st
import datetime

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="❤️ Birthday Wishes for Munish",
    page_icon="🎉",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align:center; color:#FF4B4B;'>Daily Love Wish for Munish ❤️</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#FF6F61;'>A heartfelt message every day until Feb 4, 2026</p>",
    unsafe_allow_html=True
)

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
    # ... add more messages up to Feb 4, 2026
]

# -----------------------------
# Feb 4 Special Birthday Message
# -----------------------------
special_birthday_message = """
<h2 style='color:#FF4B4B;'>🎉 HAPPY BIRTHDAY MUNISH! 🎂❤️</h2>
<p style='color:#FF6F61; font-size:18px;'>
Today is YOUR special day, my love! 💖<br>
Munish, you are my everything, my reason to smile, my heart's home.<br>
May this year bring you endless joy, love, and all your dreams come true.<br>
I promise to make every moment with you unforgettable. 🤍<br>
I love you more than words can ever express. ❤️
</p>
"""

# -----------------------------
# Today’s Date
# -----------------------------
today = datetime.date.today()
birthday = datetime.date(2026, 2, 4)
days_left = (birthday - today).days

# -----------------------------
# Display Wish
# -----------------------------
st.subheader("📅 Today's Wish")

if today == birthday:
    st.success("🎉 TODAY IS MUNISH'S BIRTHDAY! 🎉")
    st.markdown(special_birthday_message, unsafe_allow_html=True)
else:
    # Pick a daily message (cycle through list)
    index = (today - datetime.date(today.year, 1, 1)).days % len(daily_messages)
    message = daily_messages[index]
    st.info(f"💌 {message}")
    st.markdown(f"<p style='color:#FF4B4B;'>⏳ Days left until Feb 4, 2026: <b>{days_left} days</b></p>", unsafe_allow_html=True)

# -----------------------------
# Optional: Show Another Message
# -----------------------------
st.divider()
st.subheader("🔮 Surprise Another Message")
if st.button("Generate Extra Message"):
    import random
    extra_messages = [
        "Thinking of you always makes me smile, Munish. ❤️",
        "Every heartbeat whispers your name, my love. 💖",
        "You are my sunshine on every cloudy day. ☀️",
        "Munish, you are my forever favorite. 💕",
        "Love you endlessly, today and always. 🌹"
    ]
    st.write("💌", random.choice(extra_messages))
