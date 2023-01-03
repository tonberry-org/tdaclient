# generated by datamodel-codegen:
#   filename:  post_access_token_request.json
#   timestamp: 2023-01-03T22:14:59+00:00

from __future__ import annotations

from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel


class GrantType(str, Enum):
    authorization_code = 'authorization_code'
    refresh_token = 'refresh_token'


class PostActionTokenInput(BaseModel):
    client_id: str
    grant_type: GrantType
    refresh_token: Optional[str] = None
    access_type: Optional[Literal['offline']] = None
    code: Optional[str] = None
    redirect_uri: Optional[str] = None


class PostAccessTokenRequest(BaseModel):
    input: PostActionTokenInput
