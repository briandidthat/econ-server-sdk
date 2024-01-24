def test_new_spot_price_fixture(new_spot_price):
    assert new_spot_price.symbol == "BTC"
    assert new_spot_price.currency == "USD"
    assert new_spot_price.amount == "40000.00"
    assert new_spot_price.date == "2024-01-01"


def test_new_statistic_fixture(new_statistic):
    assert new_statistic.symbol == "BTC"
    assert new_statistic.start_price == "30000.00"
    assert new_statistic.end_price == "40000.00"
    assert new_statistic.price_change == "10000.00"
    assert new_statistic.percent_change == "25.00"
    assert new_statistic.start_date == "2023-01-01"
    assert new_statistic.end_date == "2024-01-01"
    assert new_statistic.time_frame == "12 months" 


def test_new_stock_price_fixture(new_stock_price):
    assert new_stock_price.symbol == "AAPL"
    assert new_stock_price.price == "200.00"


def test_new_observation_fixture(new_mortgage_rate_observation):
    assert new_mortgage_rate_observation.realtime_start == "2018-01-01"
    assert new_mortgage_rate_observation.realtime_end == "2024-01-01"
    assert new_mortgage_rate_observation.date == "2024-01-01"
    assert new_mortgage_rate_observation.value == "6.75"


def test_new_observations_fixture(new_mortgage_rate_observations):
    assert len(new_mortgage_rate_observations) == 3
