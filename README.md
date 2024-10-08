# AI CV Builder

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Documentation](#documentation)
7. [Troubleshooting](#troubleshooting)
8. [How to Contribute](#how-to-contribute)
9. [License](#license)
10. [Disclaimer](#disclaimer)

## Introduction

`ai_cv_builder` is a Python library designed to simplify the creation of personalized, professional resumes. By integrating with GPT models, this library allows you to generate resumes tailored to specific job descriptions and formatted in various styles. It provides a flexible approach to resume building with minimal effort.

## Features

- **Dynamic Resume Styling:** Choose from pre-defined styles to create visually appealing resumes.
- **Job Description Integration:** Customize resumes based on job description URLs.
- **Flexible Configuration:** Set up resume details using YAML configuration files.
- **Interactive CLI:** Easily generate resumes via an interactive command-line interface.
- **AI-Powered Content:** Leverage GPT models to enhance resume content.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/SamOdum/ai_cv_builder.git
   cd ai_cv_builder
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `secrets.yaml` file in the root directory with your OpenAI API key:

   ```yaml
   openai_api_key: "your-api-key-here"
   ```

6. Create a `my_resume.yaml` file with your resume details (see documentation for format).

## Usage

To run the resume builder:

```bash
python main.py
```

This will:

1. Load your API key and resume data
2. Prompt you to choose a resume style
3. Generate a resume based on your data and chosen style
4. Save the output as an HTML file

## Dependencies

`ai_cv_builder` requires the following Python packages:

- langchain
- langchain-community
- langchain-core
- langchain-openai
- langchain-text-splitters
- langsmith
- openai
- regex==2024.7.24
- selenium==4.9.1
- webdriver-manager==4.0.2
- inquirer
- faiss-cpu

For a complete list with versions, see [requirements.txt](requirements.txt).

## Documentation

(Placeholder for detailed documentation of each module in the `ai_cv_builder` library)

## Troubleshooting

For issues:

- Open an issue on GitHub
- Join our [Telegram community](https://t.me/AICVBuilderCommunity) for support

## How to Contribute

We welcome contributions to `ai_cv_builder`! Here's how you can help:

### Web Designers

Enhance resume templates with improved visual design. [Learn more](how_to_contribute/web_designer.md).

### Prompt Engineers

Help refine prompts for better resume customization. [Learn more](how_to_contribute/prompt_engineer.md).

### Software Engineers

Submit pull requests to improve functionality or fix bugs. Follow [GitHub's guide on contributing to projects](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).

### Other Contributions

- Report issues
- Suggest new features
- Improve documentation

## Known Issues

### CSS Style Path Setting

There is a known issue with setting the CSS style path in [manager_facade.py](manager_facade.py) when using the package in different environments.
To handle both scenarios, the code include the code relevant to each environment. Comment out the code that is not relevant to your environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

`ai_cv_builder` is designed to assist with resume creation. While it aims to be helpful, the service may not cover all specific requirements for every job application. We assume no responsibility for the quality or accuracy of the generated resumes. Users should review and edit the output to ensure it meets their needs and accurately represents their qualifications.
