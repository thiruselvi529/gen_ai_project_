import streamlit as st
from modules.mood_detector import detect_mood
from modules.caption_generator import generate_caption
from modules.hashtag_generator import generate_hashtags

st.set_page_config(page_title="Social Mood Matcher", page_icon="😊")

st.title("😊 Social Mood Matcher")
st.subheader("AI Caption & Hashtag Generator")

st.write("Enter your post idea or mood to generate captions and hashtags.")

user_input = st.text_area("Enter your post idea")

if st.button("Generate Caption"):

    if user_input == "":
        st.warning("Please enter some text!")

    else:
        mood = detect_mood(user_input)

        caption = generate_caption(mood)
        hashtags = generate_hashtags(mood)

        st.success("Caption Generated!")

        st.subheader("Caption")
        st.write(caption)

        st.subheader("Hashtags")
        st.write(hashtags)