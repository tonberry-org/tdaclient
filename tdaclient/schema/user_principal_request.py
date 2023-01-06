# generated by datamodel-codegen:
#   filename:  user_principal_request.json
#   timestamp: 2023-01-06T20:23:23+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from . import authorization


class Field1(str, Enum):
    streamerSubscriptionKeys = 'streamerSubscriptionKeys'
    streamerConnectionInfo = 'streamerConnectionInfo'
    preferences = 'preferences'
    surrogateIds = 'surrogateIds'


class UserPrincipalInput(BaseModel):
    fields: Optional[List[Field1]] = None


class UserPrincipalRequest(BaseModel):
    authorization: authorization.Authorization
    input: Optional[UserPrincipalInput] = None
