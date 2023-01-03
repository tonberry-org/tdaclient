# generated by datamodel-codegen:
#   filename:  common_quotes.json
#   timestamp: 2023-01-03T23:05:32+00:00

from __future__ import annotations

from decimal import Decimal
from typing import Any, Literal, Optional

from pydantic import BaseModel, Extra, Field


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Any


class MutualFundQuote(BaseModel):
    assetType: Optional[Literal['MUTUAL_FUND']] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    closePrice: Optional[Decimal] = None
    netChange: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    exchange: Optional[str] = None
    exchangeName: Optional[str] = None
    digits: Optional[int] = None
    field_52WkHigh: Optional[Decimal] = Field(None, alias='52WkHigh')
    field_52WkLow: Optional[Decimal] = Field(None, alias='52WkLow')
    nAV: Optional[Decimal] = None
    peRatio: Optional[Decimal] = None
    divAmount: Optional[Decimal] = None
    divYield: Optional[Decimal] = None
    divDate: Optional[str] = None
    securityStatus: Optional[str] = None


class FutureQuote(BaseModel):
    assetType: Optional[Literal['FUTURE']] = None
    symbol: Optional[str] = None
    bidPriceInDouble: Optional[Decimal] = None
    askPriceInDouble: Optional[Decimal] = None
    lastPriceInDouble: Optional[Decimal] = None
    bidId: Optional[str] = None
    askId: Optional[str] = None
    highPriceInDouble: Optional[Decimal] = None
    lowPriceInDouble: Optional[Decimal] = None
    closePriceInDouble: Optional[Decimal] = None
    exchange: Optional[str] = None
    description: Optional[str] = None
    lastId: Optional[str] = None
    openPriceInDouble: Optional[Decimal] = None
    changeInDouble: Optional[Decimal] = None
    futurePercentChange: Optional[Decimal] = None
    exchangeName: Optional[str] = None
    securityStatus: Optional[str] = None
    openInterest: Optional[Decimal] = None
    mark: Optional[Decimal] = None
    tick: Optional[Decimal] = None
    tickAmount: Optional[Decimal] = None
    product: Optional[str] = None
    futurePriceFormat: Optional[str] = None
    futureTradingHours: Optional[str] = None
    futureIsTradable: Optional[bool] = None
    futureMultiplier: Optional[Decimal] = None
    futureIsActive: Optional[bool] = None
    futureSettlementPrice: Optional[Decimal] = None
    futureActiveSymbol: Optional[str] = None
    futureExpirationDate: Optional[str] = None


class FutureOptionQuote(BaseModel):
    assetType: Optional[Literal['OPTION']] = None
    symbol: Optional[str] = None
    bidPriceInDouble: Optional[Decimal] = None
    askPriceInDouble: Optional[Decimal] = None
    lastPriceInDouble: Optional[Decimal] = None
    highPriceInDouble: Optional[Decimal] = None
    lowPriceInDouble: Optional[Decimal] = None
    closePriceInDouble: Optional[Decimal] = None
    description: Optional[str] = None
    openPriceInDouble: Optional[Decimal] = None
    netChangeInDouble: Optional[Decimal] = None
    openInterest: Optional[Decimal] = None
    exchangeName: Optional[str] = None
    securityStatus: Optional[str] = None
    volatility: Optional[Decimal] = None
    moneyIntrinsicValueInDouble: Optional[Decimal] = None
    multiplierInDouble: Optional[Decimal] = None
    digits: Optional[int] = None
    strikePriceInDouble: Optional[Decimal] = None
    contractType: Optional[str] = None
    underlying: Optional[str] = None
    timeValueInDouble: Optional[Decimal] = None
    deltaInDouble: Optional[Decimal] = None
    gammaInDouble: Optional[Decimal] = None
    thetaInDouble: Optional[Decimal] = None
    vegaInDouble: Optional[Decimal] = None
    rhoInDouble: Optional[Decimal] = None
    mark: Optional[Decimal] = None
    tick: Optional[Decimal] = None
    tickAmount: Optional[Decimal] = None
    futureIsTradable: Optional[bool] = None
    futureTradingHours: Optional[str] = None
    futurePercentChange: Optional[Decimal] = None
    futureIsActive: Optional[bool] = None
    futureExpirationDate: Optional[int] = None
    expirationType: Optional[str] = None
    exerciseType: Optional[str] = None
    inTheMoney: Optional[bool] = None


class IndexQuote(BaseModel):
    assetType: Optional[Literal['INDEX']] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    lastPrice: Optional[Decimal] = None
    openPrice: Optional[Decimal] = None
    highPrice: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    closePrice: Optional[Decimal] = None
    netChange: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    exchange: Optional[str] = None
    exchangeName: Optional[str] = None
    digits: Optional[int] = None
    field_52WkHigh: Optional[Decimal] = Field(None, alias='52WkHigh')
    field_52WkLow: Optional[Decimal] = Field(None, alias='52WkLow')
    securityStatus: Optional[str] = None


