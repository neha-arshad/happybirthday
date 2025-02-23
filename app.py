import streamlit as st
from datetime import date
import random
import base64

st.title("🎉 Happy Birthday Calculator 🎉")
st.write("Enter your name and age to calculate your BirthYear and days left for your next Birthday!")

# Sidebar Theme Selection
st.sidebar.title("🎨 Choose Theme")
theme = st.sidebar.radio("Choose a Birthday Theme:", ["Classic", "Neon", "Eclipse Mode", "Bubblegum"])

# Apply Theme Styling
theme_styles = {
    "Neon": """
        <style>
            body, .stApp { 
                background-color: #00FFFF;
                color: #FF10F0;
                text-shadow: 0 0 5px #FF10F0, 0 0 10px #FF10F0, 0 0 20px #FF10F0;
            }
        </style>
    """,
    "Eclipse Mode": """
        <style>
            body, .stApp { 
                background-color: #121212;
                color: #FFD700;
                text-shadow: 0 0 5px #FFD700, 0 0 10px #FFD700, 0 0 20px #FFD700;
            }
        </style>
    """,
    "Bubblegum": """
        <style>
            body, .stApp { 
                background-color: pink;
                color: purple;
                text-shadow: 0 0 5px #800080, 0 0 10px #800080, 0 0 20px #800080;
            }
        </style>
    """,
}

if theme in theme_styles:
    st.markdown(theme_styles[theme], unsafe_allow_html=True);

#  User Input
name = st.text_input("Enter your name:");
if name:
	st.write("Hello", name);

age = st.number_input("Enter your age:", min_value=0, max_value=120);

if name and age:
    today = date.today();
    birth_year = today.year - age

    month = st.selectbox("Select your birth month:", list(range(1, 12)))
    day = st.selectbox("Select your birth day:", list(range(1, 30)))

    try:
        birthday = date(birth_year, month, day)

        # Calculate next birthday
        next_birthday = date(today.year, month, day)
        if today > next_birthday:
            next_birthday = date(today.year + 1, month, day)

        days_left = (next_birthday - today).days

        st.success(f"🎂 {name}, you were born in {birth_year} and you are {age} years old!")
        st.info(f"⏳ {days_left} days left for your next Birthday! 🥳")

        # Random Birthday Wishes
        wishes = [
            "🎊 Happy Birthday, {name}! May your cake be bigger than your problems! 🎂",
            "🎉 {name}, wishing you a day full of laughter, cake, and no diet rules! 🍰",
            "🎈 {name}, your birthday wish has been granted! You may eat all the cake today. 🥳"
        ]
        st.write(random.choice(wishes).format(name=name))

    except ValueError:
        st.error("❌ Invalid date! Please select a valid day for your birth month.")

# Upload Birthday Selfie
uploaded_file = st.file_uploader("Upload your Birthday Selfie! 📸", type=["jpg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="🎉 Your Birthday Selfie!", use_container_width=True)


# Blow the Candles Effect
if st.button("Blow the Candles 🕯"):
    st.write(f"🎉 Happy Birthday, {name}! 🎊")
    st.snow()
    st.balloons()



# Function to convert MP3 file to base64
def get_audio_base64(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode()

# Local MP3 File Path
mp3_file_path = "birthdaySong.mp3"

try:
    audio_base64 = get_audio_base64(mp3_file_path)
    music_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """
    st.markdown(music_html, unsafe_allow_html=True)
except:
    st.error("⚠️ Background music file not found! Please check the file path.")