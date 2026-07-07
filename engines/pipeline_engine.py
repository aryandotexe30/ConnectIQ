from services.company_repository import CompanyRepository


class PipelineEngine:

    def __init__(

        self,

        intelligence_engine,

        export_service,

    ):

        self.intelligence = intelligence_engine

        self.repository = CompanyRepository()

        self.exporter = export_service

    def process(self, companies):

        results = []

        total = len(companies)

        for index, company in enumerate(companies, start=1):

            print()

            print("=" * 80)

            print(f"[{index}/{total}] {company.company_name}")

            print("=" * 80)

            if self.repository.exists(company.company_name):

                print("Already researched. Skipping.")

                continue

            result = self.intelligence.analyze(company)

            self.repository.save(result)

            results.append(result)

            print("Research Complete.")

        if results:

            output = self.exporter.export(results)

            print()

            print(f"Excel exported to: {output}")

        return results