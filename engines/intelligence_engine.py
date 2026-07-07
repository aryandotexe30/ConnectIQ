from models.company_result import (
    CompanyResult,
    Person,
)


class IntelligenceEngine:

    def __init__(
        self,
        website_engine,
        research_engine,
    ):

        self.website_engine = website_engine

        self.research_engine = research_engine

    def analyze(self, company):

        result = CompanyResult()

        result.company_name = company.company_name

        # ----------------------------
        # Find official website
        # ----------------------------

        website = self.website_engine.find_website(company)

        if website:

            result.website = website

            company.website = website

        # ----------------------------
        # Research company
        # ----------------------------

        research = self.research_engine.research(company)

        if not research:

            return result

        # ----------------------------
        # Summary
        # ----------------------------

        result.summary = research.get(
            "summary",
            ""
        )

        result.industry = research.get(
            "industry",
            ""
        )

        # ----------------------------
        # Products
        # ----------------------------

        result.products = research.get(
            "products",
            []
        )

        # ----------------------------
        # Services
        # ----------------------------

        result.services = research.get(
            "services",
            []
        )

        # ----------------------------
        # Financials
        # ----------------------------

        financials = research.get(
            "financials",
            {}
        )

        result.financials.revenue = financials.get(
            "revenue",
            ""
        )

        result.financials.employees = financials.get(
            "employees",
            ""
        )

        result.financials.market_cap = financials.get(
            "market_cap",
            ""
        )

        result.financials.parent_company = financials.get(
            "parent_company",
            ""
        )

        # ----------------------------
        # People
        # ----------------------------

        people = research.get(
            "people",
            []
        )

        for person in people:

            result.people.append(

                Person(

                    name=person.get(
                        "name",
                        ""
                    ),

                    title=person.get(
                        "title",
                        ""
                    ),

                    department=person.get(
                        "department",
                        ""
                    ),

                    email=person.get(
                        "email",
                        ""
                    ),

                    phone=person.get(
                        "phone",
                        ""
                    ),

                    linkedin=person.get(
                        "linkedin",
                        ""
                    ),

                    source=person.get(
                        "source",
                        ""
                    ),

                    confidence=person.get(
                        "confidence",
                        0
                    )

                )

            )

        return result