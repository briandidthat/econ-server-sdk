from enum import StrEnum

from typing import List

from pydantic import BaseModel, Field, ConfigDict


# CRYPTO API MODELS
class SpotPrice(BaseModel):
    symbol: str
    currency: str
    amount: str
    date: str


class Statistic(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    symbol: str
    start_price: str = Field(alias="startPrice")
    end_price: str = Field(alias="endPrice")
    price_change: str = Field(alias="priceChange")
    percent_change: str = Field(alias="percentChange")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    time_frame: str = Field(alias="timeFrame")


class Request(BaseModel):
    symbol: str
    date: str


class BatchRequest(BaseModel):
    requests: List[Request]


class BatchResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    spot_prices: List[SpotPrice] = Field(alias="spotPrices")


# STOCK API MODELS
class StockPrice(BaseModel):
    symbol: str
    price: str


# FRED API MODELS
class FredOperation(StrEnum):
    """
    This enum contains the FRED series id's that are relevant to this project
    """

    SP_500 = "SP500"
    NASDAQ = "NASDAQ100"
    CORE_CPI = "CPILFESL"
    STICKY_CPI = "CORESTICKM159SFRBATL"
    TOTAL_PUBLIC_DEBT = "GFDEBTN"
    AVERAGE_MORTGAGE_RATE = "MORTGAGE30US"
    AVERAGE_HOME_SALE_PRICE = "ASPUS"
    DEBT_TO_GDP = "GFDEGDQ188S"
    ONE_YEAR_TREASURY_YIELD = "DGS1"
    FIVE_YEAR_TREASURY_YIELD = "DGS5"
    TEN_YEAR_TREASURY_YIELD = "DGS10"
    UNEMPLOYMENT_RATE = "U2RATE"
    FEDERAL_FUNDS_RATE = "FEDFUNDS"
    DELINQUENCY_RATE = "DRCCLACBS"


class Observation(BaseModel):
    realtime_start: str
    realtime_end: str
    date: str
    value: str


class FredResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    observation_start: str = Field(alias="observationStart")
    observation_end: str = Field(alias="observationEnd")
    count: int
    observations: List[Observation]
