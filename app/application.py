from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from config.settings import Settings
from services.excel_service import ExcelService

from engines.website_engine import WebsiteEngine
from engines.research_engine import ResearchEngine


class ConnectIQ:

    def __init__(self):

        self.console = Console()

        self.settings = Settings()

        self.excel = ExcelService()

        self.website_engine = WebsiteEngine()

        self.research_engine = ResearchEngine()

    def run(self):

        self.console.print()

        self.console.print(
            Panel.fit(
                "[bold cyan]ConnectIQ[/bold cyan]\n"
                "Business Intelligence Engine\n"
                "Version 1.0.0",
                border_style="green",
            )
        )

        excel_file = (
            Path(self.settings.INPUT_FOLDER)
            / "companies.xlsx"
        )

        self.console.print(
            "[bold yellow]Loading companies...[/bold yellow]"
        )

        companies = self.excel.load_companies(
            excel_file
        )

        self.console.print(
            f"[green]Loaded {len(companies)} companies.[/green]"
        )

        # Development mode
        companies = companies[:1]

        for company in companies:

            self.console.rule(
                f"[bold cyan]{company.company_name}"
            )

            website = self.website_engine.find_website(
                company
            )

            if website:

                company.website = website

                self.console.print(
                    f"[green]Website[/green] : {website}"
                )

            else:

                self.console.print(
                    "[red]Website not found.[/red]"
                )

            self.console.print()

            self.console.print(
                "[bold yellow]Researching company...[/bold yellow]"
            )

            intelligence = self.research_engine.research(
                company
            )

            self.console.print()

            self.console.rule(
                "[bold green]RESULTS"
            )

            self.console.print()

            self.console.print(
                f"[bold cyan]Summary[/bold cyan]\n"
            )

            self.console.print(
                intelligence.get(
                    "summary",
                    "Not Available"
                )
            )

            self.console.print()

            self.console.print(
                "[bold cyan]Industry[/bold cyan]"
            )

            self.console.print(
                intelligence.get(
                    "industry",
                    ""
                )
            )

            self.console.print()

            self.console.print(
                "[bold cyan]Products[/bold cyan]"
            )

            for product in intelligence.get(
                "products",
                []
            ):

                self.console.print(
                    f"• {product}"
                )

            self.console.print()

            self.console.print(
                "[bold cyan]Services[/bold cyan]"
            )

            for service in intelligence.get(
                "services",
                []
            ):

                self.console.print(
                    f"• {service}"
                )

            self.console.print()

            financials = intelligence.get(
                "financials",
                {}
            )

            self.console.print(
                "[bold cyan]Financials[/bold cyan]"
            )

            self.console.print(
                f"Revenue : {financials.get('revenue','')}"
            )

            self.console.print(
                f"Employees : {financials.get('employees','')}"
            )

            self.console.print(
                f"Market Cap : {financials.get('market_cap','')}"
            )

            self.console.print(
                f"Parent Company : {financials.get('parent_company','')}"
            )

            self.console.print()

            self.console.print(
                "[bold cyan]Decision Makers[/bold cyan]"
            )

            people = intelligence.get(
                "people",
                []
            )

            if not people:

                self.console.print(
                    "[yellow]No decision makers found.[/yellow]"
                )

            else:

                for person in people:

                    self.console.print()

                    self.console.print(
                        f"[bold]{person.get('name','')}[/bold]"
                    )

                    self.console.print(
                        f"Title : {person.get('title','')}"
                    )

                    self.console.print(
                        f"Department : {person.get('department','')}"
                    )

                    self.console.print(
                        f"Reason : {person.get('reason','')}"
                    )

                    self.console.print(
                        f"Confidence : {person.get('confidence','')}"
                    )

            self.console.print()

            self.console.rule()