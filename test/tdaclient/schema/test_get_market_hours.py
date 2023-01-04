from tdaclient.schema.market_hours_response import MarketHoursResponse
import json

RESPONSE = """
{
    "equity": {
        "EQ": {
            "date": "2023-01-04",
            "marketType": "EQUITY",
            "exchange": "NULL",
            "category": "NULL",
            "product": "EQ",
            "productName": "equity",
            "isOpen": true,
            "sessionHours": {
                "preMarket": [
                    {
                        "start": "2023-01-04T07:00:00-05:00",
                        "end": "2023-01-04T09:30:00-05:00"
                    }
                ],
                "regularMarket": [
                    {
                        "start": "2023-01-04T09:30:00-05:00",
                        "end": "2023-01-04T16:00:00-05:00"
                    }
                ],
                "postMarket": [
                    {
                        "start": "2023-01-04T16:00:00-05:00",
                        "end": "2023-01-04T20:00:00-05:00"
                    }
                ]
            }
        }
    },
    "option": {
        "EQO": {
            "date": "2023-01-04",
            "marketType": "OPTION",
            "exchange": "NULL",
            "category": "NULL",
            "product": "EQO",
            "productName": "equity option",
            "isOpen": true,
            "sessionHours": {
                "regularMarket": [
                    {
                        "start": "2023-01-04T09:30:00-05:00",
                        "end": "2023-01-04T16:00:00-05:00"
                    }
                ]
            }
        },
        "IND": {
            "date": "2023-01-04",
            "marketType": "OPTION",
            "exchange": "NULL",
            "category": "NULL",
            "product": "IND",
            "productName": "index option",
            "isOpen": true,
            "sessionHours": {
                "regularMarket": [
                    {
                        "start": "2023-01-04T09:30:00-05:00",
                        "end": "2023-01-04T16:15:00-05:00"
                    }
                ]
            }
        }
    }
}
"""


def test_market_hours_response() -> None:
    response = MarketHoursResponse(output=json.loads(RESPONSE))
    print(response)
