from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from tdaclient.td.tdclient import TDClient
from requests import Session
from tdaclient.td.oauth_request import GrantTypeEnum, OAuthRequest


@pytest.fixture()
def session_mock(mocker: MockerFixture) -> MagicMock:
    return mocker.patch("requests.Session")


@pytest.fixture()
def tdclient(session_mock: Session) -> TDClient:
    return TDClient(session=session_mock)


def test_hello(tdclient: TDClient, session_mock: MagicMock) -> None:
    response_vals = {
        "access_token": "Hello",
        "refresh_token": "refresh-token-1234",
        "scope": "PlaceTrades AccountAccess MoveMoney",
        "expires_in": 1800,
        "refresh_token_expires_in": 7776000,
        "token_type": "Bearer",
    }
    response = MagicMock()
    response.json.return_value = response_vals
    session_mock.post.return_value = response
    assert (
        tdclient.oauth(
            OAuthRequest(
                grant_type=GrantTypeEnum.AUTHORIZATION_CODE,
                access_type="offline",
                code="AAAAA",
                client_id="CLIENT_ID@AMERI.TD",
                redirect_uri="https://127.0.0.1",
            )
        )
        == response_vals
    )
