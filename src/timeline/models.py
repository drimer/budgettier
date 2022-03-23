from dataclasses import dataclass

from src.time_period.models import TimePeriod


@dataclass
class Timeline:
    time_periods: [TimePeriod]
