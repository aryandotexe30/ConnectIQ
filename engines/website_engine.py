from urllib.parse import urlparse

from services.search_service import SearchService


class WebsiteEngine:

    def __init__(self):
        self.search = SearchService()

    def find_website(self, company):

        print(f"\nSearching {company.company_name}")

        results = self.search.search_company(
            company.company_name
        )

        if not results:
            return None

        blacklist = [
            "linkedin",
            "facebook",
            "instagram",
            "youtube",
            "wikipedia",
            "justdial",
            "indiamart",
            "tradeindia",
        ]

        for result in results:

            url = result.get("url")

            if not url:
                continue

            domain = urlparse(url).netloc.lower()

            if any(site in domain for site in blacklist):
                continue

            return url

        return None