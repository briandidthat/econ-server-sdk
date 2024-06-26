from datetime import date

from enum import StrEnum

from typing import List

from pydantic import BaseModel, Field, ConfigDict

# CRYPTO AND STOCK MODELS


class AssetPrice(BaseModel):
    symbol: str
    price: str
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
    model_config = ConfigDict(populate_by_name=True)

    symbol: str
    start_date: str = Field(
        alias="startDate", default=date.today().strftime("%Y-%m-%d")
    )
    end_date: str = Field(alias="endDate", default=date.today().strftime("%Y-%m-%d"))


class BatchRequest(BaseModel):
    requests: List[Request]


class BatchResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    asset_prices: List[AssetPrice] = Field(alias="assetPrices")


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
