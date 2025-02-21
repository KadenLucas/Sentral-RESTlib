from . import api

class IncomingMessageAttributes(api.Attributes):
    __slots__ = [
        "type",
        "message",
        "is_unsolicited"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class IncomingMessageLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class IncomingMessage(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = IncomingMessageAttributes(data)

    def set_links(self, data: dict):
        self.links = IncomingMessageLinks(data)

    @staticmethod
    def get(id: int):
        return IncomingMessage(
            self.engine.query(f"/v1/messaging/incoming-message/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            IncomingMessage(data) for data in self.engine.query("/v1/messaging/incoming-message", "GET", params=params)["data"]
        ]

class OutgoingMessageAttributes(api.Attributes):
    __slots__ = [
        "type",
        "subject",
        "content",
        "timestamp"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessageRelationships(api.Relationships):
    __slots__ = [
        "recipient"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessageLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessage(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = OutgoingMessageAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = OutgoingMessageRelationships(data)

    def set_links(self, data: dict):
        self.links = OutgoingMessageLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return OutgoingMessage(
            self.engine.query(f"/v1/messaging/outgoing-message/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            OutgoingMessage(data) for data in self.engine.query("/v1/messaging/outgoing-message", "GET", params=params)["data"]
        ]

    def get_recipients(self, params: dict = None):
        return [
            OutgoingMessageRecipient(data) for data in self.engine.query(self.links.self + "/recipients", "GET", params=params)["data"]
        ]

class OutgoingMessageRecipientAttributes(api.Attributes):
    __slots__ = [
        "delivery_status",
        "delivery_date_time",
        "recipient_title",
        "recipient_first_name",
        "recipient_last_name",
        "recipient_mobile_phone",
        "recipient_email"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessageRecipientRelationships(api.Relationships):
    __slots__ = [
        "subject_person",
        "recipient",
        "message"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessageRecipientLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OutgoingMessageRecipient(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = OutgoingMessageRecipientAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = OutgoingMessageRecipientRelationships(data)

    def set_links(self, data: dict):
        self.links = OutgoingMessageRecipientLinks(data)

    @staticmethod
    def get(id: int):
        return OutgoingMessageRecipient(
            self.engine.query(f"/v1/messaging/outgoing-message-recipient/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            OutgoingMessageRecipient(data) for data in self.engine.query("/v1/messaging/outgoing-message-recipient", "GET", params=params)["data"]
        ]
