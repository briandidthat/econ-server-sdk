import pytest
from typing import List
from src.econ_server_sdk_briandidthat.models import (
    SpotPrice,
    StockPrice,
    Statistic,
    Observation,
    FredResponse,
)


@pytest.fixture(scope="module")
def spot_price() -> SpotPrice:
    return SpotPrice(
        symbol="BTC",
        currency="USD",
        amount="40000.00",
        date="2024-01-01",
    )


@pytest.fixture(scope="module")
def historical_spot_price():
    return SpotPrice(
        symbol="BTC",
        currency="USD",
        amount="30000.00",
        date="2023-01-01",
    )


@pytest.fixture(scope="module")
def spot_prices() -> List[SpotPrice]:
    return [
        SpotPrice(
            symbol="BTC",
            currency="USD",
            amount="40000.00",
            date="2024-01-01",
        ),
        SpotPrice(
            symbol="ETH",
            currency="USD",
            amount="2000.00",
            date="2024-01-01",
        ),
        SpotPrice(
            symbol="AVAX",
            currency="USD",
            amount="30.00",
            date="2024-01-01",
        ),
    ]


@pytest.fixture(scope="module")
def statistic() -> Statistic:
    return Statistic(
        symbol="BTC",
        startPrice="30000.00",
        endPrice="40000.00",
        priceChange="10000.00",
        percentChange="25.00",
        startDate="2023-01-01",
        endDate="2024-01-01",
        timeFrame="12 months",
    )


@pytest.fixture(scope="module")
def stock_price() -> StockPrice:
    return StockPrice(symbol="AAPL", price="200.00")


@pytest.fixture(scope="module")
def observation() -> Observation:
    return Observation(
        realtime_start="2018-01-01",
        realtime_end="2024-01-01",
        date="2024-01-01",
        value="6.75",
    )


@pytest.fixture(scope="module")
def fred_response() -> FredResponse:
    return FredResponse(
        observation_start="2018-01-01",
        observation_end="2024-01-01",
        count="3",
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
