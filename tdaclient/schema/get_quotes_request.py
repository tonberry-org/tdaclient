# generated by datamodel-codegen:
#   filename:  get_quotes_request.json
#   timestamp: 2023-01-04T17:36:49+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from . import authorization


class GetQuotesInput(BaseModel):
    apiKey: str
    symbols: List[str] = Field(..., min_items=1)


class GetQuotesRequest(BaseModel):
    authorization: authorization.Authorization
    input: GetQuotesInput
