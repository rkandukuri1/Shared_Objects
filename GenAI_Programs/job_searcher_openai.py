import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# -------------------------------
# LOAD ENV
# -------------------------------
load_dotenv()

# -------------------------------
# CONFIG
# -------------------------------
API_URL = "https://jsearch.p.rapidapi.com/search"

HEADERS = {
    "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# -------------------------------
# BUILD SEARCH QUERY
# -------------------------------
def build_search_query(user_skills):
    skills = [s.strip() for s in user_skills.split(",") if s.strip()]

    if len(skills) >= 2:
        return f"{skills[0]} {skills[1]}"
    elif len(skills) == 1:
        return skills[0]
    else:
        return "software"


# -------------------------------
# FETCH JOBS
# -------------------------------
def fetch_jobs(user_skills, country):

    try:
        query = build_search_query(user_skills)

        params = {
            "query": query,
            "page": "1",
            "num_pages": "2",
            "country": country
        }

        response = requests.get(
            API_URL,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        print("STATUS:", response.status_code)
        print("QUERY:", query)

        data = response.json()

        return data.get("data", [])

    except Exception as e:
        st.error(f"Error fetching jobs: {e}")
        return []


# -------------------------------
# PROCESS SINGLE JOB
# -------------------------------
def process_job(job):

    posting_date = job.get("job_posted_at", "")

    # Convert ISO date into readable format
    try:
        if posting_date:
            dt = datetime.fromisoformat(posting_date.replace("Z", "+00:00"))
            display_date = dt.strftime("%d-%b-%Y %I:%M %p")
        else:
            display_date = "N/A"
    except:
        display_date = posting_date

    return {
        "title": job.get("job_title", ""),
        "posting_date": posting_date,      # Used for sorting
        "display_date": display_date,      # Used for display
        "company": job.get("employer_name", ""),
        "location": job.get("job_city", ""),
        "description": job.get("job_description", "")[:250] + "...",
        "apply_link": job.get("job_apply_link", "")
    }


# -------------------------------
# FIND JOBS
# -------------------------------
def find_jobs(user_skills, country):

    jobs = fetch_jobs(user_skills, country)

    # Keep only jobs with apply link
    jobs = [j for j in jobs if j.get("job_apply_link")]

    # Limit to first 8
    jobs = jobs[:8]

    results = []

    for job in jobs:
        results.append(process_job(job))

    # Sort by posting date (Ascending)
    results.sort(
        key=lambda x: (
            datetime.fromisoformat(
                x["posting_date"].replace("Z", "+00:00")
            ) if x["posting_date"] else datetime.max
        )
    )

    return results


# ======================================================
# STREAMLIT UI
# ======================================================

st.set_page_config(
    page_title="AI Job Search",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Search")

st.write("Find jobs based on your skills.")

skills = st.text_input(
    "Enter your skills (comma separated)",
    placeholder="Python, SQL, FastAPI"
)

country = st.selectbox(
    "Country",
    [
        "us",
        "in",
        "uk",
        "ca",
        "au"
    ]
)

if st.button("🔍 Search Jobs"):

    if not skills.strip():
        st.warning("Please enter at least one skill.")
        st.stop()

    with st.spinner("Searching jobs..."):

        jobs = find_jobs(skills, country)

    if not jobs:
        st.error("No jobs found.")

    else:

        st.success(f"Found {len(jobs)} jobs")

        for job in jobs:

            with st.container():

                st.subheader(job["title"])

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Company:** {job['company']}")
                    st.write(f"**Location:** {job['location']}")

                with col2:
                    st.write(f"**Posted:** {job['display_date']}")

                st.write(job["description"])

                st.link_button(
                    "Apply Now",
                    job["apply_link"]
                )

                st.divider()