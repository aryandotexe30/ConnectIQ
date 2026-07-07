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
                "GEMINI_API_KEY not found."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def research_company(
        self,
        company_name,
        company_text,
    ):

        prompt = f"""
You are a senior business intelligence analyst.

Analyse the following company.

Company:

{company_name}

Website Text:

{company_text}

Return ONLY valid JSON.

Schema:

{{
    "summary":"",
    "industry":"",
    "products":[],
    "services":[],
    "financials":
    {{
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
            "email":"",
            "phone":"",
            "linkedin":"",
            "confidence":0
        }}
    ],
    "sales_insight":
    {{
        "best_department":"",
        "reason":"",
        "opportunity_score":0
    }}
}}

Never explain.

Never use markdown.

Return JSON only.
"""

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        text = response.text.strip()

        if text.startswith("```"):

            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            return json.loads(text)

        except Exception:

            return {
                "summary": "",
                "industry": "",
                "products": [],
                "services": [],
                "financials": {},
                "people": [],
                "sales_insight": {}
            }