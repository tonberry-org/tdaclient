# generated by datamodel-codegen:
#   filename:  get_account_response.json
#   timestamp: 2023-01-03T23:05:32+00:00

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

from . import common


class Session2(str, Enum):
    NORMAL = 'NORMAL'
    AM = 'AM'
    PM = 'PM'
    SEAMLESS = 'SEAMLESS'


class Duration2(str, Enum):
    DAY = 'DAY'
    GOOD_TILL_CANCEL = 'GOOD_TILL_CANCEL'
    FILL_OR_KILL = 'FILL_OR_KILL'


class OrderType2(str, Enum):
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


class CancelTime2(BaseModel):
    date: Optional[str] = None
    shortFormat: Optional[bool] = False


class ComplexOrderStrategyType2(str, Enum):
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


class RequestedDestination2(str, Enum):
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


class StopPriceLinkBasis2(str, Enum):
    MANUAL = 'MANUAL'
    BASE = 'BASE'
    TRIGGER = 'TRIGGER'
    LAST = 'LAST'
    BID = 'BID'
    ASK = 'ASK'
    ASK_BID = 'ASK_BID'
    MARK = 'MARK'
    AVERAGE = 'AVERAGE'


class StopPriceLinkType2(str, Enum):
    VALUE = 'VALUE'
    PERCENT = 'PERCENT'
    TICK = 'TICK'


class StopType2(str, Enum):
    STANDARD = 'STANDARD'
    BID = 'BID'
    ASK = 'ASK'
    LAST = 'LAST'
    MARK = 'MARK'


class TaxLotMethod2(str, Enum):
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    HIGH_COST = 'HIGH_COST'
    LOW_COST = 'LOW_COST'
    AVERAGE_COST = 'AVERAGE_COST'
    SPECIFIC_LOT = 'SPECIFIC_LOT'


class OrderLegType2(str, Enum):
    EQUITY = 'EQUITY'
    OPTION = 'OPTION'
    INDEX = 'INDEX'
    MUTUAL_FUND = 'MUTUAL_FUND'
    CASH_EQUIVALENT = 'CASH_EQUIVALENT'
    FIXED_INCOME = 'FIXED_INCOME'
    CURRENCY = 'CURRENCY'


