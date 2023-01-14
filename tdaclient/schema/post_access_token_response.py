# generated by datamodel-codegen:
#   filename:  post_access_token_response.json
#   timestamp: 2023-01-14T17:09:46+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class PostAccessTokenOutput(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: int
    scope: Optional[str] = None
    refresh_token_expires_in: Optional[int] = None


class PostAccessTokenResponse(BaseModel):
    output: PostAccessTokenOutput
