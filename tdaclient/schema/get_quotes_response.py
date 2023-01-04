# generated by datamodel-codegen:
#   filename:  get_quotes_response.json
#   timestamp: 2023-01-04T01:47:45+00:00

from __future__ import annotations

from typing import Dict, Union

from pydantic import BaseModel

from . import common_quotes


class GetQuotesResponse(BaseModel):
    output: Dict[
        str,
        Union[
            common_quotes.MutualFundQuote,
            common_quotes.FutureQuote,
            common_quotes.FutureOptionQuote,
            common_quotes.IndexQuote,
            common_quotes.OptionQuote,
            common_quotes.ForexQuote,
            common_quotes.ETFQuote,
            common_quotes.EquitiesQuote,
        ],
    ]
