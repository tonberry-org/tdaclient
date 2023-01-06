import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
from typing import Optional, TypedDict, Any, Mapping
import http.client as http_client

from tdaclient.schema import (
    PostAccessTokenRequest,
    PostAccessTokenResponse,
    UserPrincipalResponse,
    GetAccountResponse,
    GetQuoteRequest,
    GetQuoteResponse,
    OptionChainRequest,
    OptionChainResponse,
    GetQuotesRequest,
    GetQuotesResponse,
    MarketHoursResponse,
    MarketHoursRequest,
)
from tdaclient.schema.get_account_request import GetAccountRequest
from tdaclient.schema.user_principal_request import UserPrincipalRequest

http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.

logger = logging.getLogger(__name__)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class TDClientConfig(TypedDict):
    # client_id: str
    code: str


class TDAClient:
    def __init__(self, session: Optional[Session] = None) -> None:
        self.session = requests.Session() if session is None else session
        retry_strategy = Retry(
            total=5, status_forcelist=[429, 500, 502, 503, 504], backoff_factor=2
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def __get_url(self) -> str:
        return "https://api.tdameritrade.com/v1"

    def __get(
        self,
        path: str,
        query_params: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        response = self.session.get(
            f"{self.__get_url()}/{path}",
            params=query_params,
            headers=self.__headers(headers),
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return dict(response.json())

    def __post(
        self,
        path: str,
        data: Mapping[str, object],
        query_params: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        response = self.session.post(
            f"{self.__get_url()}/{path}",
            headers=self.__headers(headers),
            data=data,
            params=query_params,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return dict(response.json())

    def __auth_header(self, access_token: Optional[str]) -> dict[str, str]:
        return (
            {} if access_token is None else {"Authorization": f"Bearer {access_token}"}
        )

    def __headers(self, headers: Optional[dict[str, str]] = None) -> dict[str, str]:
        result = {"Content-Type": "application/x-www-form-urlencoded"}
        if headers is not None:
            result.update(headers)
        return result

    def userprincipals(self, request: UserPrincipalRequest) -> UserPrincipalResponse:
        return UserPrincipalResponse(
            output=self.__get(
                "userprincipals",
                headers=self.__auth_header(request.authorization.access_token),
            )
        )

    def oauth(self, request: PostAccessTokenRequest) -> PostAccessTokenResponse:
        response = self.__post("oauth2/token", data=request.input.dict())
        return PostAccessTokenResponse(output=response)

    def get_account(self, request: GetAccountRequest) -> GetAccountResponse:
        return GetAccountResponse(
            output=self.__get(
                f"accounts/{request.input.accountId}",
                headers=self.__auth_header(request.authorization.access_token),
            )
        )

    def get_quote(self, get_quote_request: GetQuoteRequest) -> GetQuoteResponse:
        response = self.__get(
            f"marketdata/{get_quote_request.input.symbol}/quotes",
            headers=self.__auth_header(get_quote_request.authorization.access_token),
        )
        return GetQuoteResponse(output=response)

    def get_quotes(self, get_quotes_request: GetQuotesRequest) -> GetQuotesResponse:
        response = self.__get(
            "marketdata/quotes",
            query_params={
                "apikey": get_quotes_request.input.apiKey,
                "symbol": ",".join(get_quotes_request.input.symbols),
            },
            headers=self.__auth_header(get_quotes_request.authorization.access_token),
        )
        return GetQuotesResponse(output=response)

    def __drop_nan(
        self, get_option_chain_response: dict[str, dict[str, dict[str, Any]]]
    ) -> Any:
        for putcall in ["putExpDateMap", "callExpDateMap"]:
            for exp in get_option_chain_response[putcall]:
                for strike in get_option_chain_response[putcall][exp]:
                    for option in get_option_chain_response[putcall][exp][strike]:
                        for key in option:
                            if option[key] == "NaN":
                                option[key] = None
        return get_option_chain_response

    def get_option_chain(
        self, get_option_chain_request: OptionChainRequest
    ) -> OptionChainResponse:
        response = self.__get(
            "marketdata/chains",
            query_params=get_option_chain_request.input.dict(),
            headers=self.__auth_header(
                get_option_chain_request.authorization.access_token
            ),
        )
        response = self.__drop_nan(response)
        return OptionChainResponse(output=response)

    def market_hours(
        self, market_hours_request: MarketHoursRequest
    ) -> MarketHoursResponse:
        query_params = {
            "markets": ",".join(market_hours_request.input.markets),
            "Date": market_hours_request.input.date.isoformat(),
        }
        response = self.__get(
            "marketdata/hours",
            headers=self.__auth_header(market_hours_request.authorization.access_token),
            query_params=query_params,
        )
        return MarketHoursResponse(output=response)
