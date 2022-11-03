from enum import Enum


class Interval(str, Enum):
    MIN1 = "1min"
    MIN5 = "5min"
    MIN10 = "10min"
    MIN30 = "30min"
    HOUR1 = "1hour"
    HOUR3 = "3hour"
    HOUR6 = "6hour"
    HOUR12 = "12hour"
    HOUR24 = "24hour"

    def __str__(self) -> str:
        return str(self.value)
