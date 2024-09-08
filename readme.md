# Math Proj SBW

This project is a Streamlit-based web application designed to help guide students in selecting the best academic path for high school, based on a series of questions about their interests and preferences.

## Features
- A multi-step question form to evaluate student preferences in various subjects such as mathematics, science, social studies, etc.
- Calculation of recommended academic streams based on weighted responses.
- Visualization of results through radar charts and grade comparisons.

## Installation

To run this project locally, you will need to install the required dependencies.

### Step 1: Set up a virtual environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows


Step 2: Install dependencies
pip install -r requirements.txt


Step 3: Install Watchdog (optional, for better performance)
pip install watchdog


Step 4: Run the application
streamlit run main.py


This will start the web application, and you can view it in your browser at:
http://localhost:8501

Project Structure

main.py - The entry point for the Streamlit web application.
utils/ - Contains utility files:
question_utils.py for question management.
chart_utils.py for visualization.
grade_utils.py for grade calculations.
Prompt/ - A directory containing fonts or any static files.
requirements.txt - A file containing the Python libraries required to run the project.
readme.md - This README file.
Usage

Navigate through the multi-step question form and answer the questions.
After completing the form, the system will recommend the best academic stream based on your responses.
Visual results will be presented in the form of radar charts and grade comparisons.
License

This project is licensed under the MIT License. See the LICENSE file for more details.

Troubleshooting

If you encounter any issues related to missing dependencies or performance, make sure you have followed the installation steps correctly, especially regarding the installation of Watchdog for performance on macOS.