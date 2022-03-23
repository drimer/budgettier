from dataclasses import dataclass
from datetime import datetime, date

from src.budget.models import Budget


@dataclass
class TimePeriod:
    date_to: date
    date_from: date
    budget: Budget
