import fitz  # PyMuPDF
import json
import re

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume(resume_text):
    resume_dict = {}

    # Regex patterns adjusted based on the provided resume format
    resume_dict['Name'] = re.search(r'Name:\s*(.*)', resume_text).group(1) if re.search(r'Name:\s*(.*)', resume_text) else ''
    resume_dict['Location'] = re.search(r'Location:\s*(.*)', resume_text).group(1) if re.search(r'Location:\s*(.*)', resume_text) else ''
    resume_dict['Email'] = re.search(r'Email:\s*(.*)', resume_text).group(1) if re.search(r'Email:\s*(.*)', resume_text) else ''
    resume_dict['GitHub'] = re.search(r'GitHub:\s*(.*)', resume_text).group(1) if re.search(r'GitHub:\s*(.*)', resume_text) else ''
    resume_dict['LinkedIn'] = re.search(r'LinkedIn:\s*(.*)', resume_text).group(1) if re.search(r'LinkedIn:\s*(.*)', resume_text) else ''
    resume_dict['LeetCode'] = re.search(r'LeetCode:\s*(.*)', resume_text).group(1) if re.search(r'LeetCode:\s*(.*)', resume_text) else ''
    
    # Extracting Education
    education_match = re.search(r'Education\s*(.*?)(?=Experience|$)', resume_text, re.DOTALL)
    resume_dict['Education'] = education_match.group(1).strip() if education_match else ''
    
    # Extracting Experience
    experience_match = re.search(r'Experience\s*(.*?)(?=Projects|$)', resume_text, re.DOTALL)
    resume_dict['Experience'] = experience_match.group(1).strip() if experience_match else ''
    
    # Extracting Projects
    projects_match = re.search(r'Projects\s*(.*?)(?=Technical Skills|$)', resume_text, re.DOTALL)
    resume_dict['Projects'] = projects_match.group(1).strip() if projects_match else ''
    
    # Extracting Technical Skills
    technical_skills_match = re.search(r'Technical Skills\s*(.*?)(?=Achievements|$)', resume_text, re.DOTALL)
    resume_dict['Technical Skills'] = technical_skills_match.group(1).strip() if technical_skills_match else ''
    
    # Extracting Achievements
    achievements_match = re.search(r'Achievements\s*(.*)', resume_text, re.DOTALL)
    resume_dict['Achievements'] = achievements_match.group(1).strip() if achievements_match else ''

    return resume_dict

def main():
    pdf_path = 'resume.pdf'  # Replace with your PDF file path
    resume_text = extract_text_from_pdf(pdf_path)
    resume_json = parse_resume(resume_text)
    
    with open('resume.json', 'w') as json_file:
        json.dump(resume_json, json_file, indent=4)
        
    print("Resume parsed and saved as JSON.")

if __name__ == "__main__":
    main()
