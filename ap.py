# Simple Resume Matcher Module

def check_resume_match(resume_text, required_skills):
    resume_text = resume_text.lower()
    matched_skills = []
    
    for skill in required_skills:
        if skill.lower() in resume_text:
            matched_skills.append(skill)
            
    total_skills = len(required_skills)
    score = (len(matched_skills) / total_skills) * 100
    
    return score, matched_skills

if __name__ == "__main__":
    sample_resume = "I am a Software Engineer with skills in Python, Git, and SQL."
    skills_list = ["Python", "Git", "Docker", "SQL"]
    
    match_percentage, found = check_resume_match(sample_resume, skills_list)
    print(f"Match Score: {match_percentage}%")
    print(f"Matched Skills: {found}")