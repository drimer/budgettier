from dataclasses import dataclass


@dataclass
class Row:
    quantity: float
    label: str
    category: str  # Optional => How?


@dataclass
class Income(Row):
    pass


@dataclass
class Outcome(Row):
    pass
