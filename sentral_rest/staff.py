from . import api
from . import messaging

class AbsenceAttributes(api.Attributes):
    __slots__ = [
        "type",
        "date",
        "start",
        "end",
        "comment",
        "explainer",
        "explainer_source",
        "letter_sent",
        "bulk_absence_id",
        "submitted"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AbsenceRelationships(api.Relationships):
    __slots__ = [
        "reason",
        "enrolment_student",
        "core_student",
        "matching_future_absence"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AbsenceLinks(api.Links):
    __slots__ = [
        "self",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Absence(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AbsenceAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AbsenceRelationships(data)

    def set_links(self, data: dict):
        self.links = AbsenceLinks(data)

    @staticmethod
    def get(id: int):
        return Absence(
            self.engine.query(f"/v1/staff/absence/{id}", "GET")
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Absence(data) for data in self.engine.query("/v1/staff/absence", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "Absence"):
        return Absence(
            self.engine.query("/v1/staff/absence", "POST", payload=payload.data)["data"]
        )

    def get_responses(self):
        return [
            messaging.IncomingMessage(data) for data in self.engine.query(self.links.self + "/responses", "GET")["data"]
        ]

    def get_attachments(self, params: dict = None):
        return [
            AbsenceAttachment(data) for data in self.engine.query(self.links.self + "/attachments", "GET", params=params)["data"]
        ]

    def post_attachment(self, payload: "AbsenceAttachment"):
        # Upload via "multipart/form-data" under key "attachment"
        pass

class AbsenceAttachment(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)
