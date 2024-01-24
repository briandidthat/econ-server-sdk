def test_new_spot_price_fixture(new_spot_price):
    assert new_spot_price.symbol == "BTC"
    assert new_spot_price.currency == "USD"
    assert new_spot_price.amount == "40000.00"
    assert new_spot_price.date == "2024-01-01"
