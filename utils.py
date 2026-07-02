from datetime import datetime, date
from typing import Optional, Any
from core.constants import DATE_FORMAT

def parse_date(date_str: Optional[str]) -> Optional[date]:
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        return None

def calculate_duration_months(start: Optional[date], end: Optional[date]) -> int:
    if not start:
        return 0
    if not end:
        end = date.today()
    return (end.year - start.year) * 12 + end.month - start.month

def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return default
