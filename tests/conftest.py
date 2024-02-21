import pytest
from typing import List
from src.econ_server_sdk_briandidthat.models import (
    Request,
    BatchRequest,
    BatchResponse,
    AssetPrice,
    Statistic,
    Observation,
    FredResponse,
)


@pytest.fixture(scope="module")
def spot_price_mock() -> AssetPrice:
    return AssetPrice(
        symbol="BTC",
        price="40000.00",
        date="2024-01-01",
    )


@pytest.fixture(scope="module")
def historical_spot_price_mock():
    return AssetPrice(
        symbol="BTC",
        price="30000.00",
        date="2023-01-01",
    )


@pytest.fixture(scope="module")
def batch_request_mock() -> BatchRequest:
    return BatchRequest(
        requests=[
            Request(symbol="BTC", date="2024-01-01"),
            Request(symbol="ETH", date="2024-01-01"),
            Request(symbol="AVAX", date="2024-01-01"),
        ]
    )


@pytest.fixture(scope="module")
def batch_crypto_response_mock() -> BatchResponse:
    return BatchResponse(
        asset_prices=[
            AssetPrice(
                symbol="BTC",
                price="40000.00",
                date="2024-01-01",
            ),
            AssetPrice(
                symbol="ETH",
                price="2000.00",
                date="2024-01-01",
            ),
            AssetPrice(
                symbol="AVAX",
                price="30.00",
                date="2024-01-01",
            ),
        ]
    )


@pytest.fixture(scope="module")
def statistic_mock() -> Statistic:
    return Statistic(
        symbol="BTC",
        start_price="30000.00",
        end_price="40000.00",
        price_change="10000.00",
        percent_change="25.00",
        start_date="2023-01-01",
        end_date="2024-01-01",
        time_frame="12 months",
    )


@pytest.fixture(scope="module")
def stock_price_mock() -> AssetPrice:
    return AssetPrice(symbol="AAPL", price="200.00", date="2024-01-01")

@pytest.fixture(scope="module")
def batch_stock_response_mock() -> BatchResponse:
    return BatchResponse(
        asset_prices=[
            AssetPrice(
                symbol="AAPL",
                price="150.00",
                date="2024-01-01",
            ),
            AssetPrice(
                symbol="GOOG",
                price="161.00",
                date="2024-01-01",
            ),
            AssetPrice(
                symbol="TSLA",
                price="400.00",
                date="2024-01-01",
            ),
        ]
    )


@pytest.fixture(scope="module")
def observation_mock() -> Observation:
    return Observation(
        realtime_start="2018-01-01",
        realtime_end="2024-01-01",
        date="2024-01-01",
        value="6.75",
    )


@pytest.fixture(scope="module")
def fred_response_mock() -> FredResponse:
    return FredResponse(
        observation_start="2018-01-01",
        observation_end="2024-01-01",
        count=3,
        observations=[
            Observation(
                realtime_start="2018-01-01",
                realtime_end="2024-01-01",
                date="2024-01-01",
                value="6.75",
            ),
            Observation(
                realtime_start="2018-01-01",
                realtime_end="2024-01-01",
                date="2023-12-01",
                value="6.69",
            ),
            Observation(
                realtime_start="2018-01-01",
                realtime_end="2024-01-01",
                date="2023-11-01",
                value="6.91",
            ),
        ],
    )
