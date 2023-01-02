import json
from tdaclient.schema.user_principal_response import (
    UserPrincipalResponse,
)

RESPONSE = """
{
    "userId": "tondreau",
    "userCdDomainId": "A000000096997406",
    "primaryAccountId": "255845516",
    "lastLoginTime": "2022-12-29T18:00:07+0000",
    "tokenExpirationTime": "2022-12-29T18:31:05+0000",
    "loginTime": "2022-12-29T18:01:05+0000",
    "accessLevel": "CUS",
    "stalePassword": false,
    "professionalStatus": "NON_PROFESSIONAL",
    "quotes": {
        "isNyseDelayed": false,
        "isNasdaqDelayed": false,
        "isOpraDelayed": false,
        "isAmexDelayed": false,
        "isCmeDelayed": true,
        "isIceDelayed": true,
        "isForexDelayed": true
    },
    "exchangeAgreements": {
        "NYSE_EXCHANGE_AGREEMENT": "ACCEPTED",
        "NASDAQ_EXCHANGE_AGREEMENT": "ACCEPTED",
        "OPRA_EXCHANGE_AGREEMENT": "ACCEPTED"
    },
    "accounts": [
        {
            "accountId": "255845516",
            "displayName": "tondreau",
            "accountCdDomainId": "A000000096997405",
            "company": "AMER",
            "segment": "ADVNCED",
            "acl": "BPDRDTDWESF7G1G3G5G7GKGLH1H3H5LTM1MAOSPNQ2QSRFSDT6TETFTOTTUAURXBXNXO",
            "authorizations": {
                "apex": false,
                "levelTwoQuotes": true,
                "stockTrading": true,
                "marginTrading": true,
                "streamingNews": false,
                "optionTradingLevel": "SPREAD",
                "streamerAccess": true,
                "advancedMargin": true,
                "scottradeAccount": false
            }
        },
        {
            "accountId": "255140896",
            "displayName": "tondreautest",
            "accountCdDomainId": "A000000097589944",
            "company": "AMER",
            "segment": "ADVNCED",
            "acl": "BPDRDTDWESF7G1G3G5G7GKGLH1H3H5LTM1OLQSRFSDT5TETFTOTTUAUR",
            "authorizations": {
                "apex": false,
                "levelTwoQuotes": false,
                "stockTrading": true,
                "marginTrading": false,
                "streamingNews": false,
                "optionTradingLevel": "LONG",
                "streamerAccess": true,
                "advancedMargin": false,
                "scottradeAccount": false
            }
        }
    ]
}
"""


def test_user_principal_response() -> None:
    response = UserPrincipalResponse(output=json.loads(RESPONSE))
    print(response)
