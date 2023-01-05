# generated by datamodel-codegen:
#   filename:  get_price_history_response.json
#   timestamp: 2023-01-05T21:57:57+00:00

from __future__ import annotations

from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field


class Candle(BaseModel):
    close: Optional[Decimal] = Field(None, description='Close')
    datetime: Optional[int] = Field(None, description='DateTime')
    high: Optional[Decimal] = Field(None, description='High')
    low: Optional[Decimal] = Field(None, description='Low')
    open: Optional[Decimal] = Field(None, description='Open')
    volume: Optional[int] = Field(None, description='Volume')


class GetPriceHistoryOutput(BaseModel):
    candles: Optional[List[Candle]] = Field(None, description='List of candles')
    empty: Optional[bool] = None
    symbol: Optional[str] = Field(None, description='Symbol')


class GetPriceHistoryResponse(BaseModel):
    output: GetPriceHistoryOutput
