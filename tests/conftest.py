import pytest
from typing import List
from src.econ_server_sdk_briandidthat.models import (
    SpotPrice,
    StockPrice,
    Statistic,
    Observation,
)


@pytest.fixture(scope="module")
def new_spot_price() -> SpotPrice:
    return SpotPrice(
        **{
            "symbol": "BTC",
            "currency": "USD",
            "amount": "40000.00",
            "date": "2024-01-01",
        }
    )


@pytest.fixture(scope="module")
def new_statistic() -> Statistic:
    return Statistic(
        **{
            "symbol": "BTC",
            "startPrice": "30000.00",
            "endPrice": "40000.00",
            "priceChange": "10000.00",
            "percentChange": "25.00",
            "startDate": "2023-01-01",
            "endDate": "2024-01-01",
            "timeFrame": "12 months",
        }
    )


@pytest.fixture(scope="module")
def new_stock_price() -> StockPrice:
    return StockPrice(**{"symbol": "AAPL", "price": "200.00"})


@pytest.fixture(scope="module")
def new_mortgage_rate_observation() -> Observation:
    return Observation(
        **{
            "realtime_start": "2018-01-01",
            "realtime_end": "2024-01-01",
            "date": "2024-01-01",
            "value": "6.75",
        }
    )


@pytest.fixture(scope="module")
def new_mortgage_rate_observations() -> List[Observation]:
    observations = [
        Observation("2018-01-01", "2024-01-01", "2024-01-01", "6.75"),
        Observation("2018-01-01", "2024-01-01", "2023-12-01", "6.69"),
        Observation("2018-01-01", "2024-01-01", "2023-11-01", "6.91"),
    ]

    return observations
