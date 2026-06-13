def lint_sql(sql):
    issues = []

    if "select *" in sql.lower():
        issues.append("SELECT * detected")

    if "select" in sql:
        issues.append("SELECT should be uppercase")

    if "from" in sql:
        issues.append("FROM should be uppercase")

    return issues