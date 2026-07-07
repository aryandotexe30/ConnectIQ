import requests
from bs4 import BeautifulSoup

from services.search_service import SearchService
from services.ai_service import AIService


class ResearchEngine:

    def __init__(self):

        self.search = SearchService()

        self.ai = AIService()

    def _download_page(self, url):

        try:

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                    " AppleWebKit/537.36 "
                    "(KHTML, like Gecko)"
                    " Chrome/138.0 Safari/537.36"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=20,
            )

            if response.status_code != 200:
                return ""

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            for tag in soup(
                [
                    "script",
                    "style",
                    "noscript",
                    "svg",
                    "footer",
                    "header",
                    "nav"
                ]
            ):
                tag.decompose()

            text = soup.get_text(
                separator="\n",
                strip=True
            )

            lines = []

            for line in text.split("\n"):

                line = line.strip()

                if len(line) > 2:
                    lines.append(line)

            text = "\n".join(lines)

            return text[:30000]

        except Exception:

            return ""

    def research(self, company):

        queries = [

            f"{company.company_name} official website",

            f"{company.company_name} about",

            f"{company.company_name} products",

            f"{company.company_name} annual report",

            f"{company.company_name} management",

            f"{company.company_name} leadership",

            f"{company.company_name} board of directors",

            f"{company.company_name} procurement",

            f"{company.company_name} engineering",

            f"{company.company_name} manufacturing"

        ]

        pages = []

        visited = set()

        for query in queries:

            print(f"\nSearching: {query}")

            try:

                results = self.search.client.search(

                    query=query,

                    search_depth="advanced",

                    max_results=2,

                )["results"]

            except Exception:

                continue

            for result in results:

                url = result.get("url")

                if not url:
                    continue

                if url in visited:
                    continue

                visited.add(url)

                print(f"Reading {url}")

                page = self._download_page(url)

                if len(page) < 300:
                    continue

                pages.append(page)

        merged_text = "\n\n".join(pages)

        print()

        print(
            f"Collected {len(pages)} pages."
        )

        print(
            f"Characters: {len(merged_text)}"
        )

        print()

        intelligence = self.ai.research_company(

            company.company_name,

            merged_text

        )

        return intelligence