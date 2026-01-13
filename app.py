import streamlit as st
import random
import datetime

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="🎂 Daily Birthday Wish",
    page_icon="❤️",
    layout="centered"
)

st.title("🎂 Daily Birthday Wish Generator ❤️")
st.caption("ML-style wishes until Feb 4, 2026")

# -----------------------------
# Training Data (Romantic Wishes)
# -----------------------------
training_text = """
Happy birthday my love
You are the best thing in my life
Every day with you feels magical
I am proud of everything you are
You inspire me to be better
Your smile makes my world brighter
I believe in your dreams
You deserve endless happiness
I am always by your side
My love for you grows every day
You are my forever
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
🎉🎂 HAPPY BIRTHDAY MY LOVE ❤️ 🎂🎉

Today is not just your birthday,
it’s the day the world became brighter for me.

You are my happiness, my strength, my dream,
and my forever.

May this year bring you success, health,
and all the love you deserve.
I will always stand by you 🤍
"""

# -----------------------------
# Display Wish
# -----------------------------
st.subheader("📅 Today's Wish")

if today == birthday:
    st.success("🎉 TODAY IS HIS BIRTHDAY 🎉")
    st.markdown(special_birthday_message)
else:
    wish = generate_message(model)
    st.info(f"❤️ {wish}")
    st.write(f"⏳ Days left until Feb 4, 2026: **{days_left} days**")

# -----------------------------
# Optional: Generate Extra Wish
# -----------------------------
st.divider()
st.subheader("🔮 Generate Another Wish")
if st.button("Generate New Wish"):
    st.write("💌", generate_message(model))

