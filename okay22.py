import streamlit as st

st.set_page_config(
    page_title="Aura AI",
    page_icon="💜",
    layout="wide"
)

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigate",
    [
        "Home",
        "Dashboard",
        "AI Chat",
        "Mood Journal",
        "Burnout Detector",
        "Study Balance",
        "Focus Mode",
        "Wellness Hub",
        "Progress Insights",
        "Settings"
    ]
)

# HOME
if page == "Home":
    st.title("💜 Aura AI")
    st.subheader("Your Safe Space. Your Growth Partner.")
    st.write("AI-powered wellness and study companion.")

# DASHBOARD
elif page == "Dashboard":
    st.title("📊 Dashboard")
    mood = st.slider("Today's Mood", 1, 10, 5)
    st.progress(mood/10)
    st.metric("Focus Score", "82%")
    st.metric("Study Hours", "4.5")

# AI CHAT
elif page == "AI Chat":
    st.title("🤖 Aura AI Chat")
    msg = st.text_input("Tell me how you feel")
    if msg:
        st.success("Thank you for sharing. Aura AI suggests taking small positive steps today.")

# MOOD JOURNAL
elif page == "Mood Journal":
    st.title("📔 Mood Journal")
    mood = st.selectbox("Mood", ["Happy","Calm","Stressed","Sad","Excited"])
    note = st.text_area("Write your thoughts")
    if st.button("Save Entry"):
        st.success("Journal saved successfully.")

# BURNOUT DETECTOR
elif page == "Burnout Detector":
    st.title("🔥 Burnout Detector")
    stress = st.slider("Stress Level",1,10,5)
    sleep = st.slider("Sleep Hours",0,12,7)

    if stress > 7:
        st.error("High Burnout Risk")
    else:
        st.success("Burnout Risk Low")

# STUDY BALANCE
elif page == "Study Balance":
    st.title("📚 Study Balance Hub")
    study = st.number_input("Study Hours",0,24,4)
    exercise = st.number_input("Exercise Hours",0,10,1)

    st.write(f"Study: {study} hrs")
    st.write(f"Exercise: {exercise} hrs")

# FOCUS MODE
elif page == "Focus Mode":
    st.title("🎯 Focus Mode")
    st.info("Pomodoro Session")
    minutes = st.slider("Session Length",15,60,25)
    st.write(f"{minutes} minute focus session")

# WELLNESS HUB
elif page == "Wellness Hub":
    st.title("🌿 Wellness Hub")
    st.write("Breathing Exercise")
    st.write("Meditation")
    st.write("Positive Affirmations")

# PROGRESS INSIGHTS
elif page == "Progress Insights":
    st.title("📈 Progress Insights")

    data = {
        "Mood":[5,6,7,8,7,8,9]
    }

    st.line_chart(data)

# SETTINGS
elif page == "Settings":
    st.title("⚙️ Settings")

    theme = st.selectbox(
        "Theme",
        ["Lavender","Ocean","Mint","Sunset","Dark"]
    )

    st.success(f"{theme} Theme Selected")
