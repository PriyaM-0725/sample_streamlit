import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Mohana Priya | Portfolio", page_icon="🌸", layout="wide")

# ---------- HEADER ----------
st.title("🌸 Mohana Priya")
st.subheader("Front-End Developer | UI/UX Enthusiast")

st.write(
    """
    Welcome to my Streamlit portfolio!  
    I'm passionate about **web development, UI/UX design, and creating meaningful digital experiences.**  
    Explore my projects and skills below 👇
    """
)

# ---------- ABOUT ME ----------
st.header("👩‍💻 About Me")
st.write(
    """
    I am a dedicated and enthusiastic developer with internship experience in 
    **Web Development and UI/UX Design**.  
    Skilled in building responsive web applications using **React.js, Next.js, and modern front-end technologies**.  
    Currently enhancing my knowledge in **AI and full-stack development**.
    """
)

# ---------- SKILLS ----------
st.header("⚡ Tech Stack")
cols = st.columns(3)
skills = [
    "React.js", "Next.js", "JavaScript", 
    "HTML5", "CSS3", "Tailwind CSS", 
    "UI/UX Design", "Figma", "Git & GitHub"
]

for i, skill in enumerate(skills):
    cols[i % 3].write(f"- {skill}")

# ---------- PROJECTS ----------
st.header("🚀 Projects")

st.markdown(
    """
    - [**BeatAware Heart**](https://beatawareheart.netlify.app/)  
      A digital health initiative that helps spread awareness about heart health through engaging visuals and resources.

    - [**Portfolio Website**](https://mohanapriyaportfolioweb.netlify.app/)  
      My personal portfolio built with Next.js and Tailwind CSS, showcasing my journey, skills, and achievements.
    """
)

# ---------- CONTACT ----------
st.header("📬 Get in Touch")
st.write("Let’s connect! Feel free to reach out:")

st.markdown(
    """
    - 📧 Email: **priyamoorthy0725@gmail.com**   
    - 🐙 [GitHub](https://github.com/PriyaM-0725)  
    """
)


