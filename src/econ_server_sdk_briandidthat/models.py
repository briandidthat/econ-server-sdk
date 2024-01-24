from enum import StrEnum

from pydantic import BaseModel, Field


# CRYPTO API MODELS
class SpotPrice(BaseModel):
    symbol: str
    currency: str
    amount: str
    date: str


class Statistic(BaseModel):
    symbol: str
    start_price: str = Field(alias="startPrice")
    end_price: str = Field(alias="endPrice")
    price_change: str = Field(alias="priceChange")
    percent_change: str = Field(alias="percentChange")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    time_frame: str = Field(alias="timeFrame")


# STOCK API MODELS
class StockPrice(BaseModel):
    symbol: str
    price: str


# FRED API MODELS
class FredOperation(StrEnum):
    """
    This enum contains the FRED series id's that we are interested in using (can add more later)
    """

    SP_500 = "sp500"
    NASDAQ = "nasdaq100"
    CORE_CPI = "coreCpi"
    STICKY_CPI = "stickyCpi"
    TOTAL_PUBLIC_DEBT = "totalPublicDebt"
    AVERAGE_MORTGAGE_RATE = "averageMortgageRate"
    AVERAGE_HOME_SALE_PRICE = "averageHomeSalePrice"
    DEBT_TO_GDP = "debtToGdp"
    ONE_YEAR_TREASURY_YIELD = "oneYearTreasuryYield"
    FIVE_YEAR_TREASURY_YIELD = "fiveYearTreasuryYield"
    TEN_YEAR_TREASURY_YIELD = "tenYearTreasuryYield"
    UNEMPLOYMENT_RATE = "unemploymentRate"
    FEDERAL_FUNDS_RATE = "federalFundsRate"


class Observation(BaseModel):
    realtime_start: str
    realtime_end: str
    date: str
    value: str
