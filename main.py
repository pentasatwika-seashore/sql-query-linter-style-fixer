from linter import lint_sql
from fixer import fix_sql

with open("../input/sample.sql", "r") as f:
    sql = f.read()

issues = lint_sql(sql)

print("Issues Found:")
for issue in issues:
    print("-", issue)

fixed_sql = fix_sql(sql)

with open("../output/sample_fixed.sql", "w") as f:
    f.write(fixed_sql)

print("Fixed SQL Generated Successfully!")
with open("../output/report.txt", "w") as report:
    report.write("SQL Lint Report\n")
    report.write("================\n")

    for issue in issues:
        report.write(issue + "\n")