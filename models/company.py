from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Contact:
    name: str
    designation: str
    department: str
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    confidence: float = 0.0
    source: Optional[str] = None


@dataclass
class Company:

    # Input Data
    company_name: str
    company_address: str
    state: str
    pin_code: str
    business_type: str

    # Enriched Data
    website: Optional[str] = None
    industry: Optional[str] = None
    description: Optional[str] = None
    employee_count: Optional[str] = None

    # AI Results
    contacts: List[Contact] = field(default_factory=list)
    opportunity_score: float = 0.0
    ai_summary: Optional[str] = None