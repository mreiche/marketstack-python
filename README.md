# python-marketstack
Python OpenAPI implementation of the [Marketstack API](https://marketstack.com/documentation) based on https://github.com/mreiche/marketstack-openapi (*not yet published nor fully implemented*).

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

## Developers

### Generate the client
Install the OpenAPI client generator
```shell
pip install openapi-python-client
```
Regenerate the client
```shell
./regenerate.sh
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
