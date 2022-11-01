# python-marketstack
Python implementation of the Marketstack API. It simply calls the API endpoints and parses the response into *Pydantic* models. 

## Configuration
Set up your API key and TLS support as ENV variables.
```shell
MARKETSTACK_API_KEY="xyz"
MARKETSTACK_TLS_SUPPORT="1"
```

## Usage
```python
from marketstack import query_intraday

intraday = query_intraday(symbols=["AAPL"])
for interval in intraday.data:
    print(f"{interval.close} on {interval.data}")
```
