# econ-server-sdk

The Python SDK for fetching economic data provides a convenient and efficient way to access USA economic indicators and related information. The SDK leverages the capabilities of the [Econ Server]([https://github.com/briandidthat/econ-server) project, which serves as a centralized repository for economic data.

Prerequisites for using this project:
1. Deploy instance of the [econ-server](https://hub.docker.com/repository/docker/briandidthat/econ-server/general) image
2. Generate a FRED API key by visiting [FRED](https://fredaccount.stlouisfed.org/login/secure/)
3. Generate a Twelve Data API key by visiting [Twelve Data](https://twelvedata.com/)

```python
from econ_server_sdk import EconServerClient

# the following variables must be loaded from env, that process is omitted for brevity
econ_server_url = YOUR_ECON_SERVER_INSTANCE_URL
fred_api_key = YOUR_FRED_API_KEY
twelve_api_key = YOUR_TWELVE_DATA_API_KEY

# instantiate econ server client
client = EconServerClient(econ_server_url, fred_api_key, twelve_api_key)
```