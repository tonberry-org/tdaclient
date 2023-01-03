# generated by datamodel-codegen:
#   filename:  get_quote_request.json
#   timestamp: 2023-01-03T23:05:32+00:00

from __future__ import annotations

from pydantic import BaseModel

from . import authorization


class GetQuoteInput(BaseModel):
    apiKey: str
    symbol: str


class GetQuoteRequest(BaseModel):
    authorization: authorization.Authorization
    input: GetQuoteInput
