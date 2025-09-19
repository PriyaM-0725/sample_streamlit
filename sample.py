import streamlit as st

# Page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="❤️",
    layout="centered"
)

# Title
st.title("Hi, I'm Mohana Priya 👋")

# About Section
st.header("About Me")
st.write("""
I am passionate about **Web Development** and **UI/UX Design**.  
I’ve completed internships in **front-end development** and enjoy building responsive, user-friendly digital experiences.  
Currently, I’m working on exciting projects that combine creativity and technology.
""")

# Project Section
st.header("My Project")
st.subheader("❤️ BeatAwareHeart")
st.write("""
BeatAwareHeart is a digital initiative designed to create awareness and provide insights into heart health.  
The project is live and accessible here:
""")
st.markdown("[Visit BeatAwareHeart 🚀](https://beatawareheart.netlify.app)", unsafe_allow_html=True)

