from typing import Literal
from enum import Enum
from pydantic import BaseModel


class GrantTypeEnum(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"


class OAuthRequest(BaseModel):
    grant_type: GrantTypeEnum
    refresh_token: str | None = None
    access_type: Literal["offline"] | None = None
    code: str | None = None
    redirect_uri: str | None = None
    client_id: str


class OAuthResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scope: str
    refresh_token_expires_in: int | None = None
    refresh_token: str | None = None
