# Student Grade Book

A command-line student grade management application built with Python.

## Features
- Add students with name and class
- Add grades on a 1-6 scale with validation
- View all grades for a specific student
- Calculate average grade per student
- View all registered students
- Data persists between sessions using CSV file storage

## Concepts used
- Object Oriented Programming (2 classes: GradeBook, Student)
- File I/O with CSV serialization using DictWriter/DictReader
- Exception handling (ZeroDivisionError for empty grade lists)
- *args for flexible method arguments
- Generator expressions for grade formatting
- Helper method pattern (find_student used throughout)

## How to run
python grade_book.py

## Grade scale
| Grade | Meaning |
|-------|---------|
| 6 | Excellent |
| 5 | Very Good |
| 4 | Good |
| 3 | Satisfactory |
| 2 | Sufficient |
| 1 | Fail |

## Menu options
| Option | Description |
|--------|-------------|
| 1 | Add a new student |
| 2 | Add a grade to a student |
| 3 | View a student's grades |
| 4 | View a student's average grade |
| 5 | View all students |
| 6 | Save and quit |
