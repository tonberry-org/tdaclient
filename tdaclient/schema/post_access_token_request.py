# generated by datamodel-codegen:
#   filename:  post_access_token_request.json
#   timestamp: 2023-01-01T22:45:45+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel
from typing_extensions import Literal


class GrantType(Enum):
    authorization_code = 'authorization_code'
    refresh_token = 'refresh_token'


class Request(BaseModel):
    grant_type: GrantType
    refresh_token: Optional[str] = None
    access_type: Optional[Literal['offline']] = None
    code: Optional[str] = None
    redirect_uri: Optional[str] = None


class PostAccessTokenRequest(BaseModel):
    request: Optional[Request] = None
