# generated by datamodel-codegen:
#   filename:  authorization.json
#   timestamp: 2023-01-02T01:31:31+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra


class Model(BaseModel):
    pass

    class Config:
        extra = Extra.forbid


class Authorization(BaseModel):
    access_token: str