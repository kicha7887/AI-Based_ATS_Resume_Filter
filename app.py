from parser.resume_parser import parse_resumes
from matching.matcher import match_resumes

# Paths
RESUME_FOLDER = "resumes/"
JD_FILE = "job_description/jd.txt"

# Read job description
with open(JD_FILE, "r", encoding="utf-8") as file:
    job_description = file.read()

# Parse resumes
resumes = parse_resumes(RESUME_FOLDER)

# Match resumes with job description
scores = match_resumes(resumes, job_description)

# Rank resumes
ranked_resumes = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\n🔹 ATS Resume Ranking Results 🔹\n")
for rank, (name, score) in enumerate(ranked_resumes, start=1):
    print(f"{rank}. {name} → Match Score: {score}")
