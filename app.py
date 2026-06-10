import streamlit as st
import sqlite3
import pandas as pd
from modules.report_gen import ReportGenerator


st.set_page_config(
    page_title="AI Proctoring Dashboard",
    layout="wide"
)

st.title("🎓 AI Proctoring Dashboard")

# -------------------
# Database Connection
# -------------------

conn = sqlite3.connect("alerts.db")

query = """
SELECT *
FROM alerts
ORDER BY id DESC
"""

df = pd.read_sql_query(
    query,
    conn
)

# -------------------
# Metrics
# -------------------

total_alerts = len(df)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Violations",
        total_alerts
    )

with col2:
    st.metric(
        "Screenshots Captured",
        total_alerts
    )

st.divider()

# -------------------
# Alert History
# -------------------

st.subheader("Violation History")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# -------------------
# Generate PDF Report
# -------------------

st.subheader("Generate Report")

if st.button("Generate PDF Report"):

    report = ReportGenerator()

    path = report.generate_report()

    st.success(
        f"Report Generated: {path}"
    )