import json
from tdaclient.schema.get_price_history_response import (
    GetPriceHistoryResponse,
)

RESPONSE = """
{
    "candles": [
        {
            "open": 3843.34,
            "high": 3846.65,
            "low": 3813.22,
            "close": 3829.25,
            "volume": 0,
            "datetime": 1672120800000
        },
        {
            "open": 3829.56,
            "high": 3848.32,
            "low": 3780.78,
            "close": 3783.22,
            "volume": 0,
            "datetime": 1672207200000
        },
        {
            "open": 3805.45,
            "high": 3857.28,
            "low": 3805.45,
            "close": 3855.26,
            "volume": -10112,
            "datetime": 1672290000000
        }
    ],
    "symbol": "$SPX.X",
    "empty": false
}
"""


def test_get_price_history_response() -> None:
    response = GetPriceHistoryResponse(response=json.loads(RESPONSE))
    print(response)
