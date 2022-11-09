from marketstack.models import ErrorCode, Interval


def test_error_codes():
    assert ErrorCode.NOT_FOUND_ERROR.value == "not_found_error"


def test_interval():
    assert Interval.HOUR1.value == "1hour"
