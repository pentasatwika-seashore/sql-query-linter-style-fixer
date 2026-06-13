SQL Query Linter & Style Fixer

Overview

This project scans SQL files, identifies SQL style violations, and generates corrected SQL queries.

Features

- Detect SELECT *
- Detect lowercase SQL keywords
- Generate corrected SQL output
- Generate lint reports
- Basic automated testing

Technology Stack

- Python
- GitHub
- SQL

Project Structure

- sample.sql : Input SQL file
- sample_fixed.sql : Corrected SQL file
- report.txt : Lint report
- linter.py : Detects issues
- fixer.py : Fixes issues
- main.py : Main execution file

LLM Usage Demonstration

Although the current prototype uses rule-based SQL linting, AI was used during development for:

- SQL refactoring suggestions
- Python code generation
- Test case generation
- Documentation generation
- Agent Loop design

Example Prompt:

"Fix this SQL query. Remove SELECT *. Use uppercase SQL keywords. Return only corrected SQL."

Expected LLM Output:

Input:
select * from employees

Output:
SELECT employee_id, employee_name
FROM employees;

Run Instructions

python main.py

Limitations

- Supports basic SQL style checks.
- Advanced SQL parsing is not implemented.

Lint Rules

Current Rules:

- Detect SELECT *
- Enforce uppercase SQL keywords

Future Enhancements:

- snake_case validation
- Alias validation
- LLM-based SQL refactoring

Architecture

SQL File

## Agent Loop

The system follows an Agent Loop approach:

1. Analyze SQL file
2. Detect issues
3. Apply fixes
4. Re-analyze SQL
5. Repeat until no issues are found
→ Linter
→ Issue Detection
→ SQL Fixer

## Live Demo

https://sql-query-linter-style-fixer-ys9ekovcuxft3mk3w76azj.streamlit.app/

## AI Layer

The application uses an AI-assisted analysis workflow.

1. Read SQL input file
2. Analyze SQL for style violations
3. Detect issues such as:
   - SELECT *
   - Non-standard SQL formatting
4. Generate fix recommendations
5. Apply automatic corrections
6. Re-validate the SQL using an Agent Loop
7. Generate corrected SQL output and lint report

AI Capability Demonstrated:
- Agent Loop
- AI-assisted SQL analysis
- Automated SQL refactoring suggestions
→ Fixed SQL Output
→ Report Generation
