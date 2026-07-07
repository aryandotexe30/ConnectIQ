from database.database import Database


class CompanyRepository:

    def __init__(self):

        self.db = Database()

    def save(self, result):

        self.db.save_company(result)

    def exists(self, company_name):

        self.db.cursor.execute(

            """
            SELECT id
            FROM companies
            WHERE company_name = ?
            LIMIT 1
            """,

            (company_name,)

        )

        row = self.db.cursor.fetchone()

        return row is not None

    def get(self, company_name):

        self.db.cursor.execute(

            """
            SELECT *

            FROM companies

            WHERE company_name = ?

            LIMIT 1
            """,

            (company_name,)

        )

        return self.db.cursor.fetchone()

    def all(self):

        self.db.cursor.execute(

            """
            SELECT *

            FROM companies
            ORDER BY company_name
            """

        )

        return self.db.cursor.fetchall()

    def delete(self, company_name):

        self.db.cursor.execute(

            """
            DELETE FROM companies
            WHERE company_name = ?
            """,

            (company_name,)

        )

        self.db.connection.commit()

    def clear(self):

        self.db.cursor.execute(

            """
            DELETE FROM companies
            """

        )

        self.db.connection.commit()