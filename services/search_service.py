import os

from dotenv import load_dotenv
from tavily import TavilyClient


class SearchService:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise Exception("TAVILY_API_KEY not found in .env")

        self.client = TavilyClient(api_key)

    def search_company(self, company_name: str):

        query = f"{company_name} official company website"

        response = self.client.search(
            query=query,
            search_depth="basic",
            max_results=5,
        )

        return response.get("results", [])