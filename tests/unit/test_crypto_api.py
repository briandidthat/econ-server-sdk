from src.econ_server_sdk_briandidthat.api import CryptoApi
from httpx import Response


test_url = "http://locahost:8080"
test_username = "tester"
crypto_api = CryptoApi(test_username, test_url)


def test_get_spot_price(spot_price, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot",
        params={"symbol": "BTC"},
        headers={"caller": test_username},
    ).mock(return_value=Response(200, content=spot_price.model_dump_json()))
    response = crypto_api.get_spot_price("BTC")

    assert response == spot_price


def test_get_historical_spot_price(historical_spot_price, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/historical",
        params={"symbol": "BTC", "date": "2023-01-01"},
        headers={"caller": test_username},
    ).mock(return_value=Response(200, content=historical_spot_price.model_dump_json()))
    response = crypto_api.get_historical_spot_price("BTC", "2023-01-01")

    assert response == historical_spot_price
