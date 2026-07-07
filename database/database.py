import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        db_folder = Path("database")

        db_folder.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            db_folder / "connectiq.db"
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS companies(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company_name TEXT,

                address TEXT,

                state TEXT,

                pin_code TEXT,

                business_type TEXT,

                website TEXT,

                summary TEXT,

                industry TEXT,

                revenue TEXT,

                employees TEXT,

                market_cap TEXT,

                parent_company TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS people(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company_name TEXT,

                name TEXT,

                title TEXT,

                department TEXT,

                email TEXT,

                phone TEXT,

                linkedin TEXT,

                confidence INTEGER
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company_name TEXT,

                product TEXT
            )
            """
        )

        self.connection.commit()

    def save_company(self, result):

        self.cursor.execute(

            """
            INSERT INTO companies(

                company_name,

                website,

                summary,

                industry,

                revenue,

                employees,

                market_cap,

                parent_company

            )

            VALUES(?,?,?,?,?,?,?,?)

            """,

            (

                result.company_name,

                result.website,

                result.summary,

                result.industry,

                result.financials.revenue,

                result.financials.employees,

                result.financials.market_cap,

                result.financials.parent_company

            )

        )

        for product in result.products:

            self.cursor.execute(

                """

                INSERT INTO products(

                    company_name,

                    product

                )

                VALUES(?,?)

                """,

                (

                    result.company_name,

                    product

                )

            )

        for person in result.people:

            self.cursor.execute(

                """

                INSERT INTO people(

                    company_name,

                    name,

                    title,

                    department,

                    email,

                    phone,

                    linkedin,

                    confidence

                )

                VALUES(?,?,?,?,?,?,?,?)

                """,

                (

                    result.company_name,

                    person.name,

                    person.title,

                    person.department,

                    person.email,

                    person.phone,

                    person.linkedin,

                    person.confidence

                )

            )

        self.connection.commit()