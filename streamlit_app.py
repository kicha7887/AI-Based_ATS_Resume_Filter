import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI ATS Suite - Resume Tools",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui.styles import apply_custom_css
from utils.helpers import init_session_state
from ui.pages.home import render_home_page
from ui.pages.ats_checker import render_ats_checker
from ui.pages.resume_maker import render_resume_maker

apply_custom_css()
init_session_state()

# ================= MAIN APP ROUTER =================
def main():
    current_page = st.session_state.current_page
    
    if current_page == "home":
        render_home_page()
    elif current_page == "ats_checker":
        render_ats_checker()
    elif current_page == "resume_maker":
        render_resume_maker()
    else:
        render_home_page()


if __name__ == "__main__":
    main()
