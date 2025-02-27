from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncGenerator, Awaitable, Callable, Generator

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

    from litestar.config.app import AppConfig
    from litestar.connection.base import ASGIConnection
    from litestar.connection.request import Request
    from litestar.handlers.base import BaseRouteHandler
    from litestar.handlers.http_handlers import HTTPRouteHandler
    from litestar.response.base import Response
    from litestar.types.asgi_types import ASGIApp, Message, Method, Scope
    from litestar.types.helper_types import SyncOrAsyncUnion
    from litestar.types.internal_types import LitestarType, PathParameterDefinition
    from litestar.types.protocols import Logger


AfterExceptionHookHandler: TypeAlias = "Callable[[Exception, Scope], SyncOrAsyncUnion[None]]"
AfterRequestHookHandler: TypeAlias = (
    "Callable[[ASGIApp], SyncOrAsyncUnion[ASGIApp]] | Callable[[Response], SyncOrAsyncUnion[Response]]"
)
AfterResponseHookHandler: TypeAlias = "Callable[[Request], SyncOrAsyncUnion[None]]"
AsyncAnyCallable: TypeAlias = Callable[..., Awaitable[Any]]
AnyCallable: TypeAlias = Callable[..., Any]
AnyGenerator: TypeAlias = "Generator[Any, Any, Any] | AsyncGenerator[Any, Any]"
BeforeMessageSendHookHandler: TypeAlias = "Callable[[Message, Scope], SyncOrAsyncUnion[None]]"
BeforeRequestHookHandler: TypeAlias = "Callable[[Request], Any | Awaitable[Any]]"
CacheKeyBuilder: TypeAlias = "Callable[[Request], str]"
ExceptionHandler: TypeAlias = "Callable[[Request, Exception], Response]"
ExceptionLoggingHandler: TypeAlias = "Callable[[Logger, Scope, list[str]], None]"
GetLogger: TypeAlias = "Callable[..., Logger]"
Guard: TypeAlias = "Callable[[ASGIConnection, BaseRouteHandler], SyncOrAsyncUnion[None]]"
LifespanHook: TypeAlias = "Callable[[LitestarType], SyncOrAsyncUnion[Any]] | Callable[[], SyncOrAsyncUnion[Any]]"
OnAppInitHandler: TypeAlias = "Callable[[AppConfig], AppConfig]"
OperationIDCreator: TypeAlias = "Callable[[HTTPRouteHandler, Method, list[str | PathParameterDefinition]], str]"
Serializer: TypeAlias = Callable[[Any], Any]
