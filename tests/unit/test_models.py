def test_spot_price(spot_price):
    assert spot_price.symbol == "BTC"
    assert spot_price.currency == "USD"
    assert spot_price.amount == "40000.00"
    assert spot_price.date == "2024-01-01"


def test_statistic(statistic):
    assert statistic.symbol == "BTC"
    assert statistic.start_price == "30000.00"
    assert statistic.end_price == "40000.00"
    assert statistic.price_change == "10000.00"
    assert statistic.percent_change == "25.00"
    assert statistic.start_date == "2023-01-01"
    assert statistic.end_date == "2024-01-01"
    assert statistic.time_frame == "12 months" 


def test_stock_price(stock_price):
    assert stock_price.symbol == "AAPL"
    assert stock_price.price == "200.00"


def test_observation(mortgage_rate_observation):
    assert mortgage_rate_observation.realtime_start == "2018-01-01"
    assert mortgage_rate_observation.realtime_end == "2024-01-01"
    assert mortgage_rate_observation.date == "2024-01-01"
    assert mortgage_rate_observation.value == "6.75"


def test_observations(mortgage_rate_observations):
    assert len(mortgage_rate_observations) == 3
