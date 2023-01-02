from tdaclient.schema.authorization import Authorization
from tdaclient.schema.option_chain_request import (
    OptionChainRequest,
    OptionChainInput,
    ContractType,
)


def test_option_chain_request() -> None:
    request = OptionChainRequest(
        authorization=Authorization(access_token="1234"),
        input=OptionChainInput(
            symbol="SPY",
            contractType=ContractType.ALL,
            strikeCount=2,
            includeQuotes=True,
            fromDate="2022-10-17",
            toDate="2022-10-21",
        ),
    )
    print(request)
