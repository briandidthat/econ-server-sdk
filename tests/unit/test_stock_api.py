from src.econ_server_sdk_briandidthat.api import StockApi
from httpx import Response

url = "http://locahost:8080"
api_key = "abcdefg"
headers = {"apiKey": api_key}

stock_api = StockApi(url, api_key)


def test_get_stock_price(stock_price_mock, respx_mock):
    respx_mock.get(f"{url}/stocks", params={"symbol": "AAPL"}, headers=headers).mock(
        return_value=Response(
            status_code=200, content=stock_price_mock.model_dump_json()
        )
    )
    response = stock_api.get_stock_price("AAPL")

    assert response == stock_price_mock


def test_get_multiple_stock_prices(batch_stock_response_mock, respx_mock):
    respx_mock.get(
        f"{url}/stocks/batch", params={"symbols": "AAPL,GOOG,TSLA"}, headers=headers
    ).mock(
        return_value=Response(
            status_code=200, content=batch_stock_response_mock.model_dump_json()
        )
    )
    response = stock_api.get_multiple_stock_prices(["AAPL", "GOOG", "TSLA"])

    assert response == batch_stock_response_mock


def test_get_historical_stock_price(stock_price_mock, respx_mock):
    respx_mock.get(
        f"{url}/stocks/historical",
        params={"symbol": "AAPL", "date": "2024-01-01"},
        headers=headers,
    ).mock(
        return_value=Response(
            status_code=200, content=stock_price_mock.model_dump_json()
        )
    )
    response = stock_api.get_historical_stock_price("AAPL", "2024-01-01")

    assert response == stock_price_mock


def test_get_multiple_hostorical_stock_prices(
    batch_historical_request_mock, batch_stock_response_mock, respx_mock
):
    respx_mock.post(f"{url}/stocks/batch/historical", headers=headers).mock(
        return_value=Response(
            status_code=200, content=batch_stock_response_mock.model_dump_json()
        )
    ).mock(
        return_value=Response(
            status_code=200, content=batch_stock_response_mock.model_dump_json()
        )
    )
    response = stock_api.get_multiple_historical_stock_prices(
        batch_historical_request_mock
    )

    assert response == batch_stock_response_mock
