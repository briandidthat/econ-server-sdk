def test_spot_price(spot_price_mock):
    assert spot_price_mock.symbol == "BTC"
    assert spot_price_mock.price == "40000.00"
    assert spot_price_mock.date == "2024-01-01"


def test_statistic(statistic_mock):
    assert statistic_mock.symbol == "BTC"
    assert statistic_mock.start_price == "30000.00"
    assert statistic_mock.end_price == "40000.00"
    assert statistic_mock.price_change == "10000.00"
    assert statistic_mock.percent_change == "25.00"
    assert statistic_mock.start_date == "2023-01-01"
    assert statistic_mock.end_date == "2024-01-01"
    assert statistic_mock.time_frame == "12 months"


def test_stock_price(stock_price_mock):
    assert stock_price_mock.symbol == "AAPL"
    assert stock_price_mock.price == "200.00"
    assert stock_price_mock.date == "2024-01-01"


def test_fred_response(fred_response_mock):
    assert fred_response_mock.count == 3
    assert len(fred_response_mock.observations) == 3


def test_observation(observation_mock):
    assert observation_mock.realtime_start == "2018-01-01"
    assert observation_mock.realtime_end == "2024-01-01"
    assert observation_mock.date == "2024-01-01"
    assert observation_mock.value == "6.75"
