import streamlit as st
from PIL import Image

import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Varshii's Portfolio", layout="wide")

# --- Custom CSS for Dark Theme, Fonts, Layout Fix, Sidebar, Animations ---
st.markdown("""
    <style>
    /* === GLOBAL STYLES === */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Times New Roman', Times, serif !important;
        background-color: #121212 !important;
        color: #e0e0e0 !important;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    /* Remove padding and white space */
    /* Fix overlapping header */
.block-container {
    padding-top: 4rem !important;
}

/* Optional: Hide white Streamlit header */
header[data-testid="stHeader"] {
    background: transparent !important;
    position: relative !important;
    z-index: 0 !important;
}

    .main {
        padding-top: 0rem !important;
    }

    /* === HEADINGS === */
    h1, h2, h3, h4, h5, h6 {
        font-weight: bold !important;
        color: #00e5ff !important;
    }

    /* === SIDEBAR === */
    section[data-testid="stSidebar"] {
       background-color: white !important;
    color: #000000 !important;
    border-right: 1px solid #cccccc;
    }

    /* Fix radio button label colors in sidebar */
    section[data-testid="stSidebar"] .css-1v0mbdj,
    section[data-testid="stSidebar"] .css-10trblm {
        color: yellow !important;
        font-weight: bold;
    }

    /* === SCROLLBAR === */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #1e1e1e;
    }
    ::-webkit-scrollbar-thumb {
        background: #00e5ff;
        border-radius: 10px;
    }

    /* === BUTTONS === */
    .stButton button {
        background-color: #00bcd4;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background-color: #008caa;
        transform: scale(1.05);
    }

    /* === FORM INPUTS === */
    .stTextInput > div > input,
    .stTextArea textarea {
        background-color: #1c1c1c !important;
        color: #ffffff !important;
        border: 1px solid #00e5ff;
        border-radius: 8px;
    }

    .stTextInput > div > input:focus,
    .stTextArea textarea:focus {
        border: 1.5px solid #00e5ff;
        outline: none;
    }

    /* === FADE-IN ANIMATION === */
    .stMarkdown, .stHeader, .stSubheader, .stImage, .stDownloadButton, .stForm {
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar Navigation
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", [
    "About", "Professional Summary", "Experience", "Education", "Projects",
    "Certifications", "Extracurricular Activities", 
    "Languages", "Technical Skills", "Soft Skills", "Resume", "Contact"
])

# About Section
if menu == "About":
    st.title("👩‍💻 About Me")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/Profile.jpg", width=250)
    with col2:
        st.write("""
        
        Hi, I'm Varshini, a passionate data science student driven by curiosity and a love for solving real-world problems through data.

I specialize in Python, machine learning, and building interactive web applications. Whether it's analyzing complex datasets or designing user-friendly tools, I aim to bridge the gap between raw data and actionable insights.

I’ve developed projects like a life expectancy prediction model and a Django-based laundry management system, combining analytical thinking with full-stack development. I'm always exploring new technologies and thrive on turning ideas into impactful solutions.
        """)

# Professional Summary
elif menu == "Professional Summary":
    st.title("💼 Professional Summary")
    st.write("""
             
    - Passionate data science student with proficiency in Artificial Intelligence, Machine Learning, and data analysis. My experience includes full stack web development and Python-based projects. Deeply interested in Machine Learning, NLP, DevOps, and AWS. Eager to leverage my knowledge and skills to drive innovation and solve real-world problems in cutting-edge technologies.
    """)

# Experience Section
elif menu == "Experience":
    st.title("📊 Experience")

    st.subheader("Cloud Support Engineer (L1) Intern  | Hostup Cloud Technologies Pvt. Ltd")
    st.caption("June 2023 - July 2023")
    st.markdown("""
    •	Assisted with Level 1 cloud support operations, including monitoring services, resolving basic client issues, and documenting support activities to help maintain service reliability.
    """)

    st.subheader("Frontend Developer (Part-time)| Hostup Cloud Technologies Pvt. Ltd")
    st.caption("February 2024 - June 2024")
    st.markdown("""
   Designed and developed responsive user interfaces, enhancing user experience and optimizing frontend performance
    """)

# Education Section
elif menu == "Education":
    st.title("🎓 Education")

    # 1. MSc
    st.subheader("M.Sc. in Data Science")
    st.write("**CHRIST (Deemed to be University)** | Lavasa, Pune, India")
    st.caption("Aug 2023 – Feb 2025 (Pursuing)")
    st.markdown("""
    • Courses: Statistics, Mathematics, Python Programming, Full Stack Web Development,  
      Java Programming, Machine Learning, Deep Learning, Power BI, Regression Analysis.
    """)

   
    # 2. BCA
    st.subheader("B.C.A. in Data Analytics")
    st.write("**Kristu Jayanti College (Autonomous)** | Bengaluru, India")
    st.caption("Aug 2021 – May 2024")
    st.markdown("""
    • Gained strong foundation in Python, Big Data, Data Warehouse, Data Mining, NLP, DevOps, and Statistics.  
    • Learned database management, data analysis, statistical methods, and programming fundamentals.
    """)

   

    # 3. PUC
    st.subheader("PUC (Class 12) | PCMB")
    st.write("**SSES Independent Residential PU College** | India")
    st.caption("June 2019 – July 2021")

  

    # 4. SSLC
    st.subheader("SSLC (Class 10)")
    st.write("**Shanthi Children High School** | India")
    st.caption("2019")


# Projects Section
elif menu == "Projects":
    st.title("🛠️ Projects")

    # Project 1: Life Expectancy
    st.subheader("📊 Life Expectancy Prediction Using Multiple Linear Regression")
    st.markdown("""
    • Built a multiple linear regression model to predict life expectancy.  
    • Used health, economic, and demographic data as predictors.  
    • Analyzed key factors affecting life expectancy.  
    • Evaluated model performance using standard metrics (like RMSE, R²).
    """)
    # Optional GitHub & Docs
    st.markdown("[🔗 GitHub Repository](https://github.com/iamvarshinigowda/Regression-modeling.git))")
    with open("assets/Project_Report.pdf", "rb") as file:
        st.download_button("📄 Download Project Report", file, "Project_Report.pdf")

    st.markdown("---")

    # Project 2: Laundry Management System
    st.subheader("🧺 Campus Wash Point – Laundry Management System (Django) | 2025")
    st.markdown("""
    • Developed a Django website to automate college laundry operations.  
    • Implemented admin order tracking, user management, and email alerts for order readiness.  
    • Enforced weekly submission limits for users to streamline workloads.  
    • Managed CRUD operations and optimized the backend with Python and SQLite.
    """)
 
    st.markdown("[🔗 GitHub Repository](https://github.com/iamvarshinigowda/Campuswash.git)")
 


# Certifications
elif menu == "Certifications":
    st.title("📜 Certifications")

    st.subheader("• Python for Data Science – Elite Badge")
    st.write("NPTEL (IIT Madras), 2023")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1FNgcL32mpr9RfDSPD-93azn_SqyawBf3/view?usp=drivesdk)")  # replace with actual link or use st.image()

    st.subheader("• Process Mining Fundamentals")
    st.write("Celonis, 2022")
    st.markdown("[🔗 View Certificate](https://drive.google.com/drive/folders/11SkHZF7VG6DC1HUkiZFWOi4jGO8vM9GN?usp=drive_link)")

    st.subheader("• Introduction to MongoDB")
    st.write("MongoDB Inc., 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1D-OEc_VGa5Vo_Eal9p_xe1uk1QSuRbqD/view?usp=drivesdk)")


# Extracurricular Activities
elif menu == "Extracurricular Activities":
    st.title("🎯 Extracurricular Activities")

    st.markdown("""
    • 🥉 Secured 3rd prize while representing college in *Kalarava*, a state-level inter-collegiate cultural festival.  
    • 🎯 Finalist in Hackaverse Hackathon at Christ University, Lavasa, Pune.  
    • 🏐 Winner of college volleyball tournament, demonstrating strong teamwork and sportsmanship.  
    • 🏆 Secured 1st position in Power BI course final project presentation.
    """)


# Languages
elif menu == "Languages":
    st.title("🌐 Languages")

    st.markdown("""
    • **English** – Speak, Read, Write  
    • **Kannada** – Speak, Read, Write  
    • **Hindi** – Speak only  
    • **Tamil** – Speak only
    """)


# Technical Skills
elif menu == "Technical Skills":
    st.title("🧠 Technical Skills")

    st.markdown("""
    • **Programming & Scripting:** Python, HTML & CSS  
    • **Data Analysis & Visualization:** Power BI  
    • **Database Management:** SQL, MongoDB  
    • **Web Development:** Django  
    • **Version Control & Collaboration:** GitHub  
    • **Machine Learning:** Model building, data preprocessing, scikit-learn, etc.  
    • **Productivity Tools:** Microsoft Word, PowerPoint, Excel  
    • **Developer Tools:** VS Code
    """)


# Soft Skills
elif menu == "Soft Skills":
    st.title("🤝 Soft Skills")

    st.markdown("""
    • **Analytical Skills**  
    • **Adaptability**  
    • **Attention to Detail**  
    • **Problem Solving**
    """)


# Resume
elif menu == "Resume":
    st.title("📄 Resume")
    with open("assets/Resume.pdf", "rb") as file:
        st.download_button("⬇️ Download My Resume", file, "Resume.pdf")

elif menu == "Contact":
    st.title("📬 Contact Me")

    st.markdown("""

• 📧 **Email:** iamvarshinigowda@gmail.com  
• 📱 **Phone:** +91 7829358829  
• 🐙 **GitHub:** [github.com/iamvarshinigowda](https://github.com/iamvarshinigowda)
""")
