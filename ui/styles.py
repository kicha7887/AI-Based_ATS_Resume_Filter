import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }

    /* Streamlit UI elements are visible */

    /* Header */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102,126,234,0.3);
    }

    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }

    .main-header p {
        color: rgba(255,255,255,0.85);
        font-size: 1rem;
    }

    /* Cards */
    .premium-card {
        background: linear-gradient(145deg, #1e1e2f, #2d2d44);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 1.5rem;
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .card-header h3 {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0;
    }

    /* Icons inside cards */
    .card-icon {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    .icon-purple { background: linear-gradient(135deg, #667eea, #764ba2); }
    .icon-green { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .icon-blue { background: linear-gradient(135deg, #4facfe, #00f2fe); }
    .icon-orange { background: linear-gradient(135deg, #fa709a, #fee140); }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    .sidebar-title {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    /* Buttons */
    div.stButton > button, 
    button[data-testid="baseButton-secondary"], 
    button[data-testid="baseButton-primary"],
    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #667eea, #764ba2) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        display: inline-flex !important;
        justify-content: center !important;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4) !important;
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 100 !important;
    }

    div.stButton > button:hover, 
    button[data-testid="baseButton-secondary"]:hover, 
    button[data-testid="baseButton-primary"]:hover,
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102,126,234,0.6) !important;
    }

    /* Navigation Cards */
    .nav-button {
        background: #252540;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        border: 2px solid rgba(255,255,255,0.1);
        transition: 0.3s;
        height: 100%;
        cursor: pointer;
    }

    .nav-button:hover {
        transform: translateY(-8px);
        border-color: #667eea;
        box-shadow: 0 10px 25px rgba(102,126,234,0.2);
    }

    .nav-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }
    .nav-title {
        color: white;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .nav-desc {
        color: rgba(255,255,255,0.7);
        font-size: 0.95rem;
    }

    /* Metrics */
    .metric-card {
        background: #252540;
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    .metric-label {
        color: #a0a0b0;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }

    /* Progress Bar */
    .progress-container {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        height: 10px;
        margin-bottom: 1rem;
        overflow: hidden;
    }

    .progress-bar {
        height: 100%;
        border-radius: 10px;
    }

    .progress-excellent { background: #38ef7d; }
    .progress-good { background: #4facfe; }
    .progress-average { background: #f093fb; }
    .progress-poor { background: #f45c43; }

    /* Inputs */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox > div > div {
        background: #1a1a2e !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }

    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stTextInput label {
        color: #a0a0b0 !important;
        font-weight: 500;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #1e1e2f;
        border-radius: 16px;
        padding: 1rem;
        border: 2px dashed #667eea;
    }

    /* DataFrame */
    [data-testid="stDataFrame"] {
        background: #1e1e2f;
        border-radius: 12px;
        padding: 1rem;
    }

    /* Status Badges */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 30px;
        font-weight: 600;
        font-size: 1rem;
        color: white;
    }
    .status-pass {
        background: linear-gradient(90deg, #11998e, #38ef7d);
    }
    .status-fail {
        background: linear-gradient(90deg, #eb3349, #f45c43);
    }

    /* Suggestion cards */
    .suggestion-item {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-left: 3px solid #667eea;
        color: #e0e0e0;
    }
    .strength-item {
        background: rgba(56, 239, 125, 0.1);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-left: 3px solid #38ef7d;
        color: #e0e0e0;
    }

    /* Form sections */
    .form-section {
        background: linear-gradient(145deg, #1e1e2f 0%, #2d2d44 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .form-section-title {
        color: #667eea;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Resume Preview */
    .resume-preview-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        color: black;
        min-height: 800px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: #252540;
        border-radius: 10px;
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
        padding: 0.5rem 1rem;
    }

    .stTabs [aria-selected="true"] {
        background: #667eea;
    }

    /* Resume Templates Selector */
    .resume-template {
        background: #252540;
        border-radius: 16px;
        padding: 1rem;
        border: 2px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        height: 280px;
    }
    .resume-template:hover {
        border-color: #667eea;
    }
    .resume-template.selected {
        border-color: #38ef7d;
        box-shadow: 0 0 15px rgba(56, 239, 125, 0.2);
    }
    .template-preview {
        background: white;
        border-radius: 8px;
        height: 180px;
        margin-bottom: 0.75rem;
    }
    .template-name {
        color: white;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    
    </style>
    """, unsafe_allow_html=True)
