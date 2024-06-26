# econ-server-sdk

The Python SDK for fetching economic data provides a convenient and efficient way to access USA economic indicators and related information. The SDK leverages the capabilities of the [Econ Server]([https://github.com/briandidthat/econ-server) project, which serves as a centralized repository for economic data.

Prerequisites for using this project:
1. Deploy instance of the [econ-server](https://hub.docker.com/repository/docker/briandidthat/econ-server/general) image
2. Generate a FRED API key by visiting [FRED](https://fredaccount.stlouisfed.org/login/secure/)
3. Generate a Twelve Data API key by visiting [Twelve Data](https://twelvedata.com/)

```python
from econ_server_sdk.api import EconServerClient
from econ_server_sdk.models import AssetPrice

# the following variables must be loaded from env, that process is omitted for brevity
econ_server_url = YOUR_ECON_SERVER_INSTANCE_URL
fred_api_key:  = YOUR_FRED_API_KEY
twelve_api_key = YOUR_TWELVE_DATA_API_KEY

# instantiate econ server client (username can be any string of your choice)
client = EconServerClient(username, econ_server_url, fred_api_key, twelve_api_key)

# request the current price of a cryptocurrency
btc: AssetPrice = client.crypto_api.get_spot_price("BTC")

# request the current price of a stock
apple: AssetPrice = client.stock_api.get_stock_price("AAPL")

# request the current observation of a FRED series (you will need to find the observation id on FRED)
one_year_bond: Observation = client.fred_api.get_current_observation("DGS1")
```