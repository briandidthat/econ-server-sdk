import logging
from typing import Any, List

import httpx

from src.econ_server_sdk_briandidthat.models import (
    Observation,
    AssetPrice,
    FredOperation,
    Statistic,
    BatchRequest,
    BatchResponse,
)

logging.basicConfig(level=logging.INFO)


class CryptoApi:
    """This class encapsulates the logic for making crypto spot price requests from the price server\n
    Args:\n
        base_url: url of the deployed econ-server instance\n
    """

    def __init__(self, base_url: str):
        self.__base_url = base_url
        self.__logger = logging.getLogger("Crypto-API")

    def set_base_url(self, base_url: str):
        self.__base_url = base_url
        self.__logger.info("Base URL updated")

    def get_spot_price(self, symbol: str) -> AssetPrice:
        params = dict(symbol=symbol)

        try:
            response = httpx.get(f"{self.__base_url}/crypto/spot", params=params)
            spot_price = AssetPrice(**response.json())
            self.__logger.info(f"Completed spot price request. {spot_price}")
            return spot_price
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_historical_spot_price(self, symbol: str, date: str) -> AssetPrice:
        params = dict(symbol=symbol, date=date)

        try:
            response = httpx.get(
                f"{self.__base_url}/crypto/spot/historical", params=params
            )
            historical_spot_price = AssetPrice(**response.json())
            self.__logger.info(
                f"Completed historical spot price request. {historical_spot_price}"
            )
            return historical_spot_price
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_price_statistics(
        self, symbol: str, start_date: str, end_date: str
    ) -> Statistic:
        params = dict(symbol=symbol, startDate=start_date, endDate=end_date)

        try:
            response = httpx.get(
                f"{self.__base_url}/crypto/spot/statistics", params=params
            )
            statistic = Statistic(**response.json())
            self.__logger.info(f"Completed statistics request. {statistic}")
            return statistic
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_multiple_spot_prices(self, symbols: list[str]) -> BatchResponse:
        params = dict(symbols=",".join(symbols))

        try:
            response = httpx.get(f"{self.__base_url}/crypto/spot/batch", params=params)
            spot_prices = BatchResponse(**response.json())
            self.__logger.info(f"Completed batch request. {spot_prices}.")
            return spot_prices
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_multiple_historical_spot_prices(
        self, batch_request: BatchRequest
    ) -> BatchResponse:
        try:
            response = httpx.post(
                f"{self.__base_url}/crypto/spot/batch/historical",
                json=batch_request.model_dump_json(),
            )
            historical_spot_prices = BatchResponse(**response.json())
            self.__logger.info(
                f"Completed batch historical request. {historical_spot_prices}"
            )
            return historical_spot_prices
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")


# ======================================== FRED API ========================================
class FredApi:
    """This class contains the logic for making FRED requests\n
    Args:\n
        base_url: url of the deployed econ-server instance\n
        api_key: FRED api key
    """

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key
        self.__logger = logging.getLogger("Fred-API")

    def get_api_key(self) -> str:
        return self.__api_key

    def set_api_key(self, api_key: str):
        self.__api_key = api_key
        self.__logger.info("Fred API key updated")

    def set_base_url(self, base_url: str):
        self.__base_url = base_url
        self.__logger.info("Base URL updated")

    def get_observations(
        self, operation: FredOperation, params: dict[str, Any]
    ) -> List[Observation]:
        # default file type is XML so if not provided in params dictionary, manually set to json
        if params.get("file_type") is None:
            params["file_type"] = "json"
        headers = dict(apiKey=self.__api_key)

        try:
            response = httpx.get(
                f"{self.__base_url}/fred/observations/{operation}",
                params=params,
                headers=headers,
            )
            observations = [Observation(**o) for o in response.json()["observations"]]
            self.__logger.info(f"Completed request for {operation}")
            return observations
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_most_recent_observation(
        self, operation: FredOperation, params: dict[str, Any]
    ) -> Observation:
        # default file type is XML so if not provided in params dictionary, manually set to json
        if params.get("file_type") is None:
            params["file_type"] = "json"
        headers = dict(apiKey=self.__api_key)

        try:
            response = httpx.get(
                f"{self.__base_url}/fred/observations/current/{operation}",
                params=params,
                headers=headers,
            )
            observation = Observation(**response.json())
            self.__logger.info(f"Completed request for {operation}")
            return observation
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")


# ======================================== STOCK API ========================================
class StockApi:
    """This class encapsulates the logic for making stock price requests\n
    Args:\n
        base_url: url of the deployed econ-server instance\n
        api_key: Twelve data api key
    """

    def __init__(self, base_url: str, api_key: str):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__headers = dict(apiKey=api_key)
        self.__logger = logging.getLogger("Stock-API")

    def get_api_key(self) -> str:
        return self.__api_key

    def set_api_key(self, api_key: str):
        self.__api_key = api_key
        self.__headers = dict(apiKey=api_key)
        self.__logger.info("Stock API key updated")

    def set_base_url(self, base_url: str):
        self.__base_url = base_url
        self.__logger.info("Base URL updated")

    def get_stock_price(self, symbol: str) -> AssetPrice:
        params = dict(symbol=symbol)

        try:
            response = httpx.get(
                f"{self.__base_url}/stocks", params=params, headers=self.__headers
            )
            stock_price = AssetPrice(**response.json())
            self.__logger.info(f"Completed stock price request for {symbol}")
            return stock_price
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_historical_stock_price(self, symbol: str, date: str) -> AssetPrice:
        params = dict(symbol=symbol, date=date)

        try:
            response = httpx.get(
                f"{self.__base_url}/stocks/historical",
                params=params,
                headers=self.__headers,
            )
            stock_price = AssetPrice(**response.json())
            return stock_price
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_stock_price_statistics(self, symbol: str, start_date: str) -> Statistic:
        params = dict(symbol=symbol, startDate=start_date)

        try:
            response = httpx.get(
                f"{self.__base_url}/stocks/statistics",
                params=params,
                headers=self.__headers,
            )
            statistic = Statistic(**response.json())
            self.__logger.info("Completed statistic request for {symbol}")
            return statistic
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_multiple_stock_prices(self, symbols: list[str]) -> BatchResponse:
        params = dict(symbols=",".join(symbols))

        try:
            response = httpx.get(
                f"{self.__base_url}/stocks/batch", params=params, headers=self.__headers
            )
            batch_response = BatchResponse(**response.json())
            self.__logger.info(f"Completed batch stock price request for {symbols}")
            return batch_response
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")

    def get_multiple_historical_stock_prices(
        self, batchRequest: BatchRequest
    ) -> BatchResponse:
        try:
            response = httpx.post(
                f"{self.__base_url}/stocks/batch/historical",
                json=batchRequest.model_dump_json(),
                headers=self.__headers
            )
            batch_response = BatchResponse(**response.json())
            return batch_response
        except httpx.HTTPError as exc:
            self.__logger.error(f"RequestException: {exc}")


# ======================================== ECON SERVER CLIENT (CONTAINS ALL APIS) ========================================


class EconServerClient:
    """This class encapsulates the logic for making requests to the econ server\n
    Args:\n
        base_url: url of the deployed econ-server instance\n
        fred_api_key: FRED api key\n
        stock_api_key: Twelve data api key
    """

    def __init__(self, base_url: str, fred_api_key: str, stock_api_key: str):
        self.crypto_api = CryptoApi(base_url)
        self.fred_api = FredApi(base_url, fred_api_key)
        self.stock_api = StockApi(base_url, stock_api_key)

    def set_base_url(self, base_url: str):
        self.crypto_api.set_base_url(base_url)
        self.fred_api.set_base_url(base_url)
        self.stock_api.set_base_url(base_url)
