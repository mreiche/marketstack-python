from enum import Enum


class Interval(str, Enum):
    VALUE_0 = "1min"
    VALUE_1 = "5min"
    VALUE_2 = "10min"
    VALUE_3 = "30min"
    VALUE_4 = "1hour"
    VALUE_5 = "3hour"
    VALUE_6 = "6hour"
    VALUE_7 = "12hour"
    VALUE_8 = "24hour"

    def __str__(self) -> str:
        return str(self.value)
