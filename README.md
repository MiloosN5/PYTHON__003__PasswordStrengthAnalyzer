# PYTHON__003__PasswordStrengthAnalyzer

## Project Overview 
- **name**: Password Strength Analyzer
- **type**: Console app
- **Live**: [❌]

## Preview

<img src="./previews/preview_1.png">

## Description 
- This project provides a simple console-based password strength analyzer. 
- It evaluates passwords against predefined security rules and allows the user to exit the program at any time by typing exit. 
- The analyzer gives detailed feedback — showing which criteria are met, which are missing, and the overall strength score of the password. 
- The application demonstrates practical password-checking logic while showcasing Python features like closures, loops, and built-in modules.

## Benefits
- The application helps users create stronger, more secure passwords by giving instant, structured feedback on their input. 
- Users can clearly see what aspects of their password need improvement and how strong it is overall. 
- Its modular design makes it easy to extend with new validation rules or scoring logic. 
- It’s lightweight, terminal-friendly, and showcases a clean, maintainable project structure — ideal for beginners aiming to adopt more advanced Python design principles.

## Tools & Techniques Used
- **Language**: Python (3.13)
- **Modules/libraries**:
    - **re** [*for regex-based password validation (uppercase, digits, special characters)*]
    - **rich** [*to enhance console output with colors and formatted text for better UX*]    
- **Control flow***
    - **for ... in** [```for item in passed:```]
    - **if/elif/else**
    - **break/continue**
    - **return**
- **Features***
    - **docstring** [```"""Basic validation: not empty, not only spaces."""```]
    - **closure**
    - **list comprehension** [```passed = [msg for rule, msg in rules if rule(password)]```]
    - **lambda** [```lambda p: len(p) >= 8```]    
- **Built-in Functions/Methods**
    - [```input(), len()```]
    - **str object** — [```lower()```] 
    - **re module** — [```search()```] 
- **External Functions**
    - **Console object (from ***rich***)** — [```print()```] 
- **Built-in/Custom Types**
    - **number** [```score = passedLength / total * 100```]
    - **class** [```class bool()```]
    - **def ***(functions)***** [```def strength_score(passedLength, total):```]
    - **sequence (list)** [```for item in passed:```]
- **Built-in variable**
    - ***__name__*** [```if __name__ == "__main__```]
  
## Running Locally
1. Clone the repository

   ```bash
   git clone https://github.com/MiloosN5/PYTHON__003__PasswordStrengthAnalyzer.git
   cd PYTHON__003__PasswordStrengthAnalyzer
   
2. Set Up a Virtual Environment (Optional) & Activate
    ```bash
    python -m venv venv # cross-platform, default Python version (whichever is first in PATH)
    # or
    py -3.12 -m venv venv # on Windows, specify exact Python version
    # then 
    venv\Scripts\activate # on Windows
    ```
3. Install Dependencies

   Before installing dependencies, make sure your virtual environment is activated (see step 2 from above)!
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Application
    ```
    python main.py
    ```
5. Enter the password in the console
6. There is a chance to try a new combination (until you type ```exit```)

***Additional:***

7. Update requirements.txt When You Add New Packages

    Whenever you install a new package (e.g. with pip install package-name), make sure to refresh your requirements.txt.

    Run this command to update the file:
    ```bash
        pip freeze > requirements.txt
    ```
8. Enjoy 😎!
