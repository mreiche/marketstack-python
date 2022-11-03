from marketstack.models import ErrorCode, Interval


def test_error_codes():
    assert ErrorCode.NOT_FOUND.value == "404_not_found"


def test_interval():
    assert Interval.HOUR1.value == "1hour"
