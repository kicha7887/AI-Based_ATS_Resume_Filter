import streamlit as st
import os
import shutil
import pandas as pd
import plotly.graph_objects as go
from parser.resume_parser import parse_resumes
from matching.matcher import match_resumes
from ai_models.ai_job_model import generate_ai_job_description
from utils.helpers import calculate_ats_metrics, get_progress_class, navigate_to
from utils.config import DOMAINS

# ================= PAGE: RESUME MAKER =================
def render_resume_maker():
    # Sidebar
    with st.sidebar:
        st.markdown('<p class="sidebar-title">📝 Resume Maker</p>', unsafe_allow_html=True)
        
        if st.button("🏠 Back to Home", use_container_width=True):
            navigate_to("home")
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 🎨 Select Template")
        
        template_options = {
            1: "Modern Professional",
            2: "Minimalist Elegant",
            3: "Creative Bold",
            4: "Executive Classic"
        }
        
        selected = st.radio(
            "Choose a template style:",
            options=list(template_options.keys()),
            format_func=lambda x: template_options[x],
            index=st.session_state.selected_template - 1,
            label_visibility="collapsed"
        )
        st.session_state.selected_template = selected
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.8rem;">
            <p>💡 Tip: Fill in all sections for best ATS compatibility</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Content
    st.markdown("""
    <div class="main-header">
        <h1>📝 AI Resume Maker</h1>
        <p>Create Professional ATS-Optimized Resumes</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Template Preview and Form
    col_form, col_preview = st.columns([1, 1], gap="large")
    
    with col_form:
        st.markdown("""
        <div class="premium-card">
            <div class="card-header">
                <div class="card-icon icon-blue">✏️</div>
                <h3>Enter Your Details</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Personal Information
        st.markdown('<div class="form-section-title">👤 Personal Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *", value=st.session_state.resume_data["full_name"], placeholder="Enter Your Full Name")
            email = st.text_input("Email *", value=st.session_state.resume_data["email"], placeholder="Enter Your Email")
            phone = st.text_input("Phone", value=st.session_state.resume_data["phone"], placeholder="Enter Your Phone Number")
        with col2:
            location = st.text_input("Location", value=st.session_state.resume_data["location"], placeholder="Enter Your Location")
            linkedin = st.text_input("LinkedIn", value=st.session_state.resume_data["linkedin"], placeholder="Enter Your LinkedIn Profile URL")
            portfolio = st.text_input("Portfolio/Website", value=st.session_state.resume_data["portfolio"], placeholder="Enter Your Portfolio URL")
        
        # Update session state
        st.session_state.resume_data["full_name"] = full_name
        st.session_state.resume_data["email"] = email
        st.session_state.resume_data["phone"] = phone
        st.session_state.resume_data["location"] = location
        st.session_state.resume_data["linkedin"] = linkedin
        st.session_state.resume_data["portfolio"] = portfolio
        
        st.markdown("---")
        
        # Professional Summary
        st.markdown('<div class="form-section-title">📋 Professional Summary</div>', unsafe_allow_html=True)
        summary = st.text_area(
            "Write a brief professional summary",
            value=st.session_state.resume_data["summary"],
            placeholder="Write your role summary",
            height=100
        )
        st.session_state.resume_data["summary"] = summary
        
        st.markdown("---")
        
        # Experience
        st.markdown('<div class="form-section-title">💼 Work Experience</div>', unsafe_allow_html=True)
        
        num_exp = st.number_input("Number of experiences", min_value=0, max_value=5, value=len(st.session_state.resume_data["experiences"]))
        
        experiences = []
        for i in range(int(num_exp)):
            with st.expander(f"Experience {i+1}", expanded=i==0):
                col1, col2 = st.columns(2)
                with col1:
                    exp_title = st.text_input(f"Job Title", key=f"exp_title_{i}", 
                                             value=st.session_state.resume_data["experiences"][i]["title"] if i < len(st.session_state.resume_data["experiences"]) else "")
                    exp_company = st.text_input(f"Company", key=f"exp_company_{i}",
                                               value=st.session_state.resume_data["experiences"][i]["company"] if i < len(st.session_state.resume_data["experiences"]) else "")
                with col2:
                    exp_duration = st.text_input(f"Duration", key=f"exp_duration_{i}", placeholder="Jan 2020 - Present",
                                                value=st.session_state.resume_data["experiences"][i]["duration"] if i < len(st.session_state.resume_data["experiences"]) else "")
                exp_desc = st.text_area(f"Description", key=f"exp_desc_{i}", height=80,
                                       value=st.session_state.resume_data["experiences"][i]["description"] if i < len(st.session_state.resume_data["experiences"]) else "")
                experiences.append({"title": exp_title, "company": exp_company, "duration": exp_duration, "description": exp_desc})
        
        st.session_state.resume_data["experiences"] = experiences
        
        st.markdown("---")
        
        # Education
        st.markdown('<div class="form-section-title">🎓 Education</div>', unsafe_allow_html=True)
        
        num_edu = st.number_input("Number of education entries", min_value=0, max_value=3, value=len(st.session_state.resume_data["education"]))
        
        education = []
        for i in range(int(num_edu)):
            with st.expander(f"Education {i+1}", expanded=i==0):
                col1, col2 = st.columns(2)
                with col1:
                    edu_degree = st.text_input(f"Degree/Certificate", key=f"edu_degree_{i}",
                                              value=st.session_state.resume_data["education"][i]["degree"] if i < len(st.session_state.resume_data["education"]) else "")
                    edu_inst = st.text_input(f"Institution", key=f"edu_inst_{i}",
                                            value=st.session_state.resume_data["education"][i]["institution"] if i < len(st.session_state.resume_data["education"]) else "")
                with col2:
                    edu_year = st.text_input(f"Year", key=f"edu_year_{i}", placeholder="2020",
                                            value=st.session_state.resume_data["education"][i]["year"] if i < len(st.session_state.resume_data["education"]) else "")
                education.append({"degree": edu_degree, "institution": edu_inst, "year": edu_year})
        
        st.session_state.resume_data["education"] = education
        
        st.markdown("---")
        
        # Skills
        st.markdown('<div class="form-section-title">🛠️ Skills</div>', unsafe_allow_html=True)
        skills_input = st.text_input(
            "Enter skills (comma-separated)",
            value=", ".join(st.session_state.resume_data["skills"]),
            placeholder="Python, JavaScript, Machine Learning, Data Analysis"
        )
        st.session_state.resume_data["skills"] = [s.strip() for s in skills_input.split(",") if s.strip()]
        
        st.markdown("---")
        
        # Projects
        st.markdown('<div class="form-section-title">🚀 Projects</div>', unsafe_allow_html=True)
        
        num_proj = st.number_input("Number of projects", min_value=0, max_value=4, value=len(st.session_state.resume_data["projects"]))
        
        projects = []
        for i in range(int(num_proj)):
            with st.expander(f"Project {i+1}", expanded=i==0):
                proj_name = st.text_input(f"Project Name", key=f"proj_name_{i}",
                                         value=st.session_state.resume_data["projects"][i]["name"] if i < len(st.session_state.resume_data["projects"]) else "")
                proj_desc = st.text_area(f"Description", key=f"proj_desc_{i}", height=60,
                                        value=st.session_state.resume_data["projects"][i]["description"] if i < len(st.session_state.resume_data["projects"]) else "")
                projects.append({"name": proj_name, "description": proj_desc})
        
        st.session_state.resume_data["projects"] = projects
        
        st.markdown("---")
        
        # Certifications
        st.markdown('<div class="form-section-title">🏆 Certifications</div>', unsafe_allow_html=True)
        certs_input = st.text_input(
            "Enter certifications (comma-separated)",
            value=", ".join(st.session_state.resume_data["certifications"]),
            placeholder="AWS Certified, Google Cloud Professional, PMP"
        )
        st.session_state.resume_data["certifications"] = [c.strip() for c in certs_input.split(",") if c.strip()]
    
    with col_preview:
        st.markdown("""
        <div class="premium-card">
            <div class="card-header">
                <div class="card-icon icon-green">👁️</div>
                <h3>Live Preview</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        from ui.resume_templates import generate_template_1, generate_template_2, generate_template_3, generate_template_4
        # Generate preview based on selected template
        template_generators = {
            1: generate_template_1,
            2: generate_template_2,
            3: generate_template_3,
            4: generate_template_4
        }
        
        resume_html = template_generators[st.session_state.selected_template](st.session_state.resume_data)
        
        # Preview container
        st.markdown(f"""
        <div class="resume-preview-container" style="max-height: 800px; overflow-y: auto;">
            {resume_html}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Download Section
        col1, col2 = st.columns(2)
        with col1:
            # Download as HTML
            html_download = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>{st.session_state.resume_data['full_name']} - Resume</title>
            </head>
            <body>
                {resume_html}
            </body>
            </html>
            """
            st.download_button(
                "📄 Download HTML",
                html_download,
                f"{st.session_state.resume_data['full_name'].replace(' ', '_') or 'resume'}_resume.html",
                "text/html",
                use_container_width=True
            )
        
        with col2:
            st.info("💡 Open HTML in browser and print to PDF for best results")