class Instruction2(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    BUY_TO_COVER = 'BUY_TO_COVER'
    SELL_SHORT = 'SELL_SHORT'
    BUY_TO_OPEN = 'BUY_TO_OPEN'
    BUY_TO_CLOSE = 'BUY_TO_CLOSE'
    SELL_TO_OPEN = 'SELL_TO_OPEN'
    SELL_TO_CLOSE = 'SELL_TO_CLOSE'
    EXCHANGE = 'EXCHANGE'


class PositionEffect2(str, Enum):
    OPENING = 'OPENING'
    CLOSING = 'CLOSING'
    AUTOMATIC = 'AUTOMATIC'


class QuantityType2(str, Enum):
    ALL_SHARES = 'ALL_SHARES'
    DOLLARS = 'DOLLARS'
    SHARES = 'SHARES'


class SpecialInstruction2(str, Enum):
    ALL_OR_NONE = 'ALL_OR_NONE'
    DO_NOT_REDUCE = 'DO_NOT_REDUCE'
    ALL_OR_NONE_DO_NOT_REDUCE = 'ALL_OR_NONE_DO_NOT_REDUCE'


class OrderStrategyType2(str, Enum):
    SINGLE = 'SINGLE'
    OCO = 'OCO'
    TRIGGER = 'TRIGGER'


class Status2(str, Enum):
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


class ActivityType3(str, Enum):
    EXECUTION = 'EXECUTION'
    ORDER_ACTION = 'ORDER_ACTION'


class OrderActivityCollectionItem2(BaseModel):
    activityType: Optional[ActivityType3] = None


class InitialBalances(BaseModel):
    accruedInterest: Optional[Decimal] = None
    availableFundsNonMarginableTrade: Optional[Decimal] = None
    bondValue: Optional[Decimal] = None
    buyingPower: Optional[Decimal] = None
    cashBalance: Optional[Decimal] = None
    cashAvailableForTrading: Optional[Decimal] = None
    cashReceipts: Optional[Decimal] = None
    dayTradingBuyingPower: Optional[Decimal] = None
    dayTradingBuyingPowerCall: Optional[Decimal] = None
    dayTradingEquityCall: Optional[Decimal] = None
    equity: Optional[Decimal] = None
    equityPercentage: Optional[Decimal] = None
    liquidationValue: Optional[Decimal] = None
    longMarginValue: Optional[Decimal] = None
    longOptionMarketValue: Optional[Decimal] = None
    longStockValue: Optional[Decimal] = None
    maintenanceCall: Optional[Decimal] = None
    maintenanceRequirement: Optional[Decimal] = None
    margin: Optional[Decimal] = None
    marginEquity: Optional[Decimal] = None
    moneyMarketFund: Optional[Decimal] = None
    mutualFundValue: Optional[Decimal] = None
    regTCall: Optional[Decimal] = None
    shortMarginValue: Optional[Decimal] = None
    shortOptionMarketValue: Optional[Decimal] = None
    shortStockValue: Optional[Decimal] = None
    totalCash: Optional[Decimal] = None
    isInCall: Optional[bool] = False
    unsettledCash: Optional[Decimal] = None
    pendingDeposits: Optional[Decimal] = None
    marginBalance: Optional[Decimal] = None
    shortBalance: Optional[Decimal] = None
    accountValue: Optional[Decimal] = None


class CurrentBalances(BaseModel):
    accruedInterest: Optional[Decimal] = None
    cashBalance: Optional[Decimal] = None
    cashReceipts: Optional[Decimal] = None
    longOptionMarketValue: Optional[Decimal] = None
    liquidationValue: Optional[Decimal] = None
    longMarketValue: Optional[Decimal] = None
    moneyMarketFund: Optional[Decimal] = None
    savings: Optional[Decimal] = None
    shortMarketValue: Optional[Decimal] = None
    pendingDeposits: Optional[Decimal] = None
    availableFunds: Optional[Decimal] = None
    availableFundsNonMarginableTrade: Optional[Decimal] = None
    buyingPower: Optional[Decimal] = None
    buyingPowerNonMarginableTrade: Optional[Decimal] = None
    dayTradingBuyingPower: Optional[Decimal] = None
    dayTradingBuyingPowerCall: Optional[Decimal] = None
    equity: Optional[Decimal] = None
    equityPercentage: Optional[Decimal] = None
    longMarginValue: Optional[Decimal] = None
    maintenanceCall: Optional[Decimal] = None
    maintenanceRequirement: Optional[Decimal] = None
    marginBalance: Optional[Decimal] = None
    regTCall: Optional[Decimal] = None
    shortBalance: Optional[Decimal] = None
    shortMarginValue: Optional[Decimal] = None
    shortOptionMarketValue: Optional[Decimal] = None
    sma: Optional[Decimal] = None
    mutualFundValue: Optional[Decimal] = None
    bondValue: Optional[Decimal] = None
    isInCall: Optional[bool] = False
    stockBuyingPower: Optional[Decimal] = None
    optionBuyingPower: Optional[Decimal] = None


class ProjectedBalances(CurrentBalances):
    pass


class InitialBalances1(BaseModel):
    accruedInterest: Optional[Decimal] = None
    cashAvailableForTrading: Optional[Decimal] = None
    cashAvailableForWithdrawal: Optional[Decimal] = None
    cashBalance: Optional[Decimal] = None
    bondValue: Optional[Decimal] = None
    cashReceipts: Optional[Decimal] = None
    liquidationValue: Optional[Decimal] = None
    longOptionMarketValue: Optional[Decimal] = None
    longStockValue: Optional[Decimal] = None
    moneyMarketFund: Optional[Decimal] = None
    mutualFundValue: Optional[Decimal] = None
    shortOptionMarketValue: Optional[Decimal] = None
    shortStockValue: Optional[Decimal] = None
    isInCall: Optional[bool] = False
    unsettledCash: Optional[Decimal] = None
    cashDebitCallValue: Optional[Decimal] = None
    pendingDeposits: Optional[Decimal] = None
    accountValue: Optional[Decimal] = None


class CurrentBalances1(BaseModel):
    accruedInterest: Optional[Decimal] = None
    cashBalance: Optional[Decimal] = None
    cashReceipts: Optional[Decimal] = None
    longOptionMarketValue: Optional[Decimal] = None
    liquidationValue: Optional[Decimal] = None
    longMarketValue: Optional[Decimal] = None
    moneyMarketFund: Optional[Decimal] = None
    savings: Optional[Decimal] = None
    shortMarketValue: Optional[Decimal] = None
    pendingDeposits: Optional[Decimal] = None
    cashAvailableForTrading: Optional[Decimal] = None
    cashAvailableForWithdrawal: Optional[Decimal] = None
    cashCall: Optional[Decimal] = None
    longNonMarginableMarketValue: Optional[Decimal] = None
    totalCash: Optional[Decimal] = None
    shortOptionMarketValue: Optional[Decimal] = None
    mutualFundValue: Optional[Decimal] = None
    bondValue: Optional[Decimal] = None
    cashDebitCallValue: Optional[Decimal] = None
    unsettledCash: Optional[Decimal] = None


class ProjectedBalances1(CurrentBalances1):
    pass


class ExecutionLeg1(BaseModel):
    legId: Optional[int] = None
    quantity: Optional[Decimal] = None
    mismarkedQuantity: Optional[Decimal] = None
    price: Optional[Decimal] = None
    time: Optional[datetime] = None


class Execution1(BaseModel):
    activityType: Optional[ActivityType3] = None
    executionType: Optional[Literal['FILL']] = None
    quantity: Optional[Decimal] = None
    orderRemainingQuantity: Optional[Decimal] = None
    executionLegs: Optional[List[ExecutionLeg1]] = None


class Position(BaseModel):
    shortQuantity: Optional[Decimal] = None
    averagePrice: Optional[Decimal] = None
    currentDayProfitLoss: Optional[Decimal] = None
    currentDayProfitLossPercentage: Optional[Decimal] = None
    longQuantity: Optional[Decimal] = None
    settledLongQuantity: Optional[Decimal] = None
    settledShortQuantity: Optional[Decimal] = None
    agedQuantity: Optional[Decimal] = None
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
    marketValue: Optional[Decimal] = None


class OrderLegCollectionItem2(BaseModel):
    orderLegType: Optional[OrderLegType2] = None
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
    instruction: Optional[Instruction2] = None
    positionEffect: Optional[PositionEffect2] = None
    quantity: Optional[Decimal] = None
    quantityType: Optional[QuantityType2] = None


class OrderStrategy(BaseModel):
    session: Optional[Session2] = None
    duration: Optional[Duration2] = None
    orderType: Optional[OrderType2] = None
    cancelTime: Optional[CancelTime2] = None
    complexOrderStrategyType: Optional[ComplexOrderStrategyType2] = None
    quantity: Optional[Decimal] = None
    filledQuantity: Optional[Decimal] = None
    remainingQuantity: Optional[Decimal] = None
    requestedDestination: Optional[RequestedDestination2] = None
    destinationLinkName: Optional[str] = None
    releaseTime: Optional[datetime] = None
    stopPrice: Optional[Decimal] = None
    stopPriceLinkBasis: Optional[StopPriceLinkBasis2] = None
    stopPriceLinkType: Optional[StopPriceLinkType2] = None
    stopPriceOffset: Optional[Decimal] = None
    stopType: Optional[StopType2] = None
    priceLinkBasis: Optional[StopPriceLinkBasis2] = None
    priceLinkType: Optional[StopPriceLinkType2] = None
    price: Optional[Decimal] = None
    taxLotMethod: Optional[TaxLotMethod2] = None
    orderLegCollection: Optional[List[OrderLegCollectionItem2]] = None
    activationPrice: Optional[Decimal] = None
    specialInstruction: Optional[SpecialInstruction2] = None
    orderStrategyType: Optional[OrderStrategyType2] = None
    orderId: Optional[int] = None
    cancelable: Optional[bool] = False
    editable: Optional[bool] = False
    status: Optional[Status2] = None
    enteredTime: Optional[datetime] = None
    closeTime: Optional[datetime] = None
    tag: Optional[str] = None
    accountId: Optional[int] = None
    orderActivityCollection: Optional[List[OrderActivityCollectionItem2]] = None
    replacingOrderCollection: Optional[List[str]] = None
    childOrderStrategies: Optional[List[str]] = None
    statusDescription: Optional[str] = None


class SecuritiesAccount(BaseModel):
    accountId: Optional[str] = None
    roundTrips: Optional[int] = None
    isDayTrader: Optional[bool] = False
    isClosingOnlyRestricted: Optional[bool] = False
    positions: Optional[List[Position]] = None
    orderStrategies: Optional[List[OrderStrategy]] = None


class MarginAccount(SecuritiesAccount):
    type: Literal['MARGIN']
    initialBalances: Optional[InitialBalances] = None
    currentBalances: Optional[CurrentBalances] = None
    projectedBalances: Optional[ProjectedBalances] = None


class CashAccount(SecuritiesAccount):
    type: Literal['CASH']
    initialBalances: Optional[InitialBalances1] = None
    currentBalances: Optional[CurrentBalances1] = None
    projectedBalances: Optional[ProjectedBalances1] = None


class GetAccountOutput(BaseModel):
    securitiesAccount: Optional[Union[MarginAccount, CashAccount]] = Field(
        None, discriminator='type'
    )


class GetAccountResponse(BaseModel):
    output: GetAccountOutput
