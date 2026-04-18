
# 🚀 ResumeIQ – AI Resume Analyzer (ATS Powered)

ResumeIQ is a smart web application that analyzes resumes using ATS-based logic.  
It evaluates resumes based on structure, keywords, and content quality, providing actionable feedback.

---

## 🔍 Features

- 📄 Upload PDF resumes
- 🎯 Resume Score (content-based)
- 🤖 ATS Score (keyword matching)
- 🧠 Detects:
  - Name
  - Email
  - Phone number
- 📊 Matched & Missing Skills
- 💡 Smart Suggestions
- 💼 Suggested Job Role
- 📥 Download Analysis Report
- ⚠️ Invalid file detection (non-resume filtering)

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **PDF Processing:** PyPDF2
- **Logic:** Rule-based AI (heuristics + keyword matching)

---

## ⚙️ How It Works

The system simulates an **Applicant Tracking System (ATS)** using:

- Keyword matching from predefined skill sets
- Section detection (Education, Skills, Experience)
- Content-length based scoring
- Resume validation rules (email, phone, structure)

---

## 📂 Project Structure
resume-analyzer/
│
├── app.py
├── requirements.txt
├── templates/
│ ├── index.html
│ └── result.html

---

## ▶️ Run Locally

1. Clone the repository:
```bash
git clone https://github.com/echchhavats05/resume-analyzer-ats-powered.git
cd resume-analyzer-ats-powered
Install dependencies:
pip install -r requirements.txt
Run the app:

python app.py
Open in browser:

http://127.0.0.1:5000