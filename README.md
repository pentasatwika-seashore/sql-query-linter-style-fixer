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

Run Instructions

python main.py

Limitations

- Supports basic SQL style checks.
- Advanced SQL parsing is not implemented.
