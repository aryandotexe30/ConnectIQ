import json
import os

from dotenv import load_dotenv
from google import genai


class AIService:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"

    def research_company(self, company_name: str, company_text: str):

        prompt = f"""
You are an expert B2B business intelligence analyst.

Your task is to analyse the information below and ONLY use the information
provided.

Never invent people.
Never guess financials.
If something is unavailable, return an empty string.

Return ONLY valid JSON.

Schema:

{{
    "summary":"",
    "industry":"",
    "products":[],
    "services":[],
    "financials":{{
        "revenue":"",
        "employees":"",
        "market_cap":"",
        "parent_company":""
    }},
    "people":[
        {{
            "name":"",
            "title":"",
            "department":"",
            "reason":"",
            "confidence":0
        }}
    ]
}}

Company:

{company_name}

Information:

{company_text}
"""

        try:

            response = self.client.models.generate_content(

                model=self.model,

                contents=prompt

            )

            text = response.text.strip()

            if text.startswith("```json"):
                text = text.replace("```json", "")
                text = text.replace("```", "").strip()

            elif text.startswith("```"):
                text = text.replace("```", "").strip()

            data = json.loads(text)

            return data

        except Exception as e:

            print()

            print("Gemini Error")

            print(e)

            print()

            return {
                "summary": "",
                "industry": "",
                "products": [],
                "services": [],
                "financials": {
                    "revenue": "",
                    "employees": "",
                    "market_cap": "",
                    "parent_company": ""
                },
                "people": []
            }