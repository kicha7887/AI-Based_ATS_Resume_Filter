# 🎯 AI-based ATS System - Resume Tools

Welcome to the **AI ATS System**, a modern, professional, and dark-themed Streamlit application tailored for job seekers and recruiters. This application serves as a comprehensive toolkit for building resumes and optimizing them for Applicant Tracking Systems (ATS).

## 🚀 Features

- **ATS Checker**: Evaluate resumes against job descriptions to determine an ATS match score. Highlights missing keywords and provides actionable feedback to optimize resumes to beat the ATS.
- **Resume Maker**: A powerful tool to create professional resumes from scratch, with dynamic fields and structured outputs.
- **Dark Theme UI**: A refined, custom-styled modular interface designed for a seamless, visually striking user experience.
- **Modular Architecture**: Well-structured repository built on best practices, separating UI pages, AI models, parsers, and matching logic.

## 🛠️ Tech Stack & Dependencies

The project is built fully in **Python** using [Streamlit](https://streamlit.io/) for the frontend interface.

Key dependencies include:
- `streamlit` - For building the interactive web app.
- `scikit-learn` & `nltk` - For Natural Language Processing (NLP) and AI-driven skill matching.
- `PyPDF2`, `pdfminer.six`, `python-docx` - For fast and effective document parsing (PDFs and Word documents).
- `plotly` - For generating beautiful data visualizations (e.g., matching scores).

## 📁 Project Structure

```
AI_ATS_Project/
├── ai_models/          # Core AI logic and models
├── matching/           # Job matching and keyword extraction engines
├── parser/             # Document parsers tailored for resumes (PDF/DOCX)
├── resumes/            # Stored/Output resumes
├── security/           # Application security logic
├── ui/                 # Frontend components and styling
│   ├── pages/          # Individual Streamlit pages (Home, ATS Checker, Resume Maker)
│   └── styles.py       # Custom dark theme and UI rendering logic
├── utils/              # Helper functions, session state configurations
├── requirements.txt    # Python dependencies
└── streamlit_app.py    # Main Streamlit application router and entry point
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd AI_ATS_Project
   ```

2. **Create and activate a virtual environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 🤝 Contribution

Feel free to fork this project, submit pull requests, or send suggestions. Whether it's enhancing the NLP models or adding new ATS-friendly resume templates, contributions are highly appreciated!
