# marketstack-python
Inofficial Python OpenAPI implementation of the [marketstack API](https://marketstack.com/documentation) based on the [marketstack OpenAPI spec](https://github.com/mreiche/marketstack-openapi).

## Usage

### Configuration (recommended)
Set up your API key and TLS support as ENV variables.
```shell
MARKETSTACK_API_KEY="xyz"
MARKETSTACK_TLS_SUPPORT="1"
```

### Create your client

```python
from marketstack.client import Client
import os

def create_client() -> tuple[Client, str]:  
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert access_key is not None and len(access_key) > 0, "Environment variable MARKETSTACK_API_KEY is not defined"

    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    protocol = "https" if tls_support == "1" else "http"
    client = Client(base_url=f"{protocol}://api.marketstack.com/v1")
    
    return client, access_key 
```

### Call operations

```python
from marketstack.api.eod import eod

client, access_key = create_client()

response = eod.sync(
    client=client,
    access_key=access_key,
    symbols="AAPL,AMZN",
    limit=10,
)
```

All endpoint features are implemented and tested. For examples see the repository's `tests/` directory.

### Multiple asynchronous calls

```python
import asyncio
from typing import List
from marketstack.api.intraday import intraday_latest
from marketstack.api.exchanges import exchanges
from marketstack.models import PagedResponseListmodelsIntervalPrice, PagedResponseListmodelsExchange

async def load_async(symbols: List[str]):
   client, access_key = create_client()
   
   prices_call = intraday_latest.asyncio(access_key=access_key, client=client, symbols=",".join(symbols))
   exchanges_call = exchanges.asyncio(access_key=access_key, client=client)
   
   # Type hints for future results
   prices_response: PagedResponseListmodelsIntervalPrice
   exchanges_response: PagedResponseListmodelsExchange
   
   prices_response, exchanges_response = await asyncio.gather(prices_call, exchanges_call)
```


### Error handling
```python
from marketstack.models import ErrorCode, ErrorResponse

if isinstance(response, ErrorResponse):
    assert response.error.code == ErrorCode.FUNCTION_ACCESS_RESTRICTED
```

### Map to Pandas dataframe
```python
import pandas as pd

df = pd.DataFrame(map(lambda x: x.__dict__, response.data))
```

## Developers area

### Generate the client
1. Install the OpenAPI client generator
   ```shell
   pip install openapi-python-client
   ```
2. Regenerate the client
   ```shell
   ./regenerate.sh
   ```

### Run the tests

1. Setup your marketstack API key in `tests/test.env`
2. Run the tests via *pytest*
   ```shell
   PYTHONPATH="." pytest --cov=marketstack tests/
   ```

### Release update
1. Update version in `setup.py`
2. Package library
    ```shell
    python setup.py sdist
    ```
3. Publish library
    ```shell
    twine upload dist/marketstack-[version].tar.gz
    ```

## References

- https://github.com/MichaelKim0407/tutorial-pip-package
- https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
