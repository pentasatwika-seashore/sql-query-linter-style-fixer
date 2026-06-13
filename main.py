from linter import lint_sql
from fixer import fix_sql

with open("../input/sample.sql", "r") as f:
    sql = f.read()

for attempt in range(3):

    issues = lint_sql(sql)

    if not issues:
        print("No issues found!")
        break

    print(f"\nAttempt {attempt + 1}")
    print("Issues Found:")

    for issue in issues:
        print("-", issue)

    sql = fix_sql(sql)

with open("../output/sample_fixed.sql", "w") as f:
    f.write(sql)

with open("../output/report.txt", "w") as report:
    report.write("SQL Lint Report\n")
    report.write("================\n")

    final_issues = lint_sql(sql)

    if not final_issues:
        report.write("All issues fixed.\n")
    else:
        for issue in final_issues:
            report.write(issue + "\n")

print("Fixed SQL Generated Successfully!")
