# Student Marks and Grade Calculator

<p align="center">
  <strong>Calculate Marks. Track Performance. Understand Grades.</strong>
  <br/>
  A beginner-friendly Python application that calculates student totals, percentages and grades based on subject marks.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Project-Beginner%20Friendly-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Category-Education-blue?style=for-the-badge" />
</p>

---

## Overview

The **Student Marks and Grade Calculator** is a simple Python command-line application designed to calculate student academic performance.

Users can enter a student's name and marks for four subjects. The application calculates the total marks, percentage and corresponding grade using predefined conditions.

It also validates subject marks to ensure that entered values remain within the accepted range of 0 to 100.

This project provides practical experience with fundamental Python programming concepts.

## Features

-  Accept student name
-  Input marks for four subjects
-  Calculate total marks
-  Calculate overall percentage
-  Assign grades based on percentage
-  Validate marks between 0 and 100
-  Simple command-line interface

## Technology

| Component | Technology |
|---|---|
| Programming Language | Python 3 |
| Interface | Command Line |
| Development | VS Code |

## How It Works

```text
       Start Application
               |
               ▼
        Enter Student Name
               |
               ▼
        Enter Subject Marks
               |
               ▼
         Validate Marks
               |
          ┌────┴────┐
          ▼         ▼
       Invalid     Valid
          |         |
          ▼         ▼
       Re-enter  Calculate Total
                    |
                    ▼
               Calculate %
                    |
                    ▼
               Assign Grade
                    |
                    ▼
              Display Result
                    |
                    ▼
                   End
```

## Getting Started

### Prerequisites

- Python 3 installed
- VS Code or another code editor
- Terminal or command prompt

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Student-Marks-Calculator
```

### 3. Run the Application

```bash
python main.py
```

Follow the instructions displayed in the terminal to enter student details and subject marks.

## Example Output

```text
================================
     STUDENT GRADE CALCULATOR
================================

Enter student name: Rahul

Enter marks for four subjects:

Subject 1: 85
Subject 2: 90
Subject 3: 78
Subject 4: 87

--------------------------------
Student Name : Rahul
Total Marks  : 340 / 400
Percentage   : 85%
Grade        : A
--------------------------------
```

*Example output assumes the grade thresholds configured in the application.*

## Python Concepts Practiced

- Variables and data types
- User input and type conversion
- Arithmetic operators
- Conditional statements
- Basic input validation
- Formatted output

## Future Improvements

- Support multiple students.
- Add subject-wise performance reports.
- Store student results in a file.
- Introduce a graphical user interface.
- Add class-level performance summaries.

## Project Objective

Build a practical understanding of Python fundamentals by developing a small application that performs calculations, processes user input and applies conditional logic.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong> Student Marks and Grade Calculator</strong>
  <br/>
  <em>Learning Python Through Practical Projects.</em>
  <br/><br/>
  Built with Python 3.
</p>
