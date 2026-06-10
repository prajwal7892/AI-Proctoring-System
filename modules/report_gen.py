from fpdf import FPDF
import sqlite3
import os


class ReportGenerator:

    def __init__(self):

        self.db_path = "alerts.db"

        os.makedirs(
            "reports",
            exist_ok=True
        )

    def generate_report(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM alerts
        """)

        alerts = cursor.fetchall()

        pdf = FPDF()

        pdf.set_auto_page_break(
            auto=True,
            margin=15
        )

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            16
        )

        pdf.cell(
            200,
            10,
            "AI Proctoring Report",
            ln=True,
            align="C"
        )

        pdf.ln(10)

        pdf.set_font(
            "Arial",
            "",
            12
        )

        pdf.cell(
            200,
            10,
            f"Total Violations: {len(alerts)}",
            ln=True
        )

        pdf.ln(10)

        for alert in alerts:

            alert_id = alert[0]
            timestamp = alert[1]
            alert_type = alert[2]
            image_path = alert[3]

            pdf.set_font(
                "Arial",
                "B",
                12
            )

            pdf.cell(
                200,
                10,
                f"Violation #{alert_id}",
                ln=True
            )

            pdf.set_font(
                "Arial",
                "",
                11
            )

            pdf.cell(
                200,
                8,
                f"Timestamp: {timestamp}",
                ln=True
            )

            pdf.cell(
                200,
                8,
                f"Type: {alert_type}",
                ln=True
            )

            if os.path.exists(image_path):

                pdf.ln(3)

                pdf.image(
                    image_path,
                    w=80
                )

                pdf.ln(60)

            pdf.ln(5)

        report_path = (
            "reports/proctoring_report.pdf"
        )

        pdf.output(
            report_path
        )

        conn.close()

        print(
            f"[REPORT GENERATED] {report_path}"
        )

        return report_path