# Expense Tracker

A simple command-line expense tracker made in Python for my Introduction to Problem Solving project. It lets you add, view, edit, and delete expenses, and keeps everything saved so you don't lose your data when you close the program.

## Project Description

This is a Python program that runs in the terminal (no GUI). It helps you keep track of how much money you're spending by letting you record expenses with an amount, date, and category, and then see totals and summaries based on that data.

## Features

- Add a new expense (amount, date, category)
- View all the expenses you've added, numbered in a list
- Edit an expense if you made a mistake
- Delete an expense you don't need anymore
- Export all your expenses to a CSV file so you can open it in Excel
- See a category summary showing how much you spent in each category and what percentage it is of your total spending
- Set a monthly budget and get warned if your spending goes over it

## How to Run It

1. Make sure Python is installed on your computer.
2. Open this folder in VS Code.
3. Open a terminal and run:

```
python main.py
```

4. A menu will show up. Type a number from 1 to 8 and press Enter to choose what you want to do.
5. Choose option 8 to exit the program.

## Files in This Project

- `main.py` — all the code for the project
- `expenses.json` — created automatically the first time you add an expense. This is where all your data is saved between runs.
- `expenses.csv` — created if you use the "Export to CSV" option.
- `README.md` — this file.

## How It Works (Basic Idea)

The program keeps all expenses in a Python list while it's running, where each expense is a dictionary with an amount, date, and category. Every time you add, edit, or delete something, the whole list gets saved to `expenses.json` using Python's built-in `json` module, so the data is still there the next time you open the program.

## What I Learned

While building this project I learned how to:

- Use `while` loops and `try`/`except` blocks to keep asking the user for input until it's valid
- Read and write data to a JSON file
- Break a program into separate functions instead of writing everything in one place
- Build a simple menu system that loops until the user chooses to exit

## Future Improvements

If I get more time later, I'd like to add:

- Searching expenses by date range
- A monthly report instead of just an overall summary
- Maybe a simple chart of spending using a library like matplotlib

## Author

[Your Name]
Semester 1, [Your Branch]
[Your College Name]
