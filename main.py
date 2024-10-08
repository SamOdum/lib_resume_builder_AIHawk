import os
import yaml
from pathlib import Path
from ai_cv_builder import FacadeManager, StyleManager, ResumeGenerator, Resume

# Load secrets
with open('secrets.yaml', 'r') as file:
    secrets = yaml.safe_load(file)
    
openai_api_key = secrets['openai_api_key']

style_manager = StyleManager()
resume_generator = ResumeGenerator()
with open('my_resume.yaml', 'r') as file:
    my_resume = file.read()
resume_object = Resume(my_resume)

# Create the output directory if it doesn't exist
output_dir = Path("data_folder/output")
output_dir.mkdir(parents=True, exist_ok=True)

resume_generator_manager = FacadeManager(openai_api_key, style_manager, resume_generator, resume_object, output_dir)
os.system('cls' if os.name == 'nt' else 'clear')
resume_generator_manager.choose_style()
os.system('cls' if os.name == 'nt' else 'clear')
        
# Generate resume
output_file = output_dir / "output_resume.html"
resume_generator_manager.resume_generator.create_resume(resume_generator_manager.selected_style_path, output_file)

print(f"Resume generated: {output_file}")

# Steps to run the script
# 1. python3 -m venv virtual
# 2. source virtual/bin/activate  
# 3. pip install -e .
# 4. python main.py
