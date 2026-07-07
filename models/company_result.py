from dataclasses import dataclass, field


# ============================================================
# PERSON
# ============================================================

@dataclass
class Person:

    name: str = ""

    title: str = ""

    department: str = ""

    email: str = ""

    phone: str = ""

    linkedin: str = ""

    source: str = ""

    confidence: int = 0


# ============================================================
# FINANCIALS
# ============================================================

@dataclass
class Financials:

    revenue: str = ""

    total_income: str = ""

    operating_profit: str = ""

    ebitda: str = ""

    net_profit: str = ""

    eps: str = ""

    market_cap: str = ""

    enterprise_value: str = ""

    assets: str = ""

    liabilities: str = ""

    net_worth: str = ""

    debt: str = ""

    cash_flow: str = ""

    employees: str = ""

    parent_company: str = ""

    source: str = ""


# ============================================================
# COMPANY
# ============================================================

@dataclass
class CompanyResult:

    company_name: str = ""

    website: str = ""

    summary: str = ""

    industry: str = ""

    gst_number: str = ""

    cin: str = ""

    pan: str = ""

    incorporation_date: str = ""

    registered_address: str = ""

    headquarters: str = ""

    company_status: str = ""

    authorized_capital: str = ""

    paidup_capital: str = ""

    products: list = field(default_factory=list)

    product_categories: list = field(default_factory=list)

    brands: list = field(default_factory=list)

    services: list = field(default_factory=list)

    industries_served: list = field(default_factory=list)

    manufacturing_locations: list = field(default_factory=list)

    certifications: list = field(default_factory=list)

    people: list = field(default_factory=list)

    financials: Financials = field(
        default_factory=Financials
    )

    competitors: list = field(default_factory=list)

    customers: list = field(default_factory=list)

    suppliers: list = field(default_factory=list)

    ai_summary: str = ""

    sales_strategy: str = ""

    opportunity_score: int = 0

    sources: list = field(default_factory=list)