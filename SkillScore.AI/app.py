import streamlit as st
import pandas as pd
import plotly.express as px
from utils import evaluate_skills, get_roadmap

# Page config
st.set_page_config(page_title="SkillScore.AI", layout="centered")

# Title and intro
st.title("🎯 SkillScore.AI")
st.markdown("Assess your skills and get a custom roadmap based on your confidence levels.")

# State flag for showing the form later
show_form = True

# Initialize name and submitted flag
name = ""
submitted = False

# Process form submission
with st.form("skill_form"):
    name = st.text_input("Enter your name (required):")

    st.markdown("### Rate your confidence (0 = No knowledge, 10 = Expert)")
    skills = {
        "Python": st.slider("Python", 0, 10, 5),
        "HTML/CSS": st.slider("HTML/CSS", 0, 10, 5),
        "JavaScript": st.slider("JavaScript", 0, 10, 5),
        "Data Science": st.slider("Data Science", 0, 10, 5),
        "Machine Learning": st.slider("Machine Learning", 0, 10, 5),
        "Web Development": st.slider("Web Development", 0, 10, 5),
        "SQL": st.slider("SQL", 0, 10, 5),
    }

    submitted = st.form_submit_button("Generate Report")

if submitted:
    if not name.strip():
        st.error("❌ Please enter your name before generating the report.")
    else:
        show_form = False  # Hide the form after generating

        score, strengths, roadmap = evaluate_skills(skills)

        # Skill Score
        st.markdown(f"### 🔍 Skill Strength Score: **{score}/100**")
        st.markdown(f"### ✅ Strong Areas: {', '.join(strengths) if strengths else 'None'}")

        # Radar Chart
        df = pd.DataFrame({
            "Skill": list(skills.keys()),
            "Confidence": list(skills.values())
        })

        fig = px.line_polar(df, r='Confidence', theta='Skill', line_close=True)
        fig.update_traces(fill='toself')
        st.plotly_chart(fig)

        # Enhanced Roadmap Output
        st.markdown("### 🗺️ Personalized Roadmap")
        st.write(roadmap)

# Show form again only if name was not submitted
if show_form:
    st.markdown("---")
    st.info("👆 Fill the form above to generate your personalized skill report.")
