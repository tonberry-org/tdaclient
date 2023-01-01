# generated by datamodel-codegen:
#   filename:  get_order_response.json
#   timestamp: 2023-01-01T22:45:43+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Literal


class Session(Enum):
    NORMAL = 'NORMAL'
    AM = 'AM'
    PM = 'PM'
    SEAMLESS = 'SEAMLESS'


class Duration(Enum):
    DAY = 'DAY'
    GOOD_TILL_CANCEL = 'GOOD_TILL_CANCEL'
    FILL_OR_KILL = 'FILL_OR_KILL'


class OrderType(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'
    STOP = 'STOP'
    STOP_LIMIT = 'STOP_LIMIT'
    TRAILING_STOP = 'TRAILING_STOP'
    MARKET_ON_CLOSE = 'MARKET_ON_CLOSE'
    EXERCISE = 'EXERCISE'
    TRAILING_STOP_LIMIT = 'TRAILING_STOP_LIMIT'
    NET_DEBIT = 'NET_DEBIT'
    NET_CREDIT = 'NET_CREDIT'
    NET_ZERO = 'NET_ZERO'


class CancelTime(BaseModel):
    date: Optional[str] = None
    shortFormat: Optional[bool] = False


class ComplexOrderStrategyType(Enum):
    NONE = 'NONE'
    COVERED = 'COVERED'
    VERTICAL = 'VERTICAL'
    BACK_RATIO = 'BACK_RATIO'
    CALENDAR = 'CALENDAR'
    DIAGONAL = 'DIAGONAL'
    STRADDLE = 'STRADDLE'
    STRANGLE = 'STRANGLE'
    COLLAR_SYNTHETIC = 'COLLAR_SYNTHETIC'
    BUTTERFLY = 'BUTTERFLY'
    CONDOR = 'CONDOR'
    IRON_CONDOR = 'IRON_CONDOR'
    VERTICAL_ROLL = 'VERTICAL_ROLL'
    COLLAR_WITH_STOCK = 'COLLAR_WITH_STOCK'
    DOUBLE_DIAGONAL = 'DOUBLE_DIAGONAL'
    UNBALANCED_BUTTERFLY = 'UNBALANCED_BUTTERFLY'
    UNBALANCED_CONDOR = 'UNBALANCED_CONDOR'
    UNBALANCED_IRON_CONDOR = 'UNBALANCED_IRON_CONDOR'
    UNBALANCED_VERTICAL_ROLL = 'UNBALANCED_VERTICAL_ROLL'
    CUSTOM = 'CUSTOM'


class RequestedDestination(Enum):
    INET = 'INET'
    ECN_ARCA = 'ECN_ARCA'
    CBOE = 'CBOE'
    AMEX = 'AMEX'
    PHLX = 'PHLX'
    ISE = 'ISE'
    BOX = 'BOX'
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'
    BATS = 'BATS'
    C2 = 'C2'
    AUTO = 'AUTO'


class StopPriceLinkBasis(Enum):
    MANUAL = 'MANUAL'
    BASE = 'BASE'
    TRIGGER = 'TRIGGER'
    LAST = 'LAST'
    BID = 'BID'
    ASK = 'ASK'
    ASK_BID = 'ASK_BID'
    MARK = 'MARK'
    AVERAGE = 'AVERAGE'


class StopPriceLinkType(Enum):
    VALUE = 'VALUE'
    PERCENT = 'PERCENT'
    TICK = 'TICK'


class StopType(Enum):
    STANDARD = 'STANDARD'
    BID = 'BID'
    ASK = 'ASK'
    LAST = 'LAST'
    MARK = 'MARK'


class PriceLinkBasis(Enum):
    MANUAL = 'MANUAL'
    BASE = 'BASE'
    TRIGGER = 'TRIGGER'
    LAST = 'LAST'
    BID = 'BID'
    ASK = 'ASK'
    ASK_BID = 'ASK_BID'
    MARK = 'MARK'
    AVERAGE = 'AVERAGE'


class PriceLinkType(Enum):
    VALUE = 'VALUE'
    PERCENT = 'PERCENT'
    TICK = 'TICK'


class TaxLotMethod(Enum):
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    HIGH_COST = 'HIGH_COST'
    LOW_COST = 'LOW_COST'
    AVERAGE_COST = 'AVERAGE_COST'
    SPECIFIC_LOT = 'SPECIFIC_LOT'


class OrderLegType(Enum):
    EQUITY = 'EQUITY'
    OPTION = 'OPTION'
    INDEX = 'INDEX'
    MUTUAL_FUND = 'MUTUAL_FUND'
    CASH_EQUIVALENT = 'CASH_EQUIVALENT'
    FIXED_INCOME = 'FIXED_INCOME'
    CURRENCY = 'CURRENCY'


class Instruction(Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    BUY_TO_COVER = 'BUY_TO_COVER'
    SELL_SHORT = 'SELL_SHORT'
    BUY_TO_OPEN = 'BUY_TO_OPEN'
    BUY_TO_CLOSE = 'BUY_TO_CLOSE'
    SELL_TO_OPEN = 'SELL_TO_OPEN'
    SELL_TO_CLOSE = 'SELL_TO_CLOSE'
    EXCHANGE = 'EXCHANGE'


class PositionEffect(Enum):
    OPENING = 'OPENING'
    CLOSING = 'CLOSING'
    AUTOMATIC = 'AUTOMATIC'


class QuantityType(Enum):
    ALL_SHARES = 'ALL_SHARES'
    DOLLARS = 'DOLLARS'
    SHARES = 'SHARES'


class SpecialInstruction(Enum):
    ALL_OR_NONE = 'ALL_OR_NONE'
    DO_NOT_REDUCE = 'DO_NOT_REDUCE'
    ALL_OR_NONE_DO_NOT_REDUCE = 'ALL_OR_NONE_DO_NOT_REDUCE'


class OrderStrategyType(Enum):
    SINGLE = 'SINGLE'
    OCO = 'OCO'
    TRIGGER = 'TRIGGER'


class Status(Enum):
    AWAITING_PARENT_ORDER = 'AWAITING_PARENT_ORDER'
    AWAITING_CONDITION = 'AWAITING_CONDITION'
    AWAITING_MANUAL_REVIEW = 'AWAITING_MANUAL_REVIEW'
    ACCEPTED = 'ACCEPTED'
    AWAITING_UR_OUT = 'AWAITING_UR_OUT'
    PENDING_ACTIVATION = 'PENDING_ACTIVATION'
    QUEUED = 'QUEUED'
    WORKING = 'WORKING'
    REJECTED = 'REJECTED'
    PENDING_CANCEL = 'PENDING_CANCEL'
    CANCELED = 'CANCELED'
    PENDING_REPLACE = 'PENDING_REPLACE'
    REPLACED = 'REPLACED'
    FILLED = 'FILLED'
    EXPIRED = 'EXPIRED'


class ActivityType(Enum):
    EXECUTION = 'EXECUTION'
    ORDER_ACTION = 'ORDER_ACTION'


class OrderActivityCollectionItem(BaseModel):
    activityType: Optional[ActivityType] = None


class Instrument(BaseModel):
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None


class FixedIncome(Instrument):
    assetType: Literal['FIXED_INCOME']
    maturityDate: Optional[datetime] = None
    variableRate: Optional[float] = None
    factor: Optional[float] = None


class Type(Enum):
    NOT_APPLICABLE = 'NOT_APPLICABLE'
    OPEN_END_NON_TAXABLE = 'OPEN_END_NON_TAXABLE'
    OPEN_END_TAXABLE = 'OPEN_END_TAXABLE'
    NO_LOAD_NON_TAXABLE = 'NO_LOAD_NON_TAXABLE'
    NO_LOAD_TAXABLE = 'NO_LOAD_TAXABLE'


class MutualFund(Instrument):
    assetType: Literal['MUTUAL_FUND']
    type: Optional[Type] = None


class Type1(Enum):
    SAVINGS = 'SAVINGS'
    MONEY_MARKET_FUND = 'MONEY_MARKET_FUND'


class CashEquivalent(Instrument):
    assetType: Literal['CASH_EQUIVALENT']
    type: Optional[Type1] = None


class Type2(Enum):
    VANILLA = 'VANILLA'
    BINARY = 'BINARY'
    BARRIER = 'BARRIER'


class PutCall(Enum):
    PUT = 'PUT'
    CALL = 'CALL'


class CurrencyType(Enum):
    USD = 'USD'
    CAD = 'CAD'
    EUR = 'EUR'
    JPY = 'JPY'


class Index(Instrument):
    assetType: Literal['INDEX']


class Currency(Instrument):
    assetType: Literal['CURRENCY']


class AssetTypeEnum(Enum):
    EQUITY = 'EQUITY'
    OPTION = 'OPTION'
    INDEX = 'INDEX'
    MUTUAL_FUND = 'MUTUAL_FUND'
    CASH_EQUIVALENT = 'CASH_EQUIVALENT'
    FIXED_INCOME = 'FIXED_INCOME'
    CURRENCY = 'CURRENCY'


class ActivityType1(Enum):
    EXECUTION = 'EXECUTION'
    ORDER_ACTION = 'ORDER_ACTION'


class ExecutionLeg(BaseModel):
    legId: Optional[int] = None
    quantity: Optional[float] = None
    mismarkedQuantity: Optional[float] = None
    price: Optional[float] = None
    time: Optional[datetime] = None


class Execution(BaseModel):
    activityType: Optional[ActivityType1] = None
    executionType: Optional[Literal['FILL']] = None
    quantity: Optional[float] = None
    orderRemainingQuantity: Optional[float] = None
    executionLegs: Optional[List[ExecutionLeg]] = None


class Equity(Instrument):
    assetType: Literal['EQUITY']


class OptionDeliverable(BaseModel):
    symbol: Optional[str] = None
    deliverableUnits: Optional[float] = None
    currencyType: Optional[CurrencyType] = None
    assetType: Optional[AssetTypeEnum] = None


class Option(Instrument):
    assetType: Literal['OPTION']
    type: Optional[Type2] = None
    putCall: Optional[PutCall] = None
    underlyingSymbol: Optional[str] = None
    optionMultiplier: Optional[int] = None
    optionDeliverables: Optional[List[OptionDeliverable]] = None


class OrderLegCollectionItem(BaseModel):
    orderLegType: Optional[OrderLegType] = None
    legId: Optional[int] = None
    instrument: Optional[
        Union[Equity, FixedIncome, MutualFund, CashEquivalent, Option, Currency, Index]
    ] = Field(None, discriminator='assetType')
    instruction: Optional[Instruction] = None
    positionEffect: Optional[PositionEffect] = None
    quantity: Optional[float] = None
    quantityType: Optional[QuantityType] = None


class Response(BaseModel):
    session: Optional[Session] = None
    duration: Optional[Duration] = None
    orderType: Optional[OrderType] = None
    cancelTime: Optional[CancelTime] = None
    complexOrderStrategyType: Optional[ComplexOrderStrategyType] = None
    quantity: Optional[float] = None
    filledQuantity: Optional[float] = None
    remainingQuantity: Optional[float] = None
    requestedDestination: Optional[RequestedDestination] = None
    destinationLinkName: Optional[str] = None
    releaseTime: Optional[datetime] = None
    stopPrice: Optional[float] = None
    stopPriceLinkBasis: Optional[StopPriceLinkBasis] = None
    stopPriceLinkType: Optional[StopPriceLinkType] = None
    stopPriceOffset: Optional[float] = None
    stopType: Optional[StopType] = None
    priceLinkBasis: Optional[PriceLinkBasis] = None
    priceLinkType: Optional[PriceLinkType] = None
    price: Optional[float] = None
    taxLotMethod: Optional[TaxLotMethod] = None
    orderLegCollection: Optional[List[OrderLegCollectionItem]] = None
    activationPrice: Optional[float] = None
    specialInstruction: Optional[SpecialInstruction] = None
    orderStrategyType: Optional[OrderStrategyType] = None
    orderId: Optional[int] = None
    cancelable: Optional[bool] = False
    editable: Optional[bool] = False
    status: Optional[Status] = None
    enteredTime: Optional[datetime] = None
    closeTime: Optional[datetime] = None
    tag: Optional[str] = None
    accountId: Optional[int] = None
    orderActivityCollection: Optional[List[OrderActivityCollectionItem]] = None
    replacingOrderCollection: Optional[List] = None
    childOrderStrategies: Optional[List] = None
    statusDescription: Optional[str] = None


class GetOrderResponse(BaseModel):
    response: Optional[Response] = None
