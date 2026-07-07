from dataclasses import dataclass, field


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


@dataclass
class Financials:

    revenue: str = ""

    employees: str = ""

    market_cap: str = ""

    parent_company: str = ""


@dataclass
class CompanyResult:

    company_name: str = ""

    website: str = ""

    summary: str = ""

    industry: str = ""

    products: list[str] = field(default_factory=list)

    services: list[str] = field(default_factory=list)

    financials: Financials = field(default_factory=Financials)

    people: list[Person] = field(default_factory=list)