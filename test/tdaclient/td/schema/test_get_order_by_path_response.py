from tdaclient.td.schema.gen.get_order_by_path_response import (
    GetOrderByPathResponse,
)
import json

RESPONSE = """
[
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
    },
    {
        "session": "NORMAL",
        "duration": "DAY",
        "orderType": "NET_CREDIT",
        "complexOrderStrategyType": "IRON_CONDOR",
        "quantity": 3.0,
        "filledQuantity": 3.0,
        "remainingQuantity": 0.0,
        "requestedDestination": "AUTO",
        "destinationLinkName": "AutoRoute",
        "price": 0.75,
        "orderLegCollection": [
            {
                "orderLegType": "OPTION",
                "legId": 1,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.LS23880000",
                    "symbol": "SPXW_122822C3880",
                    "description": "$SPX.X Dec 28 2022 3880.0 Call",
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
                    "cusip": "0SPXW.LS23900000",
                    "symbol": "SPXW_122822C3900",
                    "description": "$SPX.X Dec 28 2022 3900.0 Call",
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
                    "cusip": "0SPXW.XS23790000",
                    "symbol": "SPXW_122822P3790",
                    "description": "$SPX.X Dec 28 2022 3790.0 Put",
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
                    "cusip": "0SPXW.XS23770000",
                    "symbol": "SPXW_122822P3770",
                    "description": "$SPX.X Dec 28 2022 3770.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "instruction": "BUY_TO_OPEN",
                "positionEffect": "OPENING",
                "quantity": 3.0
            }
        ],
        "orderStrategyType": "SINGLE",
        "orderId": 5970663269,
        "cancelable": false,
        "editable": false,
        "status": "FILLED",
        "enteredTime": "2022-12-28T15:23:51+0000",
        "closeTime": "2022-12-28T15:25:06+0000",
        "tag": "tIP",
        "accountId": 255845516,
        "orderActivityCollection": [
            {
                "activityType": "EXECUTION",
                "activityId": 9478360645,
                "executionType": "FILL",
                "quantity": 3.0,
                "orderRemainingQuantity": 0.0,
                "executionLegs": [
                    {
                        "legId": 1,
                        "quantity": 3.0,
                        "mismarkedQuantity": 0.0,
                        "price": 0.32,
                        "time": "2022-12-28T15:25:06+0000"
                    },
                    {
                        "legId": 2,
                        "quantity": 3.0,
                        "mismarkedQuantity": 0.0,
                        "price": 0.07,
                        "time": "2022-12-28T15:25:06+0000"
                    },
                    {
                        "legId": 3,
                        "quantity": 3.0,
                        "mismarkedQuantity": 0.0,
                        "price": 0.75,
                        "time": "2022-12-28T15:25:06+0000"
                    },
                    {
                        "legId": 4,
                        "quantity": 3.0,
                        "mismarkedQuantity": 0.0,
                        "price": 0.25,
                        "time": "2022-12-28T15:25:06+0000"
                    }
                ]
            }
        ]
    },
    {
        "orderStrategyType": "OCO",
        "orderId": 5970692200,
        "cancelable": false,
        "editable": false,
        "enteredTime": "2022-12-28T15:28:04+0000",
        "accountId": 255845516,
        "childOrderStrategies": [
            {
                "session": "NORMAL",
                "duration": "DAY",
                "orderType": "STOP_LIMIT",
                "complexOrderStrategyType": "IRON_CONDOR",
                "quantity": 3.0,
                "filledQuantity": 0.0,
                "remainingQuantity": 0.0,
                "requestedDestination": "AUTO",
                "destinationLinkName": "AutoRoute",
                "stopPrice": 5.0,
                "stopType": "MARK",
                "price": 5.0,
                "orderLegCollection": [
                    {
                        "orderLegType": "OPTION",
                        "legId": 1,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.LS23880000",
                            "symbol": "SPXW_122822C3880",
                            "description": "$SPX.X Dec 28 2022 3880.0 Call",
                            "putCall": "CALL",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "BUY_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 2,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.LS23900000",
                            "symbol": "SPXW_122822C3900",
                            "description": "$SPX.X Dec 28 2022 3900.0 Call",
                            "putCall": "CALL",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "SELL_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 3,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.XS23790000",
                            "symbol": "SPXW_122822P3790",
                            "description": "$SPX.X Dec 28 2022 3790.0 Put",
                            "putCall": "PUT",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "BUY_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 4,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.XS23770000",
                            "symbol": "SPXW_122822P3770",
                            "description": "$SPX.X Dec 28 2022 3770.0 Put",
                            "putCall": "PUT",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "SELL_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    }
                ],
                "orderStrategyType": "SINGLE",
                "orderId": 5970701101,
                "cancelable": false,
                "editable": false,
                "status": "CANCELED",
                "enteredTime": "2022-12-28T15:28:04+0000",
                "closeTime": "2022-12-28T17:07:34+0000",
                "tag": "tIP",
                "accountId": 255845516
            },
            {
                "session": "NORMAL",
                "duration": "DAY",
                "orderType": "STOP",
                "complexOrderStrategyType": "IRON_CONDOR",
                "quantity": 3.0,
                "filledQuantity": 0.0,
                "remainingQuantity": 0.0,
                "requestedDestination": "AUTO",
                "destinationLinkName": "AutoRoute",
                "stopPrice": 7.0,
                "stopType": "MARK",
                "orderLegCollection": [
                    {
                        "orderLegType": "OPTION",
                        "legId": 1,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.LS23880000",
                            "symbol": "SPXW_122822C3880",
                            "description": "$SPX.X Dec 28 2022 3880.0 Call",
                            "putCall": "CALL",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "BUY_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 2,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.LS23900000",
                            "symbol": "SPXW_122822C3900",
                            "description": "$SPX.X Dec 28 2022 3900.0 Call",
                            "putCall": "CALL",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "SELL_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 3,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.XS23790000",
                            "symbol": "SPXW_122822P3790",
                            "description": "$SPX.X Dec 28 2022 3790.0 Put",
                            "putCall": "PUT",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "BUY_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    },
                    {
                        "orderLegType": "OPTION",
                        "legId": 4,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.XS23770000",
                            "symbol": "SPXW_122822P3770",
                            "description": "$SPX.X Dec 28 2022 3770.0 Put",
                            "putCall": "PUT",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "SELL_TO_CLOSE",
                        "positionEffect": "CLOSING",
                        "quantity": 3.0
                    }
                ],
                "orderStrategyType": "SINGLE",
                "orderId": 5970701102,
                "cancelable": false,
                "editable": false,
                "status": "CANCELED",
                "enteredTime": "2022-12-28T15:28:04+0000",
                "closeTime": "2022-12-28T17:07:39+0000",
                "tag": "tIP",
                "accountId": 255845516
            }
        ]
    },
    {
        "session": "NORMAL",
        "duration": "DAY",
        "orderType": "LIMIT",
        "complexOrderStrategyType": "NONE",
        "quantity": 3.0,
        "filledQuantity": 0.0,
        "remainingQuantity": 0.0,
        "requestedDestination": "AUTO",
        "destinationLinkName": "AutoRoute",
        "price": 1.95,
        "orderLegCollection": [
            {
                "orderLegType": "OPTION",
                "legId": 1,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.XS23770000",
                    "symbol": "SPXW_122822P3770",
                    "description": "$SPX.X Dec 28 2022 3770.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "instruction": "SELL_TO_CLOSE",
                "positionEffect": "CLOSING",
                "quantity": 3.0
            }
        ],
        "orderStrategyType": "SINGLE",
        "orderId": 5971162592,
        "cancelable": false,
        "editable": false,
        "status": "REJECTED",
        "enteredTime": "2022-12-28T17:08:08+0000",
        "closeTime": "2022-12-28T17:08:08+0000",
        "tag": "tIP",
        "accountId": 255845516
    },
    {
        "session": "NORMAL",
        "duration": "DAY",
        "orderType": "NET_DEBIT",
        "complexOrderStrategyType": "VERTICAL",
        "quantity": 3.0,
        "filledQuantity": 3.0,
        "remainingQuantity": 0.0,
        "requestedDestination": "AUTO",
        "destinationLinkName": "AutoRoute",
        "price": 5.55,
        "orderLegCollection": [
            {
                "orderLegType": "OPTION",
                "legId": 1,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.XS23790000",
                    "symbol": "SPXW_122822P3790",
                    "description": "$SPX.X Dec 28 2022 3790.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "instruction": "BUY_TO_CLOSE",
                "positionEffect": "CLOSING",
                "quantity": 3.0
            },
            {
                "orderLegType": "OPTION",
                "legId": 2,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.XS23770000",
                    "symbol": "SPXW_122822P3770",
                    "description": "$SPX.X Dec 28 2022 3770.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "instruction": "SELL_TO_CLOSE",
                "positionEffect": "CLOSING",
                "quantity": 3.0
            }
        ],
        "orderStrategyType": "SINGLE",
        "orderId": 5971162595,
        "cancelable": false,
        "editable": false,
        "status": "FILLED",
        "enteredTime": "2022-12-28T17:08:24+0000",
        "closeTime": "2022-12-28T17:08:25+0000",
        "tag": "tIP",
        "accountId": 255845516,
        "orderActivityCollection": [
            {
                "activityType": "EXECUTION",
                "activityId": 9479266987,
                "executionType": "FILL",
                "quantity": 1.0,
                "orderRemainingQuantity": 0.0,
                "executionLegs": [
                    {
                        "legId": 1,
                        "quantity": 1.0,
                        "mismarkedQuantity": 0.0,
                        "price": 7.1,
                        "time": "2022-12-28T17:08:25+0000"
                    },
                    {
                        "legId": 2,
                        "quantity": 1.0,
                        "mismarkedQuantity": 0.0,
                        "price": 1.85,
                        "time": "2022-12-28T17:08:25+0000"
                    }
                ]
            },
            {
                "activityType": "EXECUTION",
                "activityId": 9479266982,
                "executionType": "FILL",
                "quantity": 2.0,
                "orderRemainingQuantity": 1.0,
                "executionLegs": [
                    {
                        "legId": 1,
                        "quantity": 2.0,
                        "mismarkedQuantity": 0.0,
                        "price": 7.1,
                        "time": "2022-12-28T17:08:25+0000"
                    },
                    {
                        "legId": 2,
                        "quantity": 2.0,
                        "mismarkedQuantity": 0.0,
                        "price": 1.85,
                        "time": "2022-12-28T17:08:25+0000"
                    }
                ]
            }
        ]
    }
]
"""


def test_get_code_by_path_response() -> None:
    response = GetOrderByPathResponse(response=json.loads(RESPONSE))
    print(response)
