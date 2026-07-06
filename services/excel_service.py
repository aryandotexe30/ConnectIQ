from pathlib import Path

import pandas as pd

from models.company import Company


class ExcelService:

    REQUIRED_COLUMNS = [
        "Company Name",
        "Company address",
        "State",
        "Pin Code",
        "Type of Business",
    ]

    def load_companies(self, file_path: Path):

        if not file_path.exists():
            raise FileNotFoundError(
                f"{file_path} does not exist."
            )

        df = pd.read_excel(file_path)

        missing = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        companies = []

        for _, row in df.iterrows():

            company = Company(
                company_name=str(row["Company Name"]).strip(),
                company_address=str(row["Company address"]).strip(),
                state=str(row["State"]).strip(),
                pin_code=str(row["Pin Code"]).strip(),
                business_type=str(row["Type of Business"]).strip(),
            )

            companies.append(company)

        return companies