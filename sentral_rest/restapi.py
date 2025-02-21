from . import api

class RestapiExceptionLogAttributes(api.Attributes):
    __slots__ = [
        "type",
        "path",
        "body",
        "stacktrace",
        "previous_exceptions",
        "created_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RestapiExceptionLogLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RestapiExceptionLog(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def get_attributes(self, data: dict):
        self.attributes = RestapiExceptionLogAttributes(data)

    def get_links(self, data: dict):
        self.links = RestapiExceptionLogLinks(data)

    def get(self, id: int):
        return RestapiExceptionLog(
            self.engine.query(f"/v1/restapi/restapi-exception-log/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            RestapiExceptionLog(data) for data in self.engine.query("/v1/restapi/restapi-exception-log", "GET", params=params)["data"]
        ]
