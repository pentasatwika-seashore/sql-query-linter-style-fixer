from src.linter import lint_sql

def test_select_star():
    sql = "select * from employees"
    issues = lint_sql(sql)

    assert "SELECT * detected" in issues