from tdaclient.schema.market_hours_response import MarketHoursResponse
import json

RESPONSE = """
{
    "option": {
        "EQO": {
            "date": "2022-12-29",
            "marketType": "OPTION",
            "exchange": "NULL",
            "category": "NULL",
            "product": "EQO",
            "productName": "equity option",
            "isOpen": true,
            "sessionHours": {
                "regularMarket": [
                    {
                        "start": "2022-12-29T09:30:00-05:00",
                        "end": "2022-12-29T16:00:00-05:00"
                    }
                ]
            }
        },
        "IND": {
            "date": "2022-12-29",
            "marketType": "OPTION",
            "exchange": "NULL",
            "category": "NULL",
            "product": "IND",
            "productName": "index option",
            "isOpen": true,
            "sessionHours": {
                "regularMarket": [
                    {
                        "start": "2022-12-29T09:30:00-05:00",
                        "end": "2022-12-29T16:15:00-05:00"
                    }
                ]
            }
        }
    }
}
"""


def test_get_market_hours() -> None:
    response = MarketHoursResponse(response=json.loads(RESPONSE))
    print(response)