class OptionQuote(BaseModel):
    assetType: Optional[Literal['OPTION']] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    bidPrice: Optional[Decimal] = None
    bidSize: Optional[int] = None
    askPrice: Optional[Decimal] = None
    askSize: Optional[int] = None
    lastPrice: Optional[Decimal] = None
    lastSize: Optional[int] = None
    openPrice: Optional[Decimal] = None
    highPrice: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    closePrice: Optional[Decimal] = None
    netChange: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    quoteTimeInLong: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    mark: Optional[Decimal] = None
    openInterest: Optional[Decimal] = None
    volatility: Optional[Decimal] = None
    moneyIntrinsicValue: Optional[Decimal] = None
    multiplier: Optional[Decimal] = None
    strikePrice: Optional[Decimal] = None
    contractType: Optional[str] = None
    underlying: Optional[str] = None
    timeValue: Optional[Decimal] = None
    deliverables: Optional[str] = None
    delta: Optional[Decimal] = None
    gamma: Optional[Decimal] = None
    theta: Optional[Decimal] = None
    vega: Optional[Decimal] = None
    rho: Optional[Decimal] = None
    securityStatus: Optional[str] = None
    theoreticalOptionValue: Optional[Decimal] = None
    underlyingPrice: Optional[Decimal] = None
    uvExpirationType: Optional[str] = None
    exchange: Optional[str] = None
    exchangeName: Optional[str] = None
    settlementType: Optional[str] = None


class ForexQuote(BaseModel):
    assetType: Optional[Literal['FOREX']] = None
    symbol: Optional[str] = None
    bidPriceInDouble: Optional[Decimal] = None
    askPriceInDouble: Optional[Decimal] = None
    lastPriceInDouble: Optional[Decimal] = None
    highPriceInDouble: Optional[Decimal] = None
    lowPriceInDouble: Optional[Decimal] = None
    closePriceInDouble: Optional[Decimal] = None
    exchange: Optional[str] = None
    description: Optional[str] = None
    openPriceInDouble: Optional[Decimal] = None
    changeInDouble: Optional[Decimal] = None
    percentChange: Optional[Decimal] = None
    exchangeName: Optional[str] = None
    digits: Optional[int] = None
    securityStatus: Optional[str] = None
    tick: Optional[Decimal] = None
    tickAmount: Optional[Decimal] = None
    product: Optional[str] = None
    tradingHours: Optional[str] = None
    isTradable: Optional[bool] = None
    marketMaker: Optional[str] = None
    field_52WkHighInDouble: Optional[Decimal] = Field(None, alias='52WkHighInDouble')
    field_52WkLowInDouble: Optional[Decimal] = Field(None, alias='52WkLowInDouble')
    mark: Optional[Decimal] = None


class ETFQuote(BaseModel):
    assetType: Optional[Literal['ETF']] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    bidPrice: Optional[Decimal] = None
    bidSize: Optional[int] = None
    bidId: Optional[str] = None
    askPrice: Optional[Decimal] = None
    askSize: Optional[int] = None
    askId: Optional[str] = None
    lastPrice: Optional[Decimal] = None
    lastSize: Optional[int] = None
    lastId: Optional[str] = None
    openPrice: Optional[Decimal] = None
    highPrice: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    closePrice: Optional[Decimal] = None
    netChange: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    quoteTimeInLong: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    mark: Optional[Decimal] = None
    exchange: Optional[str] = None
    exchangeName: Optional[str] = None
    marginable: Optional[bool] = False
    shortable: Optional[bool] = False
    volatility: Optional[Decimal] = None
    digits: Optional[int] = None
    field_52WkHigh: Optional[Decimal] = Field(None, alias='52WkHigh')
    field_52WkLow: Optional[Decimal] = Field(None, alias='52WkLow')
    peRatio: Optional[Decimal] = None
    divAmount: Optional[Decimal] = None
    divYield: Optional[Decimal] = None
    divDate: Optional[str] = None
    securityStatus: Optional[str] = None
    regularMarketLastPrice: Optional[Decimal] = None
    regularMarketLastSize: Optional[int] = None
    regularMarketNetChange: Optional[Decimal] = None
    regularMarketTradeTimeInLong: Optional[int] = None


class EquitiesQuote(BaseModel):
    assetType: Optional[Literal['EQUITY']] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    bidPrice: Optional[Decimal] = None
    bidSize: Optional[int] = None
    bidId: Optional[str] = None
    askPrice: Optional[Decimal] = None
    askSize: Optional[int] = None
    askId: Optional[str] = None
    lastPrice: Optional[Decimal] = None
    lastSize: Optional[int] = None
    lastId: Optional[str] = None
    openPrice: Optional[Decimal] = None
    highPrice: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    closePrice: Optional[Decimal] = None
    netChange: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    quoteTimeInLong: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    mark: Optional[Decimal] = None
    exchange: Optional[str] = None
    exchangeName: Optional[str] = None
    marginable: Optional[bool] = False
    shortable: Optional[bool] = False
    volatility: Optional[Decimal] = None
    digits: Optional[int] = None
    field_52WkHigh: Optional[Decimal] = Field(None, alias='52WkHigh')
    field_52WkLow: Optional[Decimal] = Field(None, alias='52WkLow')
    peRatio: Optional[Decimal] = None
    divAmount: Optional[Decimal] = None
    divYield: Optional[Decimal] = None
    divDate: Optional[str] = None
    securityStatus: Optional[str] = None
    regularMarketLastPrice: Optional[Decimal] = None
    regularMarketLastSize: Optional[int] = None
    regularMarketNetChange: Optional[Decimal] = None
    regularMarketTradeTimeInLong: Optional[int] = None
