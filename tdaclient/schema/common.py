# generated by datamodel-codegen:
#   filename:  common.json
#   timestamp: 2023-01-14T17:09:46+00:00

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Extra


class Model(BaseModel):
    pass

    class Config:
        extra = Extra.forbid


class Instrument(BaseModel):
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None


class Equity(Instrument):
    assetType: Literal['EQUITY']


class FixedIncome(Instrument):
    assetType: Literal['FIXED_INCOME']
    maturityDate: Optional[datetime] = None
    variableRate: Optional[Decimal] = None
    factor: Optional[Decimal] = None


class Type(str, Enum):
    NOT_APPLICABLE = 'NOT_APPLICABLE'
    OPEN_END_NON_TAXABLE = 'OPEN_END_NON_TAXABLE'
    OPEN_END_TAXABLE = 'OPEN_END_TAXABLE'
    NO_LOAD_NON_TAXABLE = 'NO_LOAD_NON_TAXABLE'
    NO_LOAD_TAXABLE = 'NO_LOAD_TAXABLE'


class MutualFund(Instrument):
    assetType: Literal['MUTUAL_FUND']
    type: Optional[Type] = None


class Type1(str, Enum):
    SAVINGS = 'SAVINGS'
    MONEY_MARKET_FUND = 'MONEY_MARKET_FUND'


class CashEquivalent(Instrument):
    assetType: Literal['CASH_EQUIVALENT']
    type: Optional[Type1] = None


class Type2(str, Enum):
    VANILLA = 'VANILLA'
    BINARY = 'BINARY'
    BARRIER = 'BARRIER'


class PutCall(str, Enum):
    PUT = 'PUT'
    CALL = 'CALL'


class CurrencyType(str, Enum):
    USD = 'USD'
    CAD = 'CAD'
    EUR = 'EUR'
    JPY = 'JPY'


class Index(Instrument):
    assetType: Literal['INDEX']


class Currency(Instrument):
    assetType: Literal['CURRENCY']


class AssetTypeEnum(str, Enum):
    EQUITY = 'EQUITY'
    OPTION = 'OPTION'
    INDEX = 'INDEX'
    MUTUAL_FUND = 'MUTUAL_FUND'
    CASH_EQUIVALENT = 'CASH_EQUIVALENT'
    FIXED_INCOME = 'FIXED_INCOME'
    CURRENCY = 'CURRENCY'


class ActivityType1(str, Enum):
    EXECUTION = 'EXECUTION'
    ORDER_ACTION = 'ORDER_ACTION'


class ExecutionLeg(BaseModel):
    legId: Optional[int] = None
    quantity: Optional[Decimal] = None
    mismarkedQuantity: Optional[Decimal] = None
    price: Optional[Decimal] = None
    time: Optional[datetime] = None


class Execution(BaseModel):
    activityType: Optional[ActivityType1] = None
    executionType: Optional[Literal['FILL']] = None
    quantity: Optional[Decimal] = None
    orderRemainingQuantity: Optional[Decimal] = None
    executionLegs: Optional[List[ExecutionLeg]] = None


class OptionDeliverable(BaseModel):
    symbol: Optional[str] = None
    deliverableUnits: Optional[Decimal] = None
    currencyType: Optional[CurrencyType] = None
    assetType: Optional[AssetTypeEnum] = None


class Option(Instrument):
    assetType: Literal['OPTION']
    type: Optional[Type2] = None
    putCall: PutCall
    underlyingSymbol: str
    optionMultiplier: Optional[int] = None
    optionDeliverables: Optional[List[OptionDeliverable]] = None
