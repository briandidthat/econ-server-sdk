from src.econ_server_sdk_briandidthat.api import CryptoApi
from httpx import Response

test_url = "http://locahost:8080"
test_username = "tester"
test_headers = {"caller": test_username}

crypto_api = CryptoApi(test_username, test_url)


def test_get_spot_price(spot_price_mock, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot",
        params={"symbol": "BTC"},
        headers=test_headers,
    ).mock(return_value=Response(200, content=spot_price_mock.model_dump_json()))
    response = crypto_api.get_spot_price("BTC")

    assert response == spot_price_mock


def test_get_historical_spot_price(historical_spot_price_mock, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/historical",
        params={"symbol": "BTC", "date": "2023-01-01"},
        headers=test_headers,
    ).mock(
        return_value=Response(200, content=historical_spot_price_mock.model_dump_json())
    )
    response = crypto_api.get_historical_spot_price("BTC", "2023-01-01")

    assert response == historical_spot_price_mock


def test_get_multiple_spot_prices(batch_crypto_response_mock, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/batch",
        params={"symbols": "BTC,ETH,AVAX"},
        headers=test_headers,
    ).mock(
        return_value=Response(200, content=batch_crypto_response_mock.model_dump_json())
    )
    response = crypto_api.get_multiple_spot_prices(["BTC", "ETH", "AVAX"])

    assert response == batch_crypto_response_mock


def test_get_multiple_historical_spot_prices(
    batch_request_mock, batch_crypto_response_mock, respx_mock
):
    respx_mock.post(
        f"{test_url}/crypto/spot/batch/historical",
        headers=test_headers,
        json=batch_request_mock.model_dump_json(),
    ).mock(
        return_value=Response(200, content=batch_crypto_response_mock.model_dump_json())
    )
    response = crypto_api.get_multiple_historical_spot_prices(batch_request_mock)

    assert response == batch_crypto_response_mock


def test_get_price_statistics(statistic_mock, respx_mock):
    respx_mock.get(
        f"{test_url}/crypto/spot/statistics",
        params={"symbol": "BTC", "startDate": "2023-01-01", "endDate": "2024-01-01"},
        headers=test_headers,
    ).mock(return_value=Response(200, content=statistic_mock.model_dump_json()))
    response = crypto_api.get_price_statistics("BTC", "2023-01-01", "2024-01-01")

    assert response == statistic_mock
