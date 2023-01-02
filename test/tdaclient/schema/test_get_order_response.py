import json
from tdaclient.schema.get_order_response import GetOrderResponse


RESPONSE = """
{
    "session": "NORMAL",
    "duration": "DAY",
    "orderType": "NET_CREDIT",
    "complexOrderStrategyType": "IRON_CONDOR",
    "quantity": 3.0,
    "filledQuantity": 0.0,
    "remainingQuantity": 0.0,
    "requestedDestination": "AUTO",
    "destinationLinkName": "AutoRoute",
    "price": 1.35,
    "orderLegCollection": [
        {
            "orderLegType": "OPTION",
            "legId": 1,
            "instrument": {
                "assetType": "OPTION",
                "cusip": "0SPXW.LT23850000",
                "symbol": "SPXW_122922C3850",
                "description": "$SPX.X Dec 29 2022 3850.0 Call",
                "putCall": "CALL",
                "underlyingSymbol": "$SPX.X"
            },
            "instruction": "SELL_TO_OPEN",
            "positionEffect": "OPENING",
            "quantity": 3.0
        },
        {
            "orderLegType": "OPTION",
            "legId": 2,
            "instrument": {
                "assetType": "OPTION",
                "cusip": "0SPXW.LT23870000",
                "symbol": "SPXW_122922C3870",
                "description": "$SPX.X Dec 29 2022 3870.0 Call",
                "putCall": "CALL",
                "underlyingSymbol": "$SPX.X"
            },
            "instruction": "BUY_TO_OPEN",
            "positionEffect": "OPENING",
            "quantity": 3.0
        },
        {
            "orderLegType": "OPTION",
            "legId": 3,
            "instrument": {
                "assetType": "OPTION",
                "cusip": "0SPXW.XT23705000",
                "symbol": "SPXW_122922P3705",
                "description": "$SPX.X Dec 29 2022 3705.0 Put",
                "putCall": "PUT",
                "underlyingSymbol": "$SPX.X"
            },
            "instruction": "SELL_TO_OPEN",
            "positionEffect": "OPENING",
            "quantity": 3.0
        },
        {
            "orderLegType": "OPTION",
            "legId": 4,
            "instrument": {
                "assetType": "OPTION",
                "cusip": "0SPXW.XT23685000",
                "symbol": "SPXW_122922P3685",
                "description": "$SPX.X Dec 29 2022 3685.0 Put",
                "putCall": "PUT",
                "underlyingSymbol": "$SPX.X"
            },
            "instruction": "BUY_TO_OPEN",
            "positionEffect": "OPENING",
            "quantity": 3.0
        }
    ],
    "orderStrategyType": "SINGLE",
    "orderId": 5971946436,
    "cancelable": false,
    "editable": false,
    "status": "REJECTED",
    "enteredTime": "2022-12-28T20:49:17+0000",
    "closeTime": "2022-12-28T20:49:17+0000",
    "tag": "tIP",
    "accountId": 255845516
}
"""


def test_get_order_response() -> None:
    response = GetOrderResponse(output=json.loads(RESPONSE))
    print(response)
