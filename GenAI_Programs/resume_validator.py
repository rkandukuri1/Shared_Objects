import streamlit as st
from pydantic import BaseModel, Field
from openai import OpenAI
import os
from dotenv import load_dotenv
import docx2txt

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ResumeValidation(BaseModel):
    match_score: int = Field(ge=0, le=100)
    matched_skills: list[str]
    missing_skills: list[str]
    experience_match: str
    strengths: list[str]
    improvement_suggestions: list[str]
    final_recommendation: str

def validate_resume(resume_text: str, requirement_text: str):
    prompt = f""" You are an expert resume validator.

Validate the resume against the requirement.

- Penalize missing required skills
- Same input must produce nearly same score every time
- Be strict and objective

Provide:
    - match_score
    - matched_skills
    - missing_skills
    - strengths
    - suggestions
    - experience_match
    - final_resolution

Hiring status:
    Consider = 75+
    WaitList = 50-74
    Reject = below 50

Match score must be between 0 and 100.
At the end provide hiring status like:
Status : Consider / WaitList / Reject

JOB REQUIREMENT: {requirement_text}
RESUME: {resume_text}
"""
    response = client.beta.chat.completions.parse(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format=ResumeValidation,
    )

    return response.choices[0].message.parsed

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="AI Resume Validator", layout="wide")

st.title("AI Resume Validator")

st.sidebar.write("Upload Resume (Word) and Requirement (Text)")
resume_file = st.sidebar.file_uploader("Upload Resume (.docx)", type=["docx"])
req_file = st.sidebar.file_uploader("Upload Requirement (.txt)", type=["txt"])

if st.sidebar.button("Validate Resume"):

    if resume_file and req_file:

        with st.sidebar.spinner("Analyzing resume..."):

            resume_text = docx2txt.process(resume_file)
            requirement_text = req_file.read().decode("utf-8")
            result = validate_resume(resume_text, requirement_text)

        st.sidebar.success("Analysis Complete!")

        # -----------------------------
        # Display Results
        # -----------------------------

        st.subheader("Match Score")
        st.progress(result.match_score / 100)
        st.sidebar.metric("Overall Match Score", f"{result.match_score}/100")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Skills")
            for skill in result.matched_skills:
                st.write(f"- {skill}")

            st.subheader("Strengths")
            for s in result.strengths:
                st.write(f"- {s}")

        with col2:
            st.subheader("Missing Skills")
            for skill in result.missing_skills:
                st.write(f"- {skill}")

            st.subheader("Improvement Suggestions")
            for s in result.improvement_suggestions:
                st.write(f"- {s}")

        st.subheader("Experience Evaluation")
        st.info(result.experience_match)

        st.subheader("Final Recommendation")
        st.success(result.final_recommendation)

    else:
        st.warning("Please upload both resume and requirement files.")
