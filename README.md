# Essay Evaluation System: HZSP (Hanyu Zuowen Shuiping Pingjia)

[中文](https://github.com/wd-github-2017/HZSP/blob/main/README_ZH.md) [日本語](https://github.com/wd-github-2017/HZSP/blob/main/README_JP.md)

This project demonstrates the working principles of a web-based essay evaluation system powered by large language models (LLMs).

## Features

- Minimalist codebase for ease of understanding core principles.
- Supports streaming output, providing real-time evaluation feedback.
- Utilizes the OpenAI SDK by default (can be easily adapted to other models, such as [DeepSeek](https://api-docs.deepseek.com/)). Local models are also supported; see [Transformers](https://huggingface.co/docs/transformers/index) for reference.
- Highly customizable evaluation criteria based on prompts (modifiable in `app.py`).
- Multilingual support for both frontend interface and output, compatible with a wide range of browsers.

## Instructions

1. Download the project to your local machine.
2. Install dependencies (it is recommended to use a newly-created environment with python=3.12):
   ```bash
   pip install -r requirements.txt
   ```
3. Add the OPENAI_API_KEY variable to your system environment variables and include your API key.
4. In the project directory, launch the Flask server:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000` in your browser.

## Usage Guide

1. Enter the essay to be evaluated in the left text box.
2. Click the "Execute Evaluation" button.
3. Wait for the evaluation results to be displayed in real time in the right text box.

## Notes

- A valid API key is required.
- It is recommended to access the system using major browsers such as Chrome, Edge, or Safari.