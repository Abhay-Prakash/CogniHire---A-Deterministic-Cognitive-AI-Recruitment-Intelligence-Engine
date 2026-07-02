from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict, Any, TypedDict
from datetime import date

class CompanyCategory(Enum):
    PRODUCT = "PRODUCT"
    SERVICES = "SERVICES"
    STARTUP = "STARTUP"
    ENTERPRISE = "ENTERPRISE"
    UNKNOWN = "UNKNOWN"

class EvidenceSource(Enum):
    CAREER_HISTORY = "CAREER_HISTORY"
    SKILLS = "SKILLS"
    BEHAVIOR = "BEHAVIOR"

class BehaviorSignal(Enum):
    RESPONSE_RATE = "RESPONSE_RATE"
    LAST_ACTIVE = "LAST_ACTIVE"
    GITHUB = "GITHUB"
    OFFER_ACCEPTANCE = "OFFER_ACCEPTANCE"

class CandidateStatus(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    MALFORMED = "MALFORMED"
    
class ValidationReason(Enum):
    VALID = "VALID"
    INVALID_JSON = "INVALID_JSON"
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    INVALID_TYPE = "INVALID_TYPE"
    TIMELINE_INVALID = "TIMELINE_INVALID"
    HONEYPOT_TIME_TRAVELER = "HONEYPOT_TIME_TRAVELER"
    HONEYPOT_SKILL_DURATION = "HONEYPOT_SKILL_DURATION"
    CURRENT_ROLE_INCONSISTENT = "CURRENT_ROLE_INCONSISTENT"

# Transport Object
RawRecord = Dict[str, Any]

@dataclass(frozen=True)
class CareerItem:
    company: str
    title: str
    start_date: Optional[date]
    end_date: Optional[date]
    is_current: bool
    duration_months: int
    description: str

@dataclass(frozen=True)
class ValidatedCandidate:
    candidate_id: str
    years_of_experience: float
    career_history: List[CareerItem]
    skills: List[Dict[str, Any]]
    redrob_signals: Dict[str, float]

@dataclass(frozen=True)
class ValidationResult:
    candidate_id: str
    status: CandidateStatus
    reason_code: str
    warnings: List[str]
    candidate: Optional[ValidatedCandidate]
    line_number: int
    processing_time_ms: float
