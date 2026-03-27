import streamlit as st
from utils.helpers import navigate_to

def render_home_page():
    st.markdown("""
    <div class="main-header" style="text-align: center;">
        <h1>🎯 AI-Powered Career Suite</h1>
        <p>Professional Resume Tools with Advanced AI Technology</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="nav-button">
            <div class="nav-icon">🔍</div>
            <div class="nav-title">ATS Resume Checker</div>
            <div class="nav-desc">Analyze your resume against job descriptions with AI-powered ATS screening. Get detailed match scores and improvement suggestions.</div>
        </div>
        <br>
        """, unsafe_allow_html=True)
        if st.button("🔍 Open ATS Checker", use_container_width=True):
            navigate_to("ats_checker")
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="nav-button">
            <div class="nav-icon">📝</div>
            <div class="nav-title">Resume Maker</div>
            <div class="nav-desc">Create professional resumes with 4 premium templates. Input your details and generate ATS-optimized resumes instantly.</div>
        </div>
        <br>
        """, unsafe_allow_html=True)
        if st.button("📝 Open Resume Maker", use_container_width=True):
            navigate_to("resume_maker")
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="premium-card">
        <div class="card-header">
            <div class="card-icon icon-cyan">✨</div>
            <h3>Why Choose Our Platform?</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    features = [
        ("🤖", "AI-Powered", "Advanced NLP algorithms for accurate analysis"),
        ("📊", "Detailed Analytics", "Comprehensive scoring and metrics"),
        ("🎨", "Premium Templates", "4 professionally designed resume layouts"),
        ("⚡", "Instant Results", "Real-time feedback and suggestions")
    ]
    
    for col, (icon, title, desc) in zip([col1, col2, col3, col4], features):
        with col:
            st.markdown(f"""
            <div class="metric-card" style="height: 180px;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="color: white; font-weight: 600; font-size: 1rem; margin-bottom: 0.5rem;">{title}</div>
                <div style="color: #a0a0b0; font-size: 0.85rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
