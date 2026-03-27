import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def init_session_state():
    defaults = {
        "current_page": "home",
        "job_description": None,
        "report_generated": False,
        "score": 0,
        "best_resume": None,
        "df_results": None,
        "metrics": None,
        "selected_template": 1,
        "resume_data": {
            "full_name": "",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "portfolio": "",
            "summary": "",
            "experiences": [],
            "education": [],
            "skills": [],
            "certifications": [],
            "projects": []
        }
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def calculate_ats_metrics(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()
    jd_words = set(re.findall(r"\b\w+\b", job_description))
    resume_words = re.findall(r"\b\w+\b", resume_text)
    keyword_pct = min(int(len(jd_words & set(resume_words)) / max(len(jd_words), 1) * 100), 100)
    tfidf = TfidfVectorizer().fit_transform([resume_text, job_description])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return {
        "Keyword Match": keyword_pct,
        "Skill Relevance": keyword_pct,
        "Context Similarity": int(similarity * 100),
        "Readability": 100 if len(resume_text) > 300 else 50
    }

def get_progress_class(value):
    if value >= 80:
        return "progress-excellent"
    elif value >= 60:
        return "progress-good"
    elif value >= 40:
        return "progress-average"
    return "progress-poor"

def navigate_to(page):
    st.session_state.current_page = page
