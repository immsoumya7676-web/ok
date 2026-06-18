import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Aura AI",
    page_icon="✨",
    layout="wide"
)

# ================= THEME =================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#FFF9C4,#BBDEFB);
}

.main-title{
text-align:center;
font-size:55px;
font-weight:bold;
color:#0D47A1;
}

.subtitle{
text-align:center;
font-size:20px;
color:#1565C0;
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.1);
margin-bottom:15px;
}

section[data-testid="stSidebar"]{
background:#1565C0;
}

section[data-testid="stSidebar"] *{
color:white;
}

.stButton>button{
background:#FFD54F;
color:black;
font-weight:bold;
border-radius:12px;
border:none;
}

.stButton>button:hover{
background:#0D47A1;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.title("✨ Aura AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🤖 AI Chat",
        "📔 Mood Journal",
        "🔥 Burnout Detector",
        "📚 Study Planner",
        "🎯 Focus Mode",
        "🌿 Wellness Hub",
        "📈 Progress",
        "⚙️ Settings"
    ]
)

# ================= HOME =================

if page == "🏠 Home":

    st.markdown('<div class="main-title">✨ Aura AI</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">Your AI Companion for Wellness, Focus & Growth</div>',
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
        use_container_width=True
    )

    st.markdown("### 🌟 Features")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.info("🤖 AI Support Chat")

    with c2:
        st.info("📔 Mood Journal")

    with c3:
        st.info("🔥 Burnout Detection")

    c4,c5,c6 = st.columns(3)

    with c4:
        st.info("📚 Study Planner")

    with c5:
        st.info("🎯 Focus Mode")

    with c6:
        st.info("🌿 Wellness Hub")

# ================= DASHBOARD =================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("😊 Mood Score","8/10","+1")

    with col2:
        st.metric("🎯 Focus Score","84%","+6%")

    with col3:
        st.metric("📚 Study Hours","5.5","+1.2")

    st.success("Welcome back! You're doing great today.")

# ================= AI CHAT =================

elif page == "🤖 AI Chat":

    st.title("🤖 Aura AI Chat")

    message = st.text_input("Tell Aura AI how you feel")

    if message:

        if "stress" in message.lower():
            st.warning(
                "You seem stressed. Try taking a short break and deep breathing."
            )

        elif "sad" in message.lower():
            st.info(
                "It's okay to have difficult days. Consider journaling your thoughts."
            )

        else:
            st.success(
                "Thank you for sharing. Aura AI is here to support you."
            )

# ================= JOURNAL =================

elif page == "📔 Mood Journal":

    st.title("📔 Mood Journal")

    mood = st.selectbox(
        "Today's Mood",
        ["😊 Happy","😌 Calm","😐 Neutral","😔 Sad","😫 Stressed"]
    )

    note = st.text_area("Write your thoughts")

    if st.button("Save Journal Entry"):
        st.success("Journal Saved Successfully!")

# ================= BURNOUT =================

elif page == "🔥 Burnout Detector":

    st.title("🔥 Burnout Detector")

    stress = st.slider("Stress Level",1,10,5)

    sleep = st.slider("Sleep Hours",0,12,7)

    workload = st.slider("Workload Level",1,10,5)

    score = stress + workload - sleep

    if score >= 10:
        st.error("🔴 High Burnout Risk")

    elif score >= 5:
        st.warning("🟡 Moderate Burnout Risk")

    else:
        st.success("🟢 Low Burnout Risk")

# ================= STUDY =================

elif page == "📚 Study Planner":

    st.title("📚 Study Planner")

    subject = st.text_input("Subject")

    hours = st.number_input(
        "Planned Study Hours",
        min_value=0,
        max_value=24,
        value=2
    )

    if st.button("Add Goal"):
        st.success(
            f"{subject} added for {hours} hours."
        )

# ================= FOCUS =================

elif page == "🎯 Focus Mode":

    st.title("🎯 Focus Mode")

    timer = st.select_slider(
        "Focus Session",
        options=[15,20,25,30,45,60]
    )

    st.info(f"Pomodoro Session: {timer} Minutes")

    st.progress(75)

# ================= WELLNESS =================

elif page == "🌿 Wellness Hub":

    st.title("🌿 Wellness Hub")

    st.success("🫁 Breathing Exercise")

    st.success("🧘 Meditation")

    st.success("🌞 Positive Affirmations")

    st.success("🎵 Relaxing Music")

# ================= PROGRESS =================

elif page == "📈 Progress":

    st.title("📈 Weekly Progress")

    df = pd.DataFrame({
        "Mood":[5,6,7,8,8,9,8]
    })

    st.line_chart(df)

    st.write("Your mood has improved this week.")

# ================= SETTINGS =================

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    theme = st.selectbox(
        "Theme",
        [
            "Blue",
            "Yellow",
            "Ocean",
            "Lavender"
        ]
    )

    notifications = st.toggle("Enable Notifications")

    st.success("Preferences Saved")
