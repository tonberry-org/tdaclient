from tdaclient.schema.post_access_token_request import (
    PostAccessTokenRequest,
    Request,
    GrantType,
)


def test_post_access_token() -> None:
    request = PostAccessTokenRequest(
        request={
            "grant_type": "authorization_code",
            "access_type": "offline",
            "code": "1234",
            "client_id": "clien_id1234",
            "redirect_uri": "https://127.0.0.1",
        }
    )
    print(request)

    request = PostAccessTokenRequest(
        request=Request(
            grant_type=GrantType.authorization_code,
            access_type="offline",
            code="1234",
            client_id="clien_id1234",
            redirect_uri="https://127.0.0.1",
        )
    )
    print(request)


def test_post_access_token_refresh() -> None:

    request = PostAccessTokenRequest(
        request=Request(
            grant_type=GrantType.refresh_token,
            client_id="clien_id1234",
            refresh_token="refresh_token_1234",
        )
    )
    print(request)
