# generated by datamodel-codegen:
#   filename:  get_order_response.json
#   timestamp: 2023-01-02T19:10:25+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from . import common


class Session1(str, Enum):
    NORMAL = 'NORMAL'
    AM = 'AM'
    PM = 'PM'
    SEAMLESS = 'SEAMLESS'


class Duration1(str, Enum):
    DAY = 'DAY'
    GOOD_TILL_CANCEL = 'GOOD_TILL_CANCEL'
    FILL_OR_KILL = 'FILL_OR_KILL'


class OrderType1(str, Enum):
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


class CancelTime1(BaseModel):
    date: Optional[str] = None
    shortFormat: Optional[bool] = False


class ComplexOrderStrategyType1(str, Enum):
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


class RequestedDestination1(str, Enum):
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


class StopPriceLinkBasis1(str, Enum):
    MANUAL = 'MANUAL'
    BASE = 'BASE'
    TRIGGER = 'TRIGGER'
    LAST = 'LAST'
    BID = 'BID'
    ASK = 'ASK'
    ASK_BID = 'ASK_BID'
    MARK = 'MARK'
    AVERAGE = 'AVERAGE'


class StopPriceLinkType1(str, Enum):
    VALUE = 'VALUE'
    PERCENT = 'PERCENT'
    TICK = 'TICK'


class StopType1(str, Enum):
    STANDARD = 'STANDARD'
    BID = 'BID'
    ASK = 'ASK'
    LAST = 'LAST'
    MARK = 'MARK'


class PriceLinkBasis1(str, Enum):
    MANUAL = 'MANUAL'
    BASE = 'BASE'
    TRIGGER = 'TRIGGER'
    LAST = 'LAST'
    BID = 'BID'
    ASK = 'ASK'
    ASK_BID = 'ASK_BID'
    MARK = 'MARK'
    AVERAGE = 'AVERAGE'


class PriceLinkType1(str, Enum):
    VALUE = 'VALUE'
    PERCENT = 'PERCENT'
    TICK = 'TICK'


class TaxLotMethod1(str, Enum):
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    HIGH_COST = 'HIGH_COST'
    LOW_COST = 'LOW_COST'
    AVERAGE_COST = 'AVERAGE_COST'
    SPECIFIC_LOT = 'SPECIFIC_LOT'


class OrderLegType1(str, Enum):
    EQUITY = 'EQUITY'
    OPTION = 'OPTION'
    INDEX = 'INDEX'
    MUTUAL_FUND = 'MUTUAL_FUND'
    CASH_EQUIVALENT = 'CASH_EQUIVALENT'
    FIXED_INCOME = 'FIXED_INCOME'
    CURRENCY = 'CURRENCY'


class Instruction1(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    BUY_TO_COVER = 'BUY_TO_COVER'
    SELL_SHORT = 'SELL_SHORT'
    BUY_TO_OPEN = 'BUY_TO_OPEN'
    BUY_TO_CLOSE = 'BUY_TO_CLOSE'
    SELL_TO_OPEN = 'SELL_TO_OPEN'
    SELL_TO_CLOSE = 'SELL_TO_CLOSE'
    EXCHANGE = 'EXCHANGE'


class PositionEffect1(str, Enum):
    OPENING = 'OPENING'
    CLOSING = 'CLOSING'
    AUTOMATIC = 'AUTOMATIC'


class QuantityType1(str, Enum):
    ALL_SHARES = 'ALL_SHARES'
    DOLLARS = 'DOLLARS'
    SHARES = 'SHARES'


class SpecialInstruction1(str, Enum):
    ALL_OR_NONE = 'ALL_OR_NONE'
    DO_NOT_REDUCE = 'DO_NOT_REDUCE'
    ALL_OR_NONE_DO_NOT_REDUCE = 'ALL_OR_NONE_DO_NOT_REDUCE'


class OrderStrategyType1(str, Enum):
    SINGLE = 'SINGLE'
    OCO = 'OCO'
    TRIGGER = 'TRIGGER'


class Status1(str, Enum):
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


class ActivityType2(str, Enum):
    EXECUTION = 'EXECUTION'
    ORDER_ACTION = 'ORDER_ACTION'


class OrderActivityCollectionItem1(BaseModel):
    activityType: Optional[ActivityType2] = None


class OrderLegCollectionItem1(BaseModel):
    orderLegType: Optional[OrderLegType1] = None
    legId: Optional[int] = None
    instrument: Optional[
        Union[
            common.Equity,
            common.FixedIncome,
            common.MutualFund,
            common.CashEquivalent,
            common.Option,
            common.Currency,
            common.Index,
        ]
    ] = Field(None, discriminator='assetType')
    instruction: Optional[Instruction1] = None
    positionEffect: Optional[PositionEffect1] = None
    quantity: Optional[float] = None
    quantityType: Optional[QuantityType1] = None


class GetOrderOutput(BaseModel):
    session: Optional[Session1] = None
    duration: Optional[Duration1] = None
    orderType: Optional[OrderType1] = None
    cancelTime: Optional[CancelTime1] = None
    complexOrderStrategyType: Optional[ComplexOrderStrategyType1] = None
    quantity: Optional[float] = None
    filledQuantity: Optional[float] = None
    remainingQuantity: Optional[float] = None
    requestedDestination: Optional[RequestedDestination1] = None
    destinationLinkName: Optional[str] = None
    releaseTime: Optional[datetime] = None
    stopPrice: Optional[float] = None
    stopPriceLinkBasis: Optional[StopPriceLinkBasis1] = None
    stopPriceLinkType: Optional[StopPriceLinkType1] = None
    stopPriceOffset: Optional[float] = None
    stopType: Optional[StopType1] = None
    priceLinkBasis: Optional[PriceLinkBasis1] = None
    priceLinkType: Optional[PriceLinkType1] = None
    price: Optional[float] = None
    taxLotMethod: Optional[TaxLotMethod1] = None
    orderLegCollection: Optional[List[OrderLegCollectionItem1]] = None
    activationPrice: Optional[float] = None
    specialInstruction: Optional[SpecialInstruction1] = None
    orderStrategyType: Optional[OrderStrategyType1] = None
    orderId: Optional[int] = None
    cancelable: Optional[bool] = False
    editable: Optional[bool] = False
    status: Optional[Status1] = None
    enteredTime: Optional[datetime] = None
    closeTime: Optional[datetime] = None
    tag: Optional[str] = None
    accountId: Optional[int] = None
    orderActivityCollection: Optional[List[OrderActivityCollectionItem1]] = None
    replacingOrderCollection: Optional[List] = None
    childOrderStrategies: Optional[List] = None
    statusDescription: Optional[str] = None


class GetOrderResponse(BaseModel):
    output: GetOrderOutput
