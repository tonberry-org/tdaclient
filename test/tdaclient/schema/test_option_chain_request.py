from tdaclient.schema.option_chain_request import (
    OptionChainRequest,
    Strategy,
    ContractType,
)


def test_option_chain_request() -> None:
    request = OptionChainRequest(
        symbol="SPY",
        contractType=ContractType.ALL,
        strikeCount=2,
        includeQuotes=True,
        fromDate="2022-10-17",
        toDate="2022-10-21",
    )
    print(request)
