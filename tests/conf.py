import pytest
from typing import List
from src.econ_server_sdk_briandidthat.models import SpotPrice, StockPrice, Statistic, Observation


@pytest.fixture(scope="module")
def new_statistic() -> Statistic:
    return Statistic("BTC", "30000.00", "40000.00", "1000.00", "25.00", "2023-01-01", "2024-01-01", "12 months")

@pytest.fixture(scope="module")
def new_spot_price() -> SpotPrice:
    return SpotPrice("BTC", "USD", "40000.00", "2024-01-01")

@pytest.fixture(scope="module")
def new_stock_price() -> StockPrice:
    return StockPrice("AAPL", "200.00")


@pytest.fixture(scope="module")
def new_mortgage_rate_observation() -> Observation:
    return Observation("2018-01-01", "2024-01-01", "2024-01-01", "6.75")

@pytest.fixture(scope="module")
def new_mortgage_rate_observations() -> List[Observation]:
    observations = [Observation("2018-01-01", "2024-01-01", "2024-01-01", "6.75"),
                    Observation("2018-01-01", "2024-01-01", "2023-12-01", "6.69"),
                    Observation("2018-01-01", "2024-01-01", "2023-11-01", "6.91")]
    
    return observations