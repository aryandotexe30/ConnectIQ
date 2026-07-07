from pathlib import Path

import pandas as pd


class ExportService:

    def __init__(self):

        self.output_folder = Path("data/output")

        self.output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def export(self, company_results):

        rows = []

        for company in company_results:

            if company.people:

                for person in company.people:

                    rows.append({

                        "Company Name": company.company_name,

                        "Website": company.website,

                        "Industry": company.industry,

                        "Summary": company.summary,

                        "Revenue": company.financials.revenue,

                        "Employees": company.financials.employees,

                        "Market Cap": company.financials.market_cap,

                        "Parent Company": company.financials.parent_company,

                        "Products": ", ".join(company.products),

                        "Services": ", ".join(company.services),

                        "Person": person.name,

                        "Designation": person.title,

                        "Department": person.department,

                        "Email": person.email,

                        "Phone": person.phone,

                        "LinkedIn": person.linkedin,

                        "Confidence": person.confidence

                    })

            else:

                rows.append({

                    "Company Name": company.company_name,

                    "Website": company.website,

                    "Industry": company.industry,

                    "Summary": company.summary,

                    "Revenue": company.financials.revenue,

                    "Employees": company.financials.employees,

                    "Market Cap": company.financials.market_cap,

                    "Parent Company": company.financials.parent_company,

                    "Products": ", ".join(company.products),

                    "Services": ", ".join(company.services),

                    "Person": "",

                    "Designation": "",

                    "Department": "",

                    "Email": "",

                    "Phone": "",

                    "LinkedIn": "",

                    "Confidence": ""

                })

        dataframe = pd.DataFrame(rows)

        output_file = self.output_folder / "company_research.xlsx"

        dataframe.to_excel(

            output_file,

            index=False

        )

        return output_file