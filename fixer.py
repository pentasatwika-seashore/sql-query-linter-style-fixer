def fix_sql(sql):
    sql = sql.replace("select", "SELECT")
    sql = sql.replace("from", "FROM")
    sql = sql.replace("*", "employee_id, employee_name")

    return sql