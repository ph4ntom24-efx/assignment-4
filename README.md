File Handling in Python

This repository contains two Python programs that demonstrate basic file operations including reading, writing, appending, and error handling.

Programs

Task 1: File Reader with Error Handling 

A program that safely reads a text file and handles missing file errors gracefully.

Features:

· Opens and reads sample.txt line by line
· Displays formatted output with line numbers
· Gracefully handles FileNotFoundError
· Provides clear error messages

Expected Output:

· File exists:
  
  Reading file content:
  Line 1: This is a sample text file.
  Line 2: It contains multiple lines.
  
· File doesn't exist:
  
  Error: The file 'sample.txt' was not found.
  

Task 2: File Writer and Appender 

A program that demonstrates writing, appending, and reading file operations.

Features:

· Takes user input and writes to output.txt
· Appends additional user input to the same file
· Reads and displays the final file content
· Uses proper file modes (w, a, r)

Expected Output:


Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.


File Operations Demonstrated

· Reading: open(filename, "r") with read() or line iteration
· Writing: open(filename, "w") - creates new or overwrites existing
· Appending: open(filename, "a") - adds to existing content
· Error Handling: try-except blocks for FileNotFoundError

Key Python Concepts Used

· Context managers (with statement)
· File modes (r, w, a)
· Exception handling
· String formatting with f-strings
· User input with input()

Usage

1. Run file_reader.py to see file reading with error handling
2. Run file_writer.py to interactively write and append to files
3. Create sample.txt to test the reader program
4. Check generated output.txt after running the writer program

These programs demonstrate fundamental file I/O operations essential for Python programming.