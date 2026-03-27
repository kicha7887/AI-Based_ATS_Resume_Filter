def generate_ai_job_description(domain, role, experience, skills):

    jd = f"""
Job Title: {role}

Domain: {domain}

Experience Required: {experience}

Required Skills:
{skills}

Responsibilities:
• Develop and deploy solutions related to {domain}
• Work with cross-functional teams
• Design scalable systems
• Solve complex technical problems

Qualifications:
• Strong knowledge of {skills}
• Good problem solving ability
• Experience with real-world projects
"""

    return {"job_description": jd}