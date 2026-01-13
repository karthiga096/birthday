import streamlit as st
import random
import datetime

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="🎂 Birthday Wish for Munish",
    page_icon="🎉",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center; color: #FF4B4B;'>🎂 Daily Birthday Wish for Munish ❤️</h1>
    """, unsafe_allow_html=True
)

st.markdown("<p style='text-align: center; color: #FF6F61;'>ML-style wishes until Feb 4, 2026</p>", unsafe_allow_html=True)

# -----------------------------
# Training Data (Romantic Wishes)
# -----------------------------
training_text = """
Happy birthday Munish my love
Munish you are the best thing in my life
Every day with Munish feels magical
I am proud of everything Munish is
Munish inspires me to be better
Munish's smile makes my world brighter
I believe in Munish's dreams
Munish deserves endless happiness
I am always by Munish's side
My love for Munish grows every day
Munish is my forever
"""

# -----------------------------
# Markov Chain Model (ML Concept)
# -----------------------------
def train_model(text):
    words = text.split()
    model = {}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if word not in model:
            model[word] = []
        model[word].append(next_word)
    return model

def generate_message(model, length=18):
    word = random.choice(list(model.keys()))
    message = [word]
    for _ in range(length):
        word = random.choice(model.get(word, list(model.keys())))
        message.append(word)
    return " ".join(message)

# -----------------------------
# Dates
# -----------------------------
today = datetime.date.today()
birthday = datetime.date(2026, 2, 4)
days_left = (birthday - today).days

model = train_model(training_text)

# -----------------------------
# Special Birthday Message
# -----------------------------
special_birthday_message = """
<h3 style='color: #FF4B4B;'>🎉🎂 HAPPY BIRTHDAY MUNISH ❤️ 🎂🎉</h3>
<p style='color: #FF6F61; font-size: 18px;'>
Today is not just your birthday, it’s the day the world became brighter for me.<br>
Munish, you are my happiness, my strength, my dream, and my forever.<br>
May this year bring you success, health, and all the love you deserve.<br>
I will always stand by you 🤍
</p>
"""

# -----------------------------
# Display Wish
# -----------------------------
st.subheader("📅 Today's Wish")

if today == birthday:
    st.success("🎉 TODAY IS MUNISH'S BIRTHDAY 🎉")
    st.markdown(special_birthday_message, unsafe_allow_html=True)
else:
    wish = generate_message(model)
    st.info(f"❤️ {wish}")
    st.markdown(f"<p style='color: #FF4B4B;'>⏳ Days left until Feb 4, 2026: <b>{days_left} days</b></p>", unsafe_allow_html=True)

# -----------------------------
# Optional: Generate Extra Wish
# -----------------------------
st.divider()
st.subheader("🔮 Generate Another Wish")
if st.button("Generate New Wish"):
    st.write("💌", generate_message(model))
