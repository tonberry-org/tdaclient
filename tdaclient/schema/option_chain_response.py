# generated by datamodel-codegen:
#   filename:  option_chain_response.json
#   timestamp: 2023-01-14T17:09:46+00:00

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel


class Strategy1(str, Enum):
    SINGLE = 'SINGLE'
    ANALYTICAL = 'ANALYTICAL'
    COVERED = 'COVERED'
    VERTICAL = 'VERTICAL'
    CALENDAR = 'CALENDAR'
    STRANGLE = 'STRANGLE'
    STRADDLE = 'STRADDLE'
    BUTTERFLY = 'BUTTERFLY'
    CONDOR = 'CONDOR'
    DIAGONAL = 'DIAGONAL'
    COLLAR = 'COLLAR'
    ROLL = 'ROLL'


class PutCall1(str, Enum):
    PUT = 'PUT'
    CALL = 'CALL'


class OptionDeliverablesListItem(BaseModel):
    symbol: Optional[str] = None
    assetType: Optional[str] = None
    deliverableUnits: Optional[str] = None
    currencyType: Optional[str] = None


class Option(BaseModel):
    putCall: Optional[PutCall1] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    exchangeName: Optional[str] = None
    bid: Optional[Decimal] = None
    ask: Optional[Decimal] = None
    lastPrice: Optional[Decimal] = None
    markPrice: Optional[Decimal] = None
    bidSize: Optional[int] = None
    askSize: Optional[int] = None
    lastSize: Optional[int] = None
    highPrice: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    openPrice: Optional[Decimal] = None
    closePrice: Optional[Decimal] = None
    totalVolume: Optional[int] = None
    quoteTimeInLong: Optional[int] = None
    tradeTimeInLong: Optional[int] = None
    netChange: Optional[Decimal] = None
    volatility: Optional[Decimal] = None
    delta: Optional[Decimal] = None
    gamma: Optional[Decimal] = None
    theta: Optional[Decimal] = None
    vega: Optional[Decimal] = None
    rho: Optional[Decimal] = None
    timeValue: Optional[Decimal] = None
    openInterest: Optional[Decimal] = None
    isInTheMoney: Optional[bool] = None
    theoreticalOptionValue: Optional[Decimal] = None
    theoreticalVolatility: Optional[Decimal] = None
    isMini: Optional[bool] = None
    isNonStandard: Optional[bool] = None
    optionDeliverablesList: Optional[List[OptionDeliverablesListItem]] = None
    strikePrice: Optional[Decimal] = None
    expirationDate: Optional[str] = None
    expirationType: Optional[str] = None
    multiplier: Optional[Decimal] = None
    settlementType: Optional[str] = None
    deliverableNote: Optional[str] = None
    isIndexOption: Optional[bool] = None
    percentChange: Optional[Decimal] = None
    markChange: Optional[Decimal] = None
    markPercentChange: Optional[Decimal] = None


class ExchangeName(str, Enum):
    IND = 'IND'
    ASE = 'ASE'
    NYS = 'NYS'
    NAS = 'NAS'
    NAP = 'NAP'
    PAC = 'PAC'
    OPR = 'OPR'
    BATS = 'BATS'


class Underlying(BaseModel):
    ask: Optional[Decimal] = None
    askSize: Optional[int] = None
    bid: Optional[Decimal] = None
    bidSize: Optional[int] = None
    change: Optional[Decimal] = None
    close: Optional[Decimal] = None
    delayed: Optional[bool] = None
    description: Optional[str] = None
    exchangeName: Optional[ExchangeName] = None
    fiftyTwoWeekHigh: Optional[Decimal] = None
    fiftyTwoWeekLow: Optional[Decimal] = None
    highPrice: Optional[Decimal] = None
    last: Optional[Decimal] = None
    lowPrice: Optional[Decimal] = None
    mark: Optional[Decimal] = None
    markChange: Optional[Decimal] = None
    markPercentChange: Optional[Decimal] = None
    openPrice: Optional[Decimal] = None
    percentChange: Optional[Decimal] = None
    quoteTime: Optional[int] = None
    symbol: Optional[str] = None
    totalVolume: Optional[int] = None
    tradeTime: Optional[int] = None


class ExpirationDate(BaseModel):
    date: Optional[str] = None


class OptionDeliverables(BaseModel):
    symbol: Optional[str] = None
    assetType: Optional[str] = None
    deliverableUnits: Optional[str] = None
    currencyType: Optional[str] = None


class OptionChainOutput(BaseModel):
    symbol: str
    status: Optional[str] = None
    underlying: Optional[Underlying] = None
    strategy: Optional[Strategy1] = None
    interval: Optional[Decimal] = None
    isDelayed: Optional[bool] = None
    isIndex: Optional[bool] = None
    daysToExpiration: Decimal
    interestRate: Decimal
    underlyingPrice: Decimal
    volatility: Decimal
    callExpDateMap: Dict[str, Dict[str, List[Option]]]
    putExpDateMap: Dict[str, Dict[str, List[Option]]]


class OptionChainResponse(BaseModel):
    output: OptionChainOutput
