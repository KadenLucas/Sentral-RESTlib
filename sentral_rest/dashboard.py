from . import api

class NoticeAttributes(api.Attributes):
    __slots__ = [
        "type",
        "source",
        "subject",
        "body",
        "is_html",
        "created_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoticeRelationships(api.Relationships):
    __slots__ = [
        "sender",
        "recipients"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoticeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Notice(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = NoticeAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = NoticeRelationships(data)

    def set_links(self, data: dict):
        self.links = NoticeLinks(data)

    @staticmethod
    def get(id: int):
        return Notice(
            self.engine.query(f"/v1/dashboard/dashboard-notice/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Notice(data) for data in self.engine.query("/v1/dashboard/dashboard-notice", "GET", params=params)["data"]
        ]

    def get_recipients(self, params: dict = None):
        return [
            NoticeRecipient(data) for data in self.engine.query(self.links.self + "/recipients", "GET", params=params)["data"]
        ]

class NoticeRecipientAttributes(api.Attributes):
    __slots__ = [
        "status"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoticeRecipientRelationships(api.Relationships):
    __slots__ = [
        "notice",
        "recipient"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoticeRecipientLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoticeRecipient(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = NoticeRecipientAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = NoticeRecipientRelationships(data)

    def set_links(self, data: dict):
        self.links = NoticeRecipientLinks(data)

    @staticmethod
    def get(id: int):
        return NoticeRecipient(
            self.engine.query(f"/v1/dashboard/dashboard-notice-recipient/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            NoticeRecipient(data) for data in self.engine.query("/v1/dashboard/dashboard-notice-recipient", "GET", params=params)["data"]
        ]

    def patch(self, payload: "NoticeRecipient"):
        return NoticeRecipient(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )
