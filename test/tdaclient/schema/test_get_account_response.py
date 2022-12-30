import json
from tdaclient.schema.get_account_response import GetAccountResponse

RESPONSE = """
{
    "securitiesAccount": {
        "type": "MARGIN",
        "accountId": "255845516",
        "roundTrips": 2,
        "isDayTrader": false,
        "isClosingOnlyRestricted": false,
        "positions": [
            {
                "shortQuantity": 0.0,
                "averagePrice": 0.27,
                "currentDayCost": 81.0,
                "currentDayProfitLoss": -73.5,
                "currentDayProfitLossPercentage": -90.74,
                "longQuantity": 3.0,
                "settledLongQuantity": 0.0,
                "settledShortQuantity": 0.0,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.XR23765000",
                    "symbol": "SPXW_122722P3765",
                    "description": "$SPX.X Dec 27 2022 3765.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "marketValue": 7.5,
                "maintenanceRequirement": 0.0,
                "previousSessionLongQuantity": 0.0
            },
            {
                "shortQuantity": 3.0,
                "averagePrice": 0.87,
                "currentDayCost": -261.0,
                "currentDayProfitLoss": 253.5,
                "currentDayProfitLossPercentage": 97.13,
                "longQuantity": 0.0,
                "settledLongQuantity": 0.0,
                "settledShortQuantity": 0.0,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.XR23785000",
                    "symbol": "SPXW_122722P3785",
                    "description": "$SPX.X Dec 27 2022 3785.0 Put",
                    "putCall": "PUT",
                    "underlyingSymbol": "$SPX.X"
                },
                "marketValue": -7.5,
                "maintenanceRequirement": 0.0,
                "previousSessionShortQuantity": 0.0
            },
            {
                "shortQuantity": 3.0,
                "averagePrice": 0.8,
                "currentDayCost": -240.0,
                "currentDayProfitLoss": 232.5,
                "currentDayProfitLossPercentage": 96.88,
                "longQuantity": 0.0,
                "settledLongQuantity": 0.0,
                "settledShortQuantity": 0.0,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.LR23890000",
                    "symbol": "SPXW_122722C3890",
                    "description": "$SPX.X Dec 27 2022 3890.0 Call",
                    "putCall": "CALL",
                    "underlyingSymbol": "$SPX.X"
                },
                "marketValue": -7.5,
                "maintenanceRequirement": 0.0,
                "previousSessionShortQuantity": 0.0
            },
            {
                "shortQuantity": 0.0,
                "averagePrice": 0.25,
                "currentDayCost": 75.0,
                "currentDayProfitLoss": -67.5,
                "currentDayProfitLossPercentage": -90.0,
                "longQuantity": 3.0,
                "settledLongQuantity": 0.0,
                "settledShortQuantity": 0.0,
                "instrument": {
                    "assetType": "OPTION",
                    "cusip": "0SPXW.LR23910000",
                    "symbol": "SPXW_122722C3910",
                    "description": "$SPX.X Dec 27 2022 3910.0 Call",
                    "putCall": "CALL",
                    "underlyingSymbol": "$SPX.X"
                },
                "marketValue": 7.5,
                "maintenanceRequirement": 6000.0,
                "previousSessionLongQuantity": 0.0
            }
        ],
        "orderStrategies": [
            {
                "session": "NORMAL",
                "duration": "DAY",
                "orderType": "NET_CREDIT",
                "complexOrderStrategyType": "IRON_CONDOR",
                "quantity": 3.0,
                "filledQuantity": 3.0,
                "remainingQuantity": 0.0,
                "requestedDestination": "CBOE",
                "destinationLinkName": "AutoRoute",
                "price": 1.15,
                "orderLegCollection": [
                    {
                        "orderLegType": "OPTION",
                        "legId": 1,
                        "instrument": {
                            "assetType": "OPTION",
                            "cusip": "0SPXW.LR23890000",
                            "symbol": "SPXW_122722C3890",
                            "description": "$SPX.X Dec 27 2022 3890.0 Call",
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
                            "cusip": "0SPXW.LR23910000",
                            "symbol": "SPXW_122722C3910",
                            "description": "$SPX.X Dec 27 2022 3910.0 Call",
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
                            "cusip": "0SPXW.XR23785000",
                            "symbol": "SPXW_122722P3785",
                            "description": "$SPX.X Dec 27 2022 3785.0 Put",
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
                            "cusip": "0SPXW.XR23765000",
                            "symbol": "SPXW_122722P3765",
                            "description": "$SPX.X Dec 27 2022 3765.0 Put",
                            "putCall": "PUT",
                            "underlyingSymbol": "$SPX.X"
                        },
                        "instruction": "BUY_TO_OPEN",
                        "positionEffect": "OPENING",
                        "quantity": 3.0
                    }
                ],
                "orderStrategyType": "SINGLE",
                "orderId": 5968731585,
                "cancelable": false,
                "editable": false,
                "status": "FILLED",
                "enteredTime": "2022-12-27T15:22:22+0000",
                "closeTime": "2022-12-27T15:22:23+0000",
                "tag": "tIP",
                "accountId": 255845516,
                "orderActivityCollection": [
                    {
                        "activityType": "EXECUTION",
                        "activityId": 9475122415,
                        "executionType": "FILL",
                        "quantity": 1.0,
                        "orderRemainingQuantity": 2.0,
                        "executionLegs": [
                            {
                                "legId": 1,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.8,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 2,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.25,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 3,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.87,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 4,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.27,
                                "time": "2022-12-27T15:22:23+0000"
                            }
                        ]
                    },
                    {
                        "activityType": "EXECUTION",
                        "activityId": 9475122422,
                        "executionType": "FILL",
                        "quantity": 1.0,
                        "orderRemainingQuantity": 1.0,
                        "executionLegs": [
                            {
                                "legId": 1,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.8,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 2,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.25,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 3,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.87,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 4,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.27,
                                "time": "2022-12-27T15:22:23+0000"
                            }
                        ]
                    },
                    {
                        "activityType": "EXECUTION",
                        "activityId": 9475122430,
                        "executionType": "FILL",
                        "quantity": 1.0,
                        "orderRemainingQuantity": 0.0,
                        "executionLegs": [
                            {
                                "legId": 1,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.8,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 2,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.25,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 3,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.87,
                                "time": "2022-12-27T15:22:23+0000"
                            },
                            {
                                "legId": 4,
                                "quantity": 1.0,
                                "mismarkedQuantity": 0.0,
                                "price": 0.27,
                                "time": "2022-12-27T15:22:23+0000"
                            }
                        ]
                    }
                ]
            }
        ],
        "initialBalances": {
            "accruedInterest": 0.0,
            "availableFundsNonMarginableTrade": 7976.49,
            "bondValue": 0.0,
            "buyingPower": 15952.98,
            "cashBalance": 7976.49,
            "cashAvailableForTrading": 0.0,
            "cashReceipts": 0.0,
            "dayTradingBuyingPower": 15952.98,
            "dayTradingBuyingPowerCall": 0.0,
            "dayTradingEquityCall": 0.0,
            "equity": 7976.49,
            "equityPercentage": 100.0,
            "liquidationValue": 7976.49,
            "longMarginValue": 0.0,
            "longOptionMarketValue": 0.0,
            "longStockValue": 0.0,
            "maintenanceCall": 0.0,
            "maintenanceRequirement": 0.0,
            "margin": 7976.49,
            "marginEquity": 0.0,
            "moneyMarketFund": 0.0,
            "mutualFundValue": 0.0,
            "regTCall": 0.0,
            "shortMarginValue": 0.0,
            "shortOptionMarketValue": 0.0,
            "shortStockValue": 0.0,
            "totalCash": 7976.49,
            "isInCall": false,
            "pendingDeposits": 0.0,
            "marginBalance": 0.0,
            "shortBalance": 0.0,
            "accountValue": 7976.49
        },
        "currentBalances": {
            "accruedInterest": 0.0,
            "cashBalance": 8307.69,
            "cashReceipts": 0.0,
            "longOptionMarketValue": 15.0,
            "liquidationValue": 8307.69,
            "longMarketValue": 0.0,
            "moneyMarketFund": 0.0,
            "savings": 0.0,
            "shortMarketValue": 0.0,
            "pendingDeposits": 0.0,
            "availableFunds": 2307.69,
            "availableFundsNonMarginableTrade": 2307.69,
            "buyingPower": 4615.38,
            "buyingPowerNonMarginableTrade": 2307.69,
            "dayTradingBuyingPower": 0.0,
            "equity": 8307.69,
            "equityPercentage": 100.0,
            "longMarginValue": 0.0,
            "maintenanceCall": 0.0,
            "maintenanceRequirement": 6000.0,
            "marginBalance": 0.0,
            "regTCall": 0.0,
            "shortBalance": 0.0,
            "shortMarginValue": 0.0,
            "shortOptionMarketValue": -15.0,
            "sma": 2307.69,
            "mutualFundValue": 0.0,
            "bondValue": 0.0
        },
        "projectedBalances": {
            "availableFunds": 2307.69,
            "availableFundsNonMarginableTrade": 2307.69,
            "buyingPower": 4615.38,
            "dayTradingBuyingPower": 0.0,
            "dayTradingBuyingPowerCall": 0.0,
            "maintenanceCall": 0.0,
            "regTCall": 0.0,
            "isInCall": false,
            "stockBuyingPower": 4615.38
        }
    }
}
"""


def test_get_account_response() -> None:
    response = GetAccountResponse(response=json.loads(RESPONSE))
    print(response)
