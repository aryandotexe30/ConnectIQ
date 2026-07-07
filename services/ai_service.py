import json
import os

from dotenv import load_dotenv
from google import genai


class AIService:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("GEMINI_API_KEY not found.")

        self.client = genai.Client(
            api_key=api_key
        )

    def research_company(
        self,
        company_name,
        company_text,
    ):

        prompt = f"""
You are a Senior Business Intelligence Analyst.

Your job is to build a COMPLETE business profile.

Company:

{company_name}

Collected Information:

{company_text}

Only use information that is present or can be inferred with high confidence.

Never hallucinate.

If a value is unavailable, return an empty string "" or an empty list [].

Return ONLY valid JSON.

Schema:

{{
  "company_name":"",
  "summary":"",
  "industry":"",

  "gst_number":"",
  "cin":"",
  "pan":"",

  "incorporation_date":"",
  "registered_address":"",
  "headquarters":"",
  "company_status":"",

  "authorized_capital":"",
  "paidup_capital":"",

  "products":[],
  "product_categories":[],
  "brands":[],
  "services":[],
  "industries_served":[],
  "manufacturing_locations":[],
  "certifications":[],

  "financials":
  {{
      "revenue":"",
      "total_income":"",
      "operating_profit":"",
      "ebitda":"",
      "net_profit":"",
      "eps":"",
      "market_cap":"",
      "enterprise_value":"",
      "assets":"",
      "liabilities":"",
      "net_worth":"",
      "debt":"",
      "cash_flow":"",
      "employees":"",
      "parent_company":""
  }},

  "people":
  [
    {{
      "name":"",
      "title":"",
      "department":"",
      "email":"",
      "phone":"",
      "linkedin":"",
      "confidence":0,
      "source":""
    }}
  ],

  "competitors":[],
  "customers":[],
  "suppliers":[],

  "sales_strategy":"",

  "opportunity_score":0,

  "sources":[]
}}

Do NOT explain.

Do NOT use markdown.

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

        except Exception as e:

            print("AI JSON Parsing Error")
            print(e)

            return {}