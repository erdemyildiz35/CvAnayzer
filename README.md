

CV Analyzer is a web application that analyzes uploaded CVs in PDF format and provides users with feedback on missing elements and areas for improvement. The project aims to enhance the quality of resumes using natural language processing and AI models.

Features
Upload and analyze CVs in PDF format

AI-powered content evaluation (using models like Mistral or OpenAI GPT)

Feedback on missing or improvable sections

Simple and user-friendly web interface

Option for offline use with local models


Technologies
Python (Flask / FastAPI)

OpenAI API or local Mistral model

pdfplumber or pdf-lib (for extracting text from PDFs)

HTML/CSS/JavaScript (Frontend)

Ollama (for managing local LLMs)

Installation and Usage
Clone the repository:

git clone https://github.com/yourusername/cv-analyzer.git
cd cv-analyzer


Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Configure your OpenAI API key or set up the local model:

Add OPENAI_API_KEY in a .env file

Or install and configure the Mistral model with Ollama


Run the application:

python app.py

Future Improvements
Support for multiple file formats (DOCX, TXT)

User registration and analysis history

More detailed analysis and personalized recommendations

Performance optimizations

License
MIT License





