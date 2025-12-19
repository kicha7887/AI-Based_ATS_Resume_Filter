# AI-Based ATS Resume Filtering System

An AI-based Applicant Tracking System (ATS) that compares resumes with predefined, role-specific job descriptions using Natural Language Processing (NLP). The system provides ATS scores, pass/fail status, and interactive visual dashboards through a Streamlit web application.

---

## 🚀 Features

- Domain-based job selection (Data Science, Software, Cloud, Cybersecurity, Web)
- Role-based predefined job descriptions
- Resume-to-job-description comparison using NLP
- ATS score generation with PASS / FAIL logic (≥85% = PASS)
- Encrypted resume storage for security
- Supports PDF and DOCX resumes
- Interactive dashboard with charts (Donut, Bar, Progress)
- Streamlit-based web interface

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit
- **Backend:** Python
- **NLP:** TF-IDF, Cosine Similarity (scikit-learn)
- **Visualization:** Plotly
- **Security:** Cryptography (Fernet Encryption)
- **Document Parsing:** pdfminer.six, python-docx

---

## 📂 Project Structure
AI_ATS_Project/

│
├── streamlit_app.py
├── parser/
│ └── resume_parser.py
├── matching/
│ └── matcher.py
├── security/
│ └── encryption.py
├── job_descriptions/
│ ├── Data_Science/
│ ├── Software_Development/
│ ├── Cloud_DevOps/
│ ├── Cybersecurity/
│ └── Web_Development/
├── resumes/
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository (cmd)
git clone https://github.com/kicha7887/AI-Based_ATS_Resume_Filter
cd AI_ATS_Resume_Filter

### 2️⃣ Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate   # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### ▶️ Run the Application
streamlit run streamlit_app.py
