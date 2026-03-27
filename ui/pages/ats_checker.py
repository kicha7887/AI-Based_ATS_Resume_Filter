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

def render_ats_checker():
    # Sidebar
    with st.sidebar:
        st.markdown('<p class="sidebar-title">⚙️ Job Configuration</p>', unsafe_allow_html=True)
        
        if st.button("🏠 Back to Home", use_container_width=True):
            navigate_to("home")
            st.rerun()
        
        st.markdown("---")
        
        domain = st.selectbox(
            "🏢 Select Domain",
            ["-- Select --"] + list(DOMAINS.keys()),
            help="Choose the job domain"
        )

        role = None
        if domain != "-- Select --":
            role = st.selectbox(
                "💼 Select Role",
                ["-- Select --"] + DOMAINS[domain],
                help="Choose the specific job role"
            )

        experience = st.selectbox(
            "📅 Experience Level",
            ["Fresher", "1-3 Years", "3-5 Years", "5+ Years"],
            help="Select required experience"
        )

        skills = st.text_input(
            "🛠️ Required Skills",
            "Python, Machine Learning, SQL",
            help="Enter comma-separated skills"
        )
        
        st.markdown("---")

        if role and role != "-- Select --":
            if st.button("✨ Generate Job Description", use_container_width=True):
                with st.spinner("🤖 AI is crafting your job description..."):
                    ai_job = generate_ai_job_description(
                        domain,
                        role,
                        experience,
                        skills
                    )
                    st.session_state.job_description = ai_job["job_description"]
                    st.rerun()
    
    # Main Content
    st.markdown("""
    <div class="main-header">
        <h1>🔍 ATS Resume Screening</h1>
        <p>AI-Powered Resume Analysis & Matching</p>
    </div>
    """, unsafe_allow_html=True)
    
    job_description = st.session_state.job_description
    
    if not job_description:
        st.markdown("""
        <div class="premium-card" style="text-align: center; padding: 4rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📋</div>
            <h2 style="color: white; margin-bottom: 1rem;">Generate a Job Description</h2>
            <p style="color: #a0a0b0; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Select a domain and role from the sidebar, then click "Generate Job Description" to begin the ATS screening process.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Job Description Section
        st.markdown("""
        <div class="premium-card">
            <div class="card-header">
                <div class="card-icon icon-purple">📄</div>
                <h3>Generated Job Description</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([5, 1])
        with col1:
            st.text_area(
                "",
                job_description,
                height=200,
                label_visibility="collapsed",
                key="jd_display"
            )
        with col2:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.job_description = None
                st.session_state.report_generated = False
                st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Resume Upload Section
        st.markdown("""
        <div class="premium-card">
            <div class="card-header">
                <div class="card-icon icon-blue">📤</div>
                <h3>Upload Resumes</h3>
            </div>
            <p style="color: #a0a0b0; margin-bottom: 1rem;">Upload PDF or DOCX files for analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        files = st.file_uploader(
            "Upload resumes",
            type=["pdf", "docx"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

        if files:
            st.info(f"📁 {len(files)} resume(s) uploaded and ready for analysis")

            if os.path.exists("resumes"):
                shutil.rmtree("resumes")

            os.makedirs("resumes")

            for f in files:
                with open(os.path.join("resumes", f.name), "wb") as out:
                    out.write(f.getbuffer())

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🚀 Generate ATS Report", use_container_width=True):
                    with st.spinner("🔍 Analyzing resumes with AI..."):
                        resumes = parse_resumes("resumes")

                        if not resumes:
                            st.error("❌ Could not extract text from resumes. Please check the file format.")
                            st.stop()

                        scores = match_resumes(resumes, job_description)

                        df = pd.DataFrame(
                            scores.items(),
                            columns=["Resume", "Score"]
                        ).sort_values("Score", ascending=False)

                        best_resume = df.iloc[0]["Resume"]
                        score = df.iloc[0]["Score"]

                        st.session_state.report_generated = True
                        st.session_state.score = score
                        st.session_state.best_resume = best_resume
                        st.session_state.df_results = df
                        st.session_state.metrics = calculate_ats_metrics(
                            resumes[best_resume],
                            job_description
                        )

                    shutil.rmtree("resumes")
                    st.rerun()

    # Results Section
    if st.session_state.report_generated:
        render_ats_results()


def render_ats_results():
    st.markdown("<br>", unsafe_allow_html=True)
    
    score = st.session_state.score
    status = "PASS" if score >= 85 else "FAIL"
    status_class = "status-pass" if status == "PASS" else "status-fail"
    
    st.markdown(f"""
    <div class="premium-card">
        <div class="card-header">
            <div class="card-icon icon-green">🏆</div>
            <h3>Analysis Results</h3>
            <span class="status-badge {status_class}" style="margin-left: auto;">{status}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: white; margin-bottom: 1rem; text-align: center;">Overall Match Score</h4>
        </div>
        """, unsafe_allow_html=True)
        
        color = "#38ef7d" if status == "PASS" else "#f45c43"
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            domain={'x': [0, 1], 'y': [0, 1]},
            number={'suffix': "%", 'font': {'size': 50, 'color': 'white'}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': 'white', 'tickfont': {'color': '#666'}},
                'bar': {'color': color},
                'bgcolor': 'rgba(255,255,255,0.1)',
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 50], 'color': 'rgba(244,92,67,0.2)'},
                    {'range': [50, 75], 'color': 'rgba(254,225,64,0.2)'},
                    {'range': [75, 100], 'color': 'rgba(56,239,125,0.2)'}
                ],
                'threshold': {
                    'line': {'color': color, 'width': 4},
                    'thickness': 0.75,
                    'value': score
                }
            }
        ))
        
        # Add glow effect by plotting multiple transparent thicker bars? Wait, Plotly doesn't support glowing directly in gauge easily. But the CSS has glow.
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=300,
            margin=dict(l=30, r=30, t=30, b=30)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 12px;">
            <p style="color: #a0a0b0; margin: 0;">Best Match</p>
            <p style="color: white; font-weight: 600; font-size: 1.1rem; margin: 0.5rem 0 0 0;">📄 {st.session_state.best_resume}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: white; margin-bottom: 1.5rem;">📊 ATS Metrics Breakdown</h4>
        </div>
        """, unsafe_allow_html=True)
        
        metrics = st.session_state.metrics
        
        for metric_name, value in metrics.items():
            progress_class = get_progress_class(value)
            st.markdown(f"""
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                    <span style="color: #e0e0e0; font-weight: 500;">{metric_name}</span>
                    <span style="color: {'#38ef7d' if value >= 70 else '#f5576c'}; font-weight: 600;">{value}%</span>
                </div>
                <div class="progress-container">
                    <div class="progress-bar {progress_class}" style="width: {value}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Resume Ranking Table
    st.markdown("""
    <div class="premium-card">
        <div class="card-header">
            <div class="card-icon icon-orange">📈</div>
            <h3>Resume Ranking</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = st.session_state.df_results
    
    def highlight_score(val):
        if val >= 85:
            return 'background-color: rgba(56, 239, 125, 0.3); color: #38ef7d'
        elif val >= 70:
            return 'background-color: rgba(79, 172, 254, 0.3); color: #4facfe'
        elif val >= 50:
            return 'background-color: rgba(254, 225, 64, 0.3); color: #fee140'
        return 'background-color: rgba(244, 92, 67, 0.3); color: #f45c43'
    
    styled_df = df.style.apply(lambda x: [highlight_score(v) for v in x] if x.name == 'Score' else ['' for _ in x])
    # The previous code used .applymap which is deprecated for Pandas 2.1+, but let's stick to .map if needed or .applymap
    st.dataframe(df.style.map(highlight_score, subset=['Score']), use_container_width=True, hide_index=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        csv = df.to_csv(index=False).encode()
        st.download_button(
            "📥 Download Full Report",
            csv,
            "ATS_Report.csv",
            "text/csv",
            use_container_width=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # AI Suggestions
    st.markdown("""
    <div class="premium-card">
        <div class="card-header">
            <div class="card-icon icon-purple">🧠</div>
            <h3>AI-Powered Insights</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.score >= 85:
        st.success("✅ Excellent! This resume is a strong match for the position.")
        
        st.markdown("""
        <div style="margin-top: 1rem;">
            <h4 style="color: #38ef7d; margin-bottom: 1rem;">💪 Key Strengths</h4>
            <div class="strength-item">✔️ Strong keyword alignment with job requirements</div>
            <div class="strength-item">✔️ High contextual similarity score</div>
            <div class="strength-item">✔️ ATS-optimized formatting detected</div>
            <div class="strength-item">✔️ Relevant skills and experience highlighted</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ This resume needs improvement to better match the job requirements.")
        
        st.markdown("""
        <div style="margin-top: 1rem;">
            <h4 style="color: #fee140; margin-bottom: 1rem;">💡 Improvement Suggestions</h4>
            <div class="suggestion-item">📝 Add more relevant technical keywords from the job description</div>
            <div class="suggestion-item">📊 Include quantifiable achievements and metrics</div>
            <div class="suggestion-item">🛠️ Highlight specific tools, frameworks, and technologies</div>
            <div class="suggestion-item">📋 Expand project descriptions with impact statements</div>
            <div class="suggestion-item">🎯 Better align resume sections with job requirements</div>
        </div>
        """, unsafe_allow_html=True)
