from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from config.settings import Settings

from services.excel_service import ExcelService
from services.export_service import ExportService

from engines.website_engine import WebsiteEngine
from engines.research_engine import ResearchEngine
from engines.intelligence_engine import IntelligenceEngine
from engines.pipeline_engine import PipelineEngine


class ConnectIQ:

    def __init__(self):

        self.console = Console()

        self.settings = Settings()

        self.excel = ExcelService()

        self.exporter = ExportService()

        self.website_engine = WebsiteEngine()


        self.research_engine = ResearchEngine()

        self.intelligence_engine = IntelligenceEngine(

            self.website_engine,

            self.research_engine,


        )

        self.pipeline = PipelineEngine(

            self.intelligence_engine,

            self.exporter,

        )

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

        self.pipeline.process(

            companies

        )

        self.console.print()

        self.console.print(

            "[bold green]Research Completed.[/bold green]"

        )