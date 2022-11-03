import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from marketstack.client import Client


def next_workday(date: datetime):
    while date.weekday() >= 5:
        date = date.replace(day=date.day + 1)
    return date


day_format = "%Y-%m-%d"
now = datetime.now()
this_year = next_workday(now.replace(month=1, day=1))
this_january = this_year.strftime(day_format)
this_year = next_workday(this_year.replace(month=this_year.month + 1))
this_february = this_year.strftime(day_format)

last_year = next_workday(now.replace(month=1, day=1, year=now.year - 1))
last_january = last_year.strftime(day_format)
last_year = last_year.replace(month=12, day=31)
last_december = last_year.strftime(day_format)


def create_client():
    assert load_dotenv(Path(__file__).parent / "test.env") is True

    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert (
        access_key is not None and len(access_key) > 0
    ), "Environment variable MARKETSTACK_API_KEY is not defined"
    protocol = "https" if tls_support == "1" else "http"
    return Client(base_url=f"{protocol}://api.marketstack.com/v1")
