from . import messaging
from . import api

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
            self.engine.query(f"/v1/attendance/absence/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Absence(data) for data in self.engine.query("/v1/attendance/absence", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "Absence"):
        return Absence(
            self.engine.query("/v1/attendance/absence", "POST", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def delete_absence_relationship_to_response(self, message_id: int):
        self.engine.query(self.links.self + f"/relationship/response/{message_id}", "DELETE")

    def post_absence_response(self, payload: messaging.IncomingMessage):
        return messaging.IncomingMessage(
            self.engine.query(self.links.self + "/response", "POST", payload=payload.data)["data"]
        )

    def get_absence_responses(self, params: dict = None):
        return [
            messaging.IncomingMessage(data) for data in self.engine.query(self.links.self + "/responses", "GET", params=params)["data"]
        ]

class AbsenceReasonAttributes(api.Attributes):
    __slots__ = [
        "description",
        "internal_code",
        "shorthand",
        "is_explained",
        "is_default",
        "is_restricted"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AbsenceReasonLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AbsenceReason(api.Route):
    def __init__(self, data: dict):
        super().__init__(self)

    def set_attributes(self, data: dict):
        self.attributes = AbsenceReasonAttributes(data)

    def set_links(self, data: dict):
        self.links = AbsenceReasonLinks(data)

    @staticmethod
    def get(id: int):
        return AbsenceReason(
            self.engine.query(f"/v1/attendance/absence-reason/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AbsenceReason(data) for data in self.engine.query("/v1/attendance/absence-reason", "GET", params=params)["data"]
        ]

class AttendanceAttributes(api.Attributes):
    __slots__ = [
        "date",
        "school_time",
        "source"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AttendanceLinks(api.Links):
    __slots__ = [
        "self",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Attendance(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AttendanceAttributes(data)

    def set_links(self, data: dict):
        self.links = AttendanceLinks(data)

    @staticmethod
    def get(id: int):
        return Attendance(
            self.engine.query(f"/v1/attendance/attendance/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Attendance(data) for data in self.engine.query("/v1/attendance/attendance", "GET", params=params)["data"]
        ]

class CoreDayRollAttributes(api.Attributes):
    __slots__ = [
        "date",
        "submitted_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CoreDayRollRelationships(api.Relationships):
    __slots__ = [
        "core_roll_class",
        "absences"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CoreDayRollLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CoreDayRoll(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = CoreDayRollAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = CoreDayRollRelationships(data)

    def set_links(self, data: dict):
        self.links = CoreDayRollLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return CoreDayRoll(
            self.engine.query(f"/v1/attendance/core-day-roll/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            CoreDayRoll(data) for data in self.engine.query("/v1/attendance/core-day-roll", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "CoreDayRoll"):
        return CoreDayRoll(
            self.engine.query("/v1/attendance/core-day-roll", "POST", payload=payload.data)["data"]
        )

class DayRollAttributes(api.Attributes):
    __slots__ = [
        "date",
        "submitted",
        "roll_marking_url"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DayRollRelationships(api.Relationships):
    __slots__ = [
        "core_roll_class"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DayRollLinks(api.Links):
    __slots__ = [
        "self",
        "roll_class"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DayRoll(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DayRollAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = DayRollRelationships(data)

    def set_links(self, data: dict):
        self.links = DayRollLinks(data)

    @staticmethod
    def get(id: int):
        return DayRoll(
            self.engine.query(f"/v1/attendance/day-roll/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            DayRoll(data) for data in self.engine.query("/v1/attendance/day-roll", "GET", params=params)["data"]
        ]

class FutureAbsenceAttributes(api.Attributes):
    __slots__ = [
        "type",
        "start_date",
        "end_data",
        "start_time",
        "end_time",
        "comment",
        "category",
        "status"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsenceRelationships(api.Relationships):
    __slots__ = [
        "student",
        "reason",
        "future_absence_reason",
        "matching_absence"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsenceLinks(api.Links):
    __slots__ = [
        "self",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsence(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FutureAbsenceAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = FutureAbsenceRelationships(data)

    def set_links(self, data: dict):
        self.links = FutureAbsenceLinks(data)

    @staticmethod
    def get(id: int):
        return FutureAbsence(
            self.engine.query(f"/v1/attendance/future-absence/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            FutureAbsence(data) for data in self.engine.query("/v1/attendance/future-absence", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "FutureAbsence"):
        return FutureAbsence(
            self.engine.query("/v1/attendance/future-absence", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "FutureAbsence"):
        return FutureAbsence(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class FutureAbsenceReasonAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsenceReasonRelationships(api.Relationships):
    __slots__ = [
        "reason"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsenceReasonLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FutureAbsenceReason(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FutureAbsenceReasonAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = FutureAbsenceReasonRelationships(data)

    def set_links(self, data: dict):
        self.links = FutureAbsenceReasonLinks(data)

    @staticmethod
    def get(id: int):
        return FutureAbsenceReason(
            self.engine.query(f"/v1/attendance/future-absence-reason/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            FutureAbsenceReason(data) for data in self.engine.query("/v1/attendance/future-absence-reason", "GET", params=params)["data"]
        ]

class PeriodRollAttributes(api.Attributes):
    __slots__ = [
        "date",
        "period",
        "period_name",
        "class_time",
        "is_submitted",
        "start_time",
        "end_time",
        "roll_marking_url"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PeriodRollLinks(api.Links):
    __slots__ = [
        "self",
        "roll_class"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PeriodRoll(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PeriodRollAttributes(data)

    def set_links(self, data: dict):
        self.links = PeriodRollLinks(data)

    @staticmethod
    def get(id: int):
        return PeriodRoll(
            self.engine.query(f"/v1/attendance/period-roll/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PeriodRoll(data) for data in self.engine.query("/v1/attendance/period-roll", "GET", params=params)["data"]
        ]
