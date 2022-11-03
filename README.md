# marketstack-python
Python OpenAPI implementation of the [Marketstack API](https://marketstack.com/documentation) based on the [OpenAPI spec](https://github.com/mreiche/marketstack-openapi) (*not fully tested*).

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

tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
protocol = "https" if tls_support == "1" else "http"
client = Client(base_url=f"{protocol}://api.marketstack.com/v1")
```

### Import and call operations
```python
from marketstack.api.eod import eod
import os

response = eod.sync(
    client=client,
    access_key=os.getenv("MARKETSTACK_API_KEY"),
    symbols="AAPL,AMZN",
    limit=10,
)
```

### Error handling
```python
from marketstack.models import ErrorCode, ErrorResponse

assert isinstance(response, ErrorResponse)
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
   pytest tests
   ```

### Release update
1. Update version in `setup.py`
2. Package library
    ```shell
    python setup.py sdist
    ```
3. Publish library
    ```shell
    twine upload dist/{packaged file}.tar.gz
    ```

## References

- https://github.com/MichaelKim0407/tutorial-pip-package
- https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
