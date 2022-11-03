from dotenv import load_dotenv
from marketstack.client import Client
import os
from pathlib import Path
from datetime import datetime


def next_weekday(date: datetime):
    while date.weekday() >= 5:
        date = date.replace(day=date.day+1)
    return date


now = next_weekday(datetime.now().replace(month=1, day=1))
date_from = now.strftime("%Y-%m-%d")
now = next_weekday(now.replace(month=now.month+1))
date_to = now.strftime("%Y-%m-%d")


def create_client():
    assert load_dotenv(Path(__file__).parent / "test.env") is True

    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert (
        access_key is not None and len(access_key) > 0
    ), "Environment variable MARKETSTACK_API_KEY is not defined"
    protocol = "https" if tls_support == "1" else "http"
    return Client(base_url=f"{protocol}://api.marketstack.com/v1")
