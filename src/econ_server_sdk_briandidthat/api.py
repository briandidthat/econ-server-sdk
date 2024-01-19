import logging
from typing import Any

import requests

from .models import Observation, SpotPrice, FredOperation, Statistic, StockPrice

logging.basicConfig(level=logging.INFO)


class CryptoApi:
    def __init__(self, user: str, base_url: str):
        self.__caller = user
        self.__base_url = base_url
        self.__logger = logging.getLogger("Crypto-API")

    def get_spot_price(self, symbol: str) -> SpotPrice:
        params = {"symbol": symbol}
        headers = dict(caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching spot price for {symbol}")
            response = requests.get(
                f"{self.__base_url}/crypto/spot", params=params, headers=headers
            )
            spot_price = SpotPrice(**response.json())
            self.__logger.info(f"Completed spot price request for {symbol}")
            return spot_price
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_historical_spot_price(self, symbol: str, date: str) -> SpotPrice:
        params = {"symbol": symbol, "date": date}
        headers = dict(caller=self.__caller)

        try:
            self.__logger.debug(
                f"Fetching historical spot price for {symbol}. Date: {date}"
            )
            response = requests.get(
                f"{self.__base_url}/crypto/spot/historical",
                params=params,
                headers=headers,
            )
            historical_spot_price = SpotPrice(**response.json())
            self.__logger.info(
                f"Completed historical spot price request for {symbol}. Date: {date}"
            )
            return historical_spot_price
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_price_statistics(
        self, symbol: str, start_date: str, end_date: str
    ) -> Statistic:
        params = {"symbol": symbol, "startDate": start_date, "endDate": end_date}
        headers = dict(caller=self.__caller)

        try:
            self.__logger.debug(
                f"Fetching price statistics for {symbol}. Timeframe: {start_date} -> {end_date}"
            )
            response = requests.get(
                f"{self.__base_url}/crypto/spot/statistics",
                params=params,
                headers=headers,
            )
            statistic = Statistic(**response.json())
            self.__logger.info(
                f"Completed statistics request for {symbol}. Timeframe: {start_date} -> {end_date}"
            )
            print(statistic)
            return statistic
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_multiple_spot_prices(self, symbols: list[str]) -> list[SpotPrice]:
        params = {"symbols": ",".join(symbols)}
        headers = dict(caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching multiple spot prices for: {symbols}")
            response = requests.get(
                f"{self.__base_url}/crypto/spot/batch", params=params, headers=headers
            )
            spot_prices = [SpotPrice(**s) for s in response.json()]
            self.__logger.info(f"Completed batch request for {symbols}.")
            return spot_prices
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_multiple_historical_spot_prices(
        self, reqs: list[tuple[str, str]]
    ) -> list[SpotPrice]:
        headers = dict(caller=self.__caller)

        try:
            self.__logger.debug(
                f"Fetching multiple historical spot prices for: {','.join([s[0] for s in reqs])}"
            )
            response = requests.post(
                f"{self.__base_url}/crypto/spot/batch", json=reqs, headers=headers
            )
            historical_spot_prices = [SpotPrice(**s) for s in response.json()]
            self.__logger.info(f"Completed batch historical request for {reqs}")
            return historical_spot_prices
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")


# ======================================== FRED API ========================================
class FredApi:
    def __init__(self, user: str, base_url: str, api_key: str):
        self.__caller = user
        self.__base_url = base_url
        self.__api_key = api_key
        self.__logger = logging.getLogger("Fred-API")

    def set_api_key(self, api_key: str):
        self.__api_key = api_key
        self.__logger.info("Fred API key updated")

    def get_observations(
        self, operation: FredOperation, params: dict[str, Any]
    ) -> list[Observation]:
        # default file type is XML so if not provided in params dictionary, manually set to json
        if params.get("file_type") is None:
            params["file_type"] = "json"
        headers = dict(apiKey=self.__api_key, caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching observations for {operation}")
            response = requests.get(
                f"{self.__base_url}/fred/observations/{operation}",
                params=params,
                headers=headers,
            )
            observations = [Observation(**o) for o in response.json()["observations"]]
            self.__logger.info(f"Completed request for {operation}")
            return observations
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_most_recent_observation(
        self, operation: FredOperation, params: dict[str, Any]
    ) -> Observation:
        # default file type is XML so if not provided in params dictionary, manually set to json
        if params.get("file_type") is None:
            params["file_type"] = "json"
        headers = dict(apiKey=self.__api_key, caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching most recent observation for {operation}")
            response = requests.get(
                f"{self.__base_url}/fred/observations/current/{operation}",
                params=params,
                headers=headers,
            )
            observation = Observation(**response.json())
            self.__logger.info(f"Completed request for {operation}")
            return observation
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")


# ======================================== STOCK API ========================================
class StockApi:
    def __init__(self, user: str, base_url: str, api_key: str):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__caller = user
        self.__logger = logging.getLogger("Stock-API")

    def set_api_key(self, api_key: str):
        self.__api_key = api_key
        self.__logger.info("Stock API key updated")

    def get_stock_price(self, symbol: str) -> StockPrice:
        params = {"symbol": symbol}
        headers = dict(apiKey=self.__api_key, caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching stock price for {symbol}")
            response = requests.get(
                f"{self.__base_url}/stocks", params=params, headers=headers
            )
            stock_price = StockPrice(**response.json())
            self.__logger.info(f"Completed stock price request for {symbol}")
            return stock_price
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")

    def get_multiple_stock_prices(self, symbols: list[str]) -> list[StockPrice]:
        params = {"symbols": ",".join(symbols)}
        headers = dict(apiKey=self.__api_key, caller=self.__caller)

        try:
            self.__logger.debug(f"Fetching multiple stock prices for {symbols}")
            response = requests.get(
                f"{self.__base_url}/stocks/batch", params=params, headers=headers
            )

            stock_prices = [StockPrice(**o) for o in response.json()]
            self.__logger.info(f"Completed batch stock price request for {symbols}")
            return stock_prices
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"RequestException: {e}")


# ======================================== ECON SERVER CLIENT (CONTAINS ALL APIS) ========================================


class EconServerClient:
    def __init__(self, user: str, base_url: str, fred_api_key: str, stock_api_key: str):
        self.crypto_api = CryptoApi(user, base_url)
        self.fred_api = FredApi(user, base_url, fred_api_key)
        self.stock_api = StockApi(user, base_url, stock_api_key)
