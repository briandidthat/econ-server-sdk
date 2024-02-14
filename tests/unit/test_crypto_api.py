from src.econ_server_sdk_briandidthat.api import CryptoApi
from httpx import Response

test_url = "http://locahost:8080"
test_username = "tester"
test_headers = {"caller": test_username}

crypto_api = CryptoApi(test_username, test_url)


def test_get_spot_price(spot_price, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot",
        params={"symbol": "BTC"},
        headers=test_headers,
    ).mock(return_value=Response(200, content=spot_price.model_dump_json()))
    response = crypto_api.get_spot_price("BTC")

    assert response == spot_price


def test_get_historical_spot_price(historical_spot_price, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/historical",
        params={"symbol": "BTC", "date": "2023-01-01"},
        headers=test_headers,
    ).mock(return_value=Response(200, content=historical_spot_price.model_dump_json()))
    response = crypto_api.get_historical_spot_price("BTC", "2023-01-01")

    assert response == historical_spot_price


# def test_get_multiple_spot_prices(spot_prices, respx_mock):
#     respx_mock.get(
#         f"{test_url}/crypto/spot/batch",
#         params={"symbols": "BTC,ETH,AVAX"},
#         headers=test_headers,
#     ).mock(
#         return_value=Response(
#             200, content=json.dumps([s.model_dump_json() for s in spot_prices])
#         )
#     )
#     response = crypto_api.get_multiple_spot_prices(["BTC", "ETH", "AVAX"])

#     assert response == spot_prices


def test_get_price_statistics(statistic, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/statistics",
        params={"symbol": "BTC", "startDate": "2023-01-01", "endDate": "2024-01-01"},
        headers=test_headers,
    ).mock(return_value=Response(200, content=statistic.model_dump_json()))
    response = crypto_api.get_price_statistics("BTC", "2023-01-01", "2024-01-01")

    assert response == statistic
