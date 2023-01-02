from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from tdaclient.client import TDAClient
from requests import Session
from tdaclient.schema import PostAccessTokenRequest
from tdaclient.schema.post_access_token_request import GrantType
from tdaclient.schema.post_access_token_request import PostActionTokenInput


@pytest.fixture()
def session_mock(mocker: MockerFixture) -> MagicMock:
    return mocker.patch("requests.Session")


@pytest.fixture()
def tdclient(session_mock: Session) -> TDAClient:
    return TDAClient(session=session_mock)


def test_hello(tdclient: TDAClient, session_mock: MagicMock) -> None:
    response_vals = {
        "access_token": "Hello",
        "refresh_token": "refresh-token-1234",
        "scope": "PlaceTrades AccountAccess MoveMoney",
        "expires_in": 1800,
        "refresh_token_expires_in": 7776000,
        "token_type": "Bearer",
    }
    response_mock = MagicMock()
    response_mock.json.return_value = response_vals
    session_mock.post.return_value = response_mock

    response = tdclient.oauth(
        PostAccessTokenRequest(
            input=PostActionTokenInput(
                grant_type=GrantType.authorization_code,
                access_type="offline",
                code="AAAAA",
                client_id="CLIENT_ID@AMERI.TD",
                redirect_uri="https://127.0.0.1",
            )
        )
    )
    assert response.output.access_token == response_vals["access_token"]
