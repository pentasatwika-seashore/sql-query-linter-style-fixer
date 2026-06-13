import streamlit as st

st.title("SQL Query Linter & Style Fixer")

st.info("AI-assisted SQL refactoring suggestions are documented in Prompt_Log.md. The project demonstrates an Agent Loop for SQL analysis and correction.")

sql = st.text_area("Enter SQL Query")

if st.button("Analyze"):

    issues = []

    if "select *" in sql.lower():
        issues.append("SELECT * detected")

    if "select" in sql:
        issues.append("SELECT should be uppercase")

    if "from" in sql:
        issues.append("FROM should be uppercase")

    if issues:
        st.error("\n".join(issues))
    else:
        st.success("No issues found!")
