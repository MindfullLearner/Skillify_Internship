# Student Performance Analyzer

## Project Overview

Student Performance Analyzer is a Python-based console application designed to manage student records and analyze their academic performance.

The application allows users to add student information, enter subject-wise marks, calculate total and average marks, assign grades, and determine performance levels. Student records are stored in a JSON file so that data remains available even after the program is closed.

## Features

- **Add Student:** Register students with their names and unique roll numbers.
- **Input Validation:** Prevent empty names, duplicate or invalid roll numbers, and marks outside the range of 0–100.
- **Performance Calculation:** Calculate total marks, average marks, grades, and performance levels.
- **Student Summary:** Display an individual student's academic summary.
- **Display All Students:** View all previously registered student records.
- **Data Persistence:** Save and load student records using a JSON file.
- **Exception Handling:** Handle invalid input, missing files, and corrupted JSON data.
- **Interactive Menu:** Navigate through the application's features using a menu-driven interface.

## Technologies Used

- Python
- JSON (Python standard library)
- Lists, tuples, and dictionaries
- Functions and loops
- File handling and exception handling

## Project Structure

```text
Student_Performance_Analyzer/
│
├── main.py
├── students.json
└── README.md
```

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this project.
3. Open the project folder in a terminal or code editor.
4. Run the following command:

```bash
python main.py
```

5. Follow the menu options displayed in the terminal.

## Grading Criteria

| Average Marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Performance Levels

| Average Marks | Performance |
|---|---|
| 90–100 | Excellent |
| 80–89.99 | Very Good |
| 70–79.99 | Good |
| 60–69.99 | Average |
| 50–59.99 | Below Average |
| Below 50 | Poor |

## Data Storage

Student records are stored in `students.json` in JSON format. The application loads existing records when it starts and updates the file when a new student is successfully added.

## Learning Outcomes

Through this project, I practiced:

- Working with Python lists, tuples, and dictionaries.
- Creating reusable functions.
- Using loops and conditional statements.
- Taking and validating user input.
- Reading and writing JSON files.
- Handling exceptions and invalid data.
- Organizing a program into separate functions.
- Building a menu-driven console application.

## Author

Developed as part of the Skillify Generative AI and Prompt Engineering Internship — Task 02.
