from litestar import Controller, MediaType, asgi
from litestar.enums import ScopeType
from litestar.response.base import ASGIResponse
from litestar.status_codes import HTTP_200_OK
from litestar.testing import create_test_client
from litestar.types import Receive, Scope, Send


def test_handle_asgi() -> None:
    @asgi(path="/")
    async def root_asgi_handler(scope: Scope, receive: Receive, send: Send) -> None:
        assert scope["type"] == ScopeType.HTTP
        assert scope["method"] == "GET"
        response = ASGIResponse(body=b"Hello World", media_type=MediaType.TEXT)
        await response(scope, receive, send)

    class MyController(Controller):
        path = "/asgi"

        @asgi()
        async def root_asgi_handler(self, scope: Scope, receive: Receive, send: Send) -> None:
            assert scope["type"] == ScopeType.HTTP
            assert scope["method"] == "GET"
            response = ASGIResponse(body=b"Hello World", media_type=MediaType.TEXT)
            await response(scope, receive, send)

    with create_test_client([root_asgi_handler, MyController]) as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello World"
        response = client.get("/asgi")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello World"


def test_asgi_signature_namespace() -> None:
    class MyController(Controller):
        path = "/asgi"
        signature_namespace = {"b": Receive}

        @asgi(signature_namespace={"c": Send})
        async def root_asgi_handler(
            self, scope: "a", receive: "b", send: "c"  # type:ignore[name-defined]  # noqa: F821
        ) -> None:
            await ASGIResponse(body=scope["path"].encode(), media_type=MediaType.TEXT)(scope, receive, send)

    with create_test_client([MyController], signature_namespace={"a": Scope}) as client:
        response = client.get("/asgi")
        assert response.status_code == HTTP_200_OK
        assert response.text == "/asgi"
