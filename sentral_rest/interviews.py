from . import api
from . import enrolments

class InterviewBookingAttributes(api.Attributes):
    __slots__ = [
        "start_time",
        "end_time",
        "notes",
        "has_parent_attended",
        "is_interpreter_required",
        "is_booking_confirmed",
        "parent_name",
        "interview_session_id",
        "interview_session_date_id",
        "interview_class_link_id"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewBookingRelationships(api.Relationships):
    __slots__ = [
        "session",
        "date",
        "class_link",
        "student",
        "parent_user"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewBookingLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewBooking(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InterviewBookingAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = InterviewBookingRelationships(data)

    def set_links(self, data: dict):
        self.links = InterviewBookingLinks(data)

    @staticmethod
    def get(id: int):
        return InterviewBooking(
            self.engine.query(f"/v1/interviews/interview-booking/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            InterviewBooking(data) for data in self.engine.query("/v1/interviews/interview-booking", "GET", params=params)["data"]
        ]

class InterviewClassLinkAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewClassLinkRelationships(api.Relationships):
    __slots__ = [
        "class_",
        "rollclass",
        "teacher"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewClassLinkLinks(api.Links):
    __slots__ = [
        "self",
        "interview_session",
        "class_",
        "rollclass",
        "students"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewClassLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InterviewClassLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = InterviewClassLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = InterviewClassLinkLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return InterviewClassLink(
            self.engine.query(f"/v1/interviews/interview-class-link/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            InterviewClassLink(data) for data in self.engine.query("/v1/interviews/interview-class-link", "GET", params=params)["data"]
        ]

    def get_class(self):
        return enrolments.Class(
            self.engine.query(self.links.class_, "GET")["data"]
        )

    def get_session(self):
        return InterviewSession(
            self.engine.query(self.links.interview_session, "GET")["data"]
        )

    def get_rollclass(self):
        return enrolments.Rollclass(
            self.engine.query(self.links.rollclass, "GET")["data"]
        )

    def get_students(self, params: dict = None):
        return [
            enrolments.Student(data) for data in self.engine.query(self.links.students, "GET", params=params)["data"]
        ]

class InterviewSessionAttributes(api.Attributes):
    __slots__ = [
        "name",
        "event_description",
        "event_location",
        "registration_open",
        "registration_close"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewSessionLinks(api.Links):
    __slots__ = [
        "self",
        "dates",
        "class_links",
        "classes",
        "rollclasses",
        "students",
        "bookings"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewSession(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InterviewSessionAttributes(data)

    def set_links(self, data: dict):
        self.links = InterviewSessionLinks(data)

    @staticmethod
    def get(id: int):
        return InterviewSession(
            self.engine.query(f"/v1/interviews/interview-session/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            InterviewSession(data) for data in self.engine.query("/v1/interviews/interview-session", "GET", params=params)["data"]
        ]

    def get_bookings(self, params: dict = None):
        return [
            InterviewBooking(data) for data in self.engine.query(self.links.bookings, "GET", params=params)["data"]
        ]

    def get_class_links(self, params: dict = None):
        return [
            InterviewClassLink(data) for data in self.engine.query(self.links.class_links, "GET", params=params)["data"]
        ]

    def get_classes(self, params: dict = None):
        return [
            enrolments.Class(data) for data in self.engine.query(self.links.classes, "GET", params=params)["data"]
        ]

    def get_dates(self, params: dict = None):
        return [
            InterviewSessionDate(data) for data in self.engine.query(self.links.dates, "GET", params=params)["data"]
        ]

    def get_rollclasses(self, params: dict = None):
        return [
            enrolments.Rollclass(data) for data in self.engine.query(self.links.rollclasses, "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            enrolments.Student(data) for data in self.engine.query(self.links.students, "GET", params=params)["data"]
        ]

class InterviewSessionDateAttributes(api.Attributes):
    __slots__ = [
        "date",
        "start_time",
        "end_time"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewSessionDateLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InterviewSessionDate(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InterviewSessionDateAttributes(data)

    def set_links(self, data: dict):
        self.links = InterviewSessionDateLinks(data)

    @staticmethod
    def get(id: int):
        return InterviewSessionDate(
            self.engine.query(f"/v1/interviews/interview-session-date/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            InterviewSessionDate(data) for data in self.engine.query("/v1/interviews/interview-session-date", "GET", params=params)["data"]
        ]
