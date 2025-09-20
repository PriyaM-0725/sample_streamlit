import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Mohana Priya | Portfolio", page_icon="🌸", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Title */
        .title {
            font-size: 42px !important;
            font-weight: 700;
            color: #6A0DAD;
            text-align: center;
        }

        /* Subtitle */
        .subtitle {
            font-size: 20px !important;
            color: #444;
            text-align: center;
            margin-bottom: 30px;
        }

        /* Card-like sections */
        .card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 25px;
        }

        /* Links */
        a {
            text-decoration: none;
            color: #6A0DAD;
            font-weight: 600;
        }
        a:hover {
            color: #E75480;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HEADER ----------
st.markdown("<h1 class='title'>🌸 Mohana Priya</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Front-End Developer | UI/UX Enthusiast</p>", unsafe_allow_html=True)

st.write(
    """
    Welcome to my Streamlit portfolio!  
    I’m passionate about **web development, UI/UX design, and creating meaningful digital experiences.**  
    Explore my journey and projects below 👇
    """
)

st.markdown("---")

# ---------- ABOUT ME ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("👩‍💻 About Me")
st.write(
    """
    I am a dedicated and enthusiastic developer with internship experience in 
    **Web Development and UI/UX Design**.  
    Skilled in building responsive web applications using **React.js, Next.js, and modern front-end technologies**.  
    Currently enhancing my knowledge in **AI and full-stack development**.
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- SKILLS ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("⚡ Tech Stack")

cols = st.columns(3)
skills = [
    "React.js", "Next.js", "JavaScript", 
    "HTML5", "CSS3", "Tailwind CSS", 
    "UI/UX Design", "Figma", "Git & GitHub"
]
for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"- {skill}")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- PROJECTS ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("🚀 Projects")

st.markdown(
    """
    - 🌐 [**BeatAware Heart**](https://beatawareheart.netlify.app/)  
      A digital health initiative that helps spread awareness about heart health through engaging visuals and resources.  

    - 💼 [**Portfolio Website**](https://mohanapriyaportfolioweb.netlify.app/)  
      My personal portfolio built with Next.js and Tailwind CSS, showcasing my journey, skills, and achievements.
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- CONTACT ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("📬 Get in Touch")
st.write("Let’s connect! Feel free to reach out:")

st.markdown(
    """
    - 📧 Email: **priyamoorthy0725@gmail.com**  
    - 🐙 [GitHub](https://github.com/PriyaM-0725)  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>✨ Built with ❤️ using Streamlit ✨</p>",
    unsafe_allow_html=True
)
