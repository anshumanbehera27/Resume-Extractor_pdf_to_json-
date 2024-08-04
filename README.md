# Resume Parser

## Overview

This Python script extracts text from a PDF resume and parses the content into a structured JSON format. It handles specific sections such as Education, Experience, Projects, Technical Skills, and Achievements. This tool is useful for converting resumes into a machine-readable format for further processing.

## Features

- **Text Extraction**: Extracts text from a PDF resume using PyMuPDF.
- **Data Parsing**: Converts the extracted text into a structured JSON format.
- **Handles Key Sections**: Includes parsing for Name, Location, Email, GitHub, LinkedIn, LeetCode, Education, Experience, Projects, Technical Skills, and Achievements.

## Requirements

- Python 3.x
- PyMuPDF (`fitz` package)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-parser.git
   ```
2. Navigate to the project directory:
```
cd resume-parser
```
3. Install the required packages:

```
pip install pymupdf
```
---
### Usage
- Place your PDF resume in the project directory and rename it to resume.pdf. Alternatively, modify the pdf_path variable in script.py to point to your resume file.
## Run the script:

```
python script.py
```
-The script will parse the resume and save the output in resume.json
