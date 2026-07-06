import requests

from services.search_service import SearchService
from services.ai_service import AIService


class PeopleEngine:

    def __init__(self):

        self.search = SearchService()
        self.ai = AIService()

    def _download_page(self, url):

        try:

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=15,
            )

            if response.status_code != 200:
                return ""

            text = response.text

            if len(text) > 50000:
                text = text[:50000]

            return text

        except Exception:
            return ""

    def find_people(self, company_name):

        search_queries = [

            f"{company_name} leadership",

            f"{company_name} management",

            f"{company_name} leadership team",

            f"{company_name} executive team",

            f"{company_name} directors",

            f"{company_name} procurement",

            f"{company_name} engineering",

            f"{company_name} operations"

        ]

        people = []

        visited = set()

        for query in search_queries:

            print(f"\nSearching: {query}")

            try:

                results = self.search.client.search(
                    query=query,
                    search_depth="advanced",
                    max_results=3,
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

                html = self._download_page(url)

                if len(html) < 500:
                    continue

                found = self.ai.extract_people(
                    company_name,
                    html,
                )

                if found:

                    people.extend(found)

        unique = []

        names = set()

        for person in people:

            name = person.get("name", "").strip()

            if not name:
                continue

            if name.lower() in names:
                continue

            names.add(name.lower())

            unique.append(person)

        return unique