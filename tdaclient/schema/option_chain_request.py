# generated by datamodel-codegen:
#   filename:  option_chain_request.json
#   timestamp: 2023-01-03T22:58:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from . import authorization


class ContractType(str, Enum):
    CALL = 'CALL'
    PUT = 'PUT'
    ALL = 'ALL'


class Strategy(str, Enum):
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


class Range(str, Enum):
    ITM = 'ITM'
    NTM = 'NTM'
    OTM = 'OTM'
    SAK = 'SAK'
    SBK = 'SBK'
    SNK = 'SNK'
    ALL = 'ALL'


class ExpMonth(str, Enum):
    ALL = 'ALL'
    JAN = 'JAN'
    FEB = 'FEB'
    MAR = 'MAR'
    APR = 'APR'
    MAY = 'MAY'
    JUN = 'JUN'
    JUL = 'JUL'
    AUG = 'AUG'
    SEP = 'SEP'
    OCT = 'OCT'
    NOV = 'NOV'
    DEV = 'DEV'


class OptionType(str, Enum):
    S = 'S'
    NS = 'NS'
    ALL = 'ALL'


class OptionChainInput(BaseModel):
    apikey: Optional[str] = None
    symbol: Optional[str] = None
    contractType: Optional[ContractType] = None
    strikeCount: Optional[int] = None
    includeQuotes: Optional[bool] = None
    strategy: Optional[Strategy] = None
    interval: Optional[int] = None
    strike: Optional[float] = None
    range: Optional[Range] = None
    fromDate: Optional[str] = None
    toDate: Optional[str] = None
    volatility: Optional[str] = None
    underlyingPrice: Optional[float] = None
    interestRate: Optional[float] = None
    daysToExpiration: Optional[float] = None
    expMonth: Optional[ExpMonth] = None
    optionType: Optional[OptionType] = None


class OptionChainRequest(BaseModel):
    authorization: authorization.Authorization
    input: OptionChainInput
