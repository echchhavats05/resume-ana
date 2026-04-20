print("App started...")

from flask import Flask, render_template, request
import PyPDF2
import re

app = Flask(__name__)


# 📄 Extract text from PDF
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text


# 🤖 Resume Analysis Logic
def analyze_resume(text):
    text_lower = text.lower()

    # 📊 Resume Score
    base_score = min(100, len(text) // 12)

    # 🎯 ATS Keywords
    ats_keywords = [
        "C","C++","python", "java", "sql", "HTML", "CSS","JavaScript","Node.js","machine learning",
        "data analysis", "communication", "teamwork",
        "leadership", "problem solving", "project"
    ]

    matched_keywords = [k for k in ats_keywords if k in text_lower]
    ats_score = int((len(matched_keywords) / len(ats_keywords)) * 100)

    missing_keywords = [k for k in ats_keywords if k not in text_lower]

    # 💡 Suggestions
    suggestions = []
    if ats_score < 50:
        suggestions.append("Improve keyword optimization for ATS")
    if "%" not in text:
        suggestions.append("Add quantified achievements (e.g., improved by 20%)")
    if len(text) < 800:
        suggestions.append("Add more detailed content")

    if not suggestions:
        suggestions.append("Well-optimized resume")

    # 💼 Role suggestion
    if "machine learning" in text_lower:
        role = "ML Engineer"
    elif "python" in text_lower:
        role = "Software Developer"
    elif "sql" in text_lower:
        role = "Data Analyst"
    else:
        role = "Fresher / Intern"

    result = f"""
Resume Score: {base_score}/100
ATS Score: {ats_score}/100

Matched Keywords:
{', '.join(matched_keywords)}

Missing Keywords:
{', '.join(missing_keywords[:5])}

Suggestions:
- """ + "\n- ".join(suggestions) + f"""

Suggested Role:
{role}
"""

    return result


# 🌐 Route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("resume")

        # ❌ No file
        if not file or file.filename == "":
            return render_template("index.html", error="⚠️ Please upload a file.")

        # ❌ File type
        if not file.filename.lower().endswith(".pdf"):
            return render_template("index.html", error="❌ Only PDF resumes are allowed.")

        try:
            text = extract_text(file)

            # ❌ Empty
            if not text or len(text.strip()) < 100:
                return render_template("index.html", error="⚠️ File is empty or unreadable.")

            text_lower = text.lower()

            # 🔍 Email
            email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

            # 🔍 Phone
            phone = re.findall(r"\+?\d[\d\s\-]{8,15}", text)

            # 🔍 Name detection
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            name = "Not detected"
            for line in lines[:10]:
                if len(line.split()) >= 2 and line.replace(" ", "").isalpha():
                    name = line
                    break

            # 📄 Section validation
            sections = ["education", "experience", "skills"]
            section_count = sum(1 for s in sections if s in text_lower)

            if section_count < 2:
                return render_template("index.html", error="⚠️ Missing key sections.")

            if len(text.split()) < 80:
                return render_template("index.html", error="⚠️ Resume too short.")

            # ✅ Analyze
            result = analyze_resume(text)

            return render_template(
                "result.html",
                result=result,
                name=name,
                email=email[0] if email else "Not found",
                phone=phone[0] if phone else "Not found"
            )

        except Exception:
            return render_template("index.html", error="❌ Invalid or corrupted PDF file.")

    return render_template("index.html")


# ▶️ Run app
if __name__ == "__main__":
 if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
