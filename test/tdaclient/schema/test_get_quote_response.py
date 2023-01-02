from tdaclient.schema.get_quote_response import GetQuoteResponse
import json

RESPONSE = """
{
    "$SPX.X": {
        "assetType": "INDEX",
        "assetMainType": "INDEX",
        "cusip": "",
        "assetSubType": "",
        "symbol": "$SPX.X",
        "description": "S&P 500 INDEX",
        "lastPrice": 3828.48,
        "openPrice": 3843.3401,
        "highPrice": 3846.6499,
        "lowPrice": 3813.22,
        "closePrice": 3844.8201,
        "netChange": -16.34,
        "totalVolume": 1064613393,
        "tradeTimeInLong": 1672170842054,
        "exchange": "x",
        "exchangeName": "INDICES",
        "digits": 2,
        "52WkHigh": 4818.6201,
        "52WkLow": 3491.5801,
        "securityStatus": "Normal",
        "netPercentChangeInDouble": -0.425,
        "delayed": false,
        "realtimeEntitled": true
    }
}
"""


def test_get_quote_response() -> None:
    response = GetQuoteResponse(output=json.loads(RESPONSE))

    print(response)
