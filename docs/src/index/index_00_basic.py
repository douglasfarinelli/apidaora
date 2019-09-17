from dataclasses import dataclass
from http import HTTPStatus

from dataclassesjson import dataclassjson

from dataclassesapi import App, MethodType, Route
from dataclassesapi.request import Query, Request
from dataclassesapi.response import Body as ResponseBody
from dataclassesapi.response import Response


@dataclass
class MyQuery(Query):
    name: str


@dataclass
class MyRequest(Request):
    query: MyQuery


@dataclass
class MyResponseBody(ResponseBody):
    message: str


@dataclassjson
@dataclass
class MyResponse(Response):
    body: MyResponseBody


def hello_controller(req: MyRequest) -> MyResponse:
    name = req.query.name
    body = MyResponseBody(message=f'Hello {name}!')
    return MyResponse(HTTPStatus.OK, body=body)


class MyApp(App):
    _routes = (Route('/hello', MethodType.GET, hello_controller),)


app = MyApp()
