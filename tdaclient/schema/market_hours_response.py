# generated by datamodel-codegen:
#   filename:  market_hours_response.json
#   timestamp: 2023-01-01T22:45:44+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel


class MarketType(Enum):
    BOND = 'BOND'
    EQUITY = 'EQUITY'
    ETF = 'ETF'
    FOREX = 'FOREX'
    FUTURE = 'FUTURE'
    FUTURE_OPTION = 'FUTURE_OPTION'
    INDEX = 'INDEX'
    INDICATOR = 'INDICATOR'
    MUTUAL_FUND = 'MUTUAL_FUND'
    OPTION = 'OPTION'
    UNKNOWN = 'UNKNOWN'


class Response(BaseModel):
    category: Optional[str] = None
    date: Optional[str] = None
    exchange: Optional[str] = None
    isOpen: Optional[bool] = None
    marketType: Optional[MarketType] = None
    product: Optional[str] = None
    productName: Optional[str] = None
    sessionHours: Optional[Dict[str, List[str]]] = None


class MarketHoursResponse(BaseModel):
    response: Optional[Response] = None
