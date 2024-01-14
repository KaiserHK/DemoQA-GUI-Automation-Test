# DemoQA GUI Automation Test
This repository contains some example code and documentation for browser testing the DemoQA BookStore web application. The DemoQA BookStore is a small web app that is used by QA and Test Automation Engineers to practice and showcase their abilities. Here is the URL to the login page of the application: https://demoqa.com/login.

# Technologies
For this project, I chose to utilize Python (3.12.1) with the following modules:
- Selenium
- PyTest
- Requests

# How to Install and Run (Windows 10)
1. Install Python (I used Python 3.12.1 for this project)
2. Setup virtual environment by running "python -m venv {project root path}" in the command line
3. Activate the virtual environment by running "{path to venv folder}\Scripts\Activate"
4. Install the required modules by running "pip install {selenium/pytest/requests}" while the virtual environment is activated.
5. Clone/Download the code in this repo (I recommend storing the BookStoreApplicationTests folder right next to the virtual environment folder).
6. Navigate to the "/BookStoreApplicationTests/Tests/" folder in the command line.
7. Run a test file from the command line by running "pytest {testFileName}.py {options}".
