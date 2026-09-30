# Project Statement: Smart Expense Tracker

Student: Mathew Mayank
Registration Number: 26BEC10054
Course: Introduction to Problem Solving
Project Type: VITyarthi - Build Your Own Project

---

## 1. Problem Statement

Students and young earners often spend money in many small transactions (food, travel, bills, shopping) and rarely record them. Without a record, it is hard to know where money is going, whether a monthly budget is being followed, or which category is causing overspending. Paper notes and memory are unreliable, and general-purpose spreadsheets need manual formulas and do not warn the user when a budget is about to be crossed.

This project solves the problem by building a simple, offline, menu-driven **Expense Tracker** in Python. It lets a user record every expense in seconds, keeps the data safely on disk, compares spending with a monthly budget, and produces clear summaries so that better spending decisions can be made.

## 2. Scope of the Project

### In scope
- A console (command-line) application written in Python 3.
- Recording, viewing, searching, updating and deleting expenses (CRUD).
- Fixed expense categories: Food, Travel, Bills, Shopping, Health, Education, Other.
- Setting a monthly budget and checking how much of it has been used, with warnings at 80% and 100%.
- Reports: category-wise totals, monthly summary, highest-spending category and average daily spend.
- Persistent storage using JSON files, and export of expenses to CSV.
- Input validation, error handling and activity logging.
- Unit tests for the core modules.
- Application of problem-solving concepts: problem decomposition, algorithm design, flowcharts, pseudocode, and use of lists, dictionaries, sorting and searching.

### Out of scope
- Graphical or web interface, and mobile apps.
- Multi-user accounts, login and cloud synchronisation.
- Bank or UPI integration and automatic transaction import.
- Multi-currency support (all amounts are in Indian Rupees).

## 3. Target Users

- College students managing a monthly allowance.
- First-time earners and interns who want to build a budgeting habit.
- Anyone who needs a lightweight, offline tool that does not require an internet connection or an account.
- Instructors and evaluators who want to see a clear application of basic problem-solving techniques.

## 4. High-Level Features

| # | Module | Feature |
|---|--------|---------|
| 1 | Expense Management | Add, view, update and delete expenses; search and filter by category, date range or keyword |
| 2 | Budget Management | Set a monthly budget; view budget used and remaining; automatic warnings at 80% and 100% |
| 3 | Reports and Analytics | Category-wise totals with percentages, monthly summary, top spending category, average daily spend |
| 4 | Data Persistence | Automatic saving to JSON files; CSV export |
| 5 | Validation and Logging | Checks for amount, date, category and text; errors handled without crashing; actions written to a log file |

## 5. Expected Outcome

A working, well-structured Python project hosted on GitHub with clean modules, tests, documentation and a detailed project report, demonstrating that a real-world everyday problem can be broken down, designed and solved step by step.
