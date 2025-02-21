from . import api
from . import core

class TimetableCalendarDateAttributes(api.Attributes):
    __slots__ = [
        "date",
        "cycle",
        "interval",
        "is_daily_timetable"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableCalendarDateRelationships(api.Relationships):
    __slots__ = [
        "day"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableCalendarDateLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableCalendarDate(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableCalendarDateAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableCalendarDateRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableCalendarDateLinks(data)

    @staticmethod
    def get(id: int):
        return TimetableCalendarDate(
            self.engine.query(f"/v1/timetables/timetable-calendar-date/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableCalendarDate(data) for data in self.engine.query("/v1/timetables/timetable-calendar-date", "GET", params=params)["data"]
        ]

class TimetableClassAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableClassRelationships(api.Relationships):
    __slots__ = [
        "subject",
        "timetable_students"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableClassLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableClass(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableClassAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableClassRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableClassLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return TimetableClass(
            self.engine.query(f"/v1/timetables/timetable-class/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableClass(data) for data in self.engine.query("/v1/timetables/timetable-class", "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            TimetableStudent(data) for data in self.engine.query(self.links.self + "/timetable-students", "GET", params=params)["data"]
        ]

class TimetableClassLessonRelationships(api.Relationships):
    __slots__ = [
        "class",
        "room",
        "period_in_day",
        "timetable_students",
        "timetable_teachers",
        "core_students",
        "core_staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableClassLessonLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableClassLesson(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableClassLessonRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableClassLessonLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return TimetableClassLesson(
            self.engine.query(f"/v1/timetables/timetable-class-lesson/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableClassLesson(data) for data in self.engine.query("/v1/timetables/timetable-class-lesson", "GET", params=params)["data"]
        ]

    def get_core_staff(self, params: dict = None):
        return [
            core.Staff(data) for data in self.engine.query(self.links.self + "/core-staff", "GET", params=params)["data"]
        ]

    def get_core_students(self, params: dict = None):
        return [
            core.Student(data) for data in self.engine.query(self.links.self + "/core-students", "GET", params=params)["data"]
        ]

    def get_timetable_students(self, params: dict = None):
        return [
            TimetableStudent(data) for data in self.engine.query(self.links.self + "timetable-students", "GET", params=params)["data"]
        ]

    def get_timetable_teachers(self, params: dict = None):
        return [
            TimetableTeacher(data) for data in self.engine.query(self.links.self + "timetable-teachers", "GET", params=params)["data"]
        ]

class TimetableDailyLessonAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type",
        "date",
        "start_time",
        "end_time"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableDailyLessonRelationships(api.Relationships):
    __slots__ = [
        "class",
        "period",
        "period_in_day",
        "room",
        "timetable_students",
        "timetable_teachers",
        "core_students",
        "core_staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableDailyLessonLinks(api.Links):
    __slots__ = [
        "links"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableDailyLesson(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableDailyLessonAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableDailyLessonRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableDailyLessonLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return TimetableDailyLesson(
            self.engine.query(f"/v1/timetables/timetable-daily-lesson/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableDailyLesson(data) for data in self.engine.query("/v1/timetables/timetable-daily-lesson", "GET", params=params)["data"]
        ]

    def get_core_staff(self, params: dict = None):
        return [
            core.Staff(data) for data in self.engine.query(self.links.self + "/core-staff", "GET", params=params)["data"]
        ]

    def get_core_students(self, params: dict = None):
        return [
            core.Student(data) for data in self.engine.query(self.links.self + "/core-students", "GET", params=params)["data"]
        ]

    def get_timetable_teachers(self, params: dict = None):
        return [
            TimetableTeacher(data) for data in self.engine.query(self.links.self + "/timetable-teachers", "GET", params=params)["data"]
        ]

    def get_timetable_student(self, params: dict = None):
        return [
            TimetableStudent(data) for data in self.engine.query(self.links.self + "/timetable-student", "GET", params=params)["data"]
        ]

class TimetableDayAttributes(api.Attributes):
    __slots__ = [
        "name",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableDayLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableDay(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableDayAttributes(data)

    def set_links(self, data: dict):
        self.links = TimetableDayLinks(data)

    @staticmethod
    def get(id: int):
        return TimetableDay(
            self.engine.query(f"/v1/timetables/timetable-day/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableDay(data) for data in self.engine.query("/v1/timetables/timetable-day", "GET", params=params)["data"]
        ]

class TimetableLessonAttributes(api.Attributes):
    __slots__ = [
        "class_name",
        "subject",
        "room_name",
        "teacher_name",
        "teacher_ids",
        "date",
        "day_name",
        "day_order",
        "period_name",
        "period_order",
        "start_time",
        "end_time",
        "colour",
        "class_type",
        "roll_marking_url"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableLessonRelationships(api.Relationships):
    __slots__ = [
        "related_student",
        "related_staff",
        "related_core_student",
        "related_core_staff"
        "related_timetable_class"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableLesson(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableLessonAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableLessonRelationships(data)

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableLesson(data) for data in self.engine.query("/v1/timetables/timetable-lesson", "GET", params=params)["data"]
        ]

class TimetablePeriodAttributes(api.Attributes):
    __slots__ = [
        "name",
        "order",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetablePeriodLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetablePeriod(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetablePeriodAttributes(data)

    def set_links(self, data: dict):
        self.links = TimetablePeriodLinks(data)

    @staticmethod
    def get(id: int):
        return TimetablePeriod(
            self.engine.query(f"/v1/timetables/timetable-period/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetablePeriod(data) for data in self.engine.query("/v1/timetables/timetable-period", "GET", params=params)["data"]
        ]

class TimetablePeriodInDayAttributes(api.Attributes):
    __slots__ = [
        "name",
        "order",
        "start_time",
        "end_time",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetablePeriodInDayRelationships(api.Relationships):
    __slots__ = [
        "day",
        "period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetablePeriodInDayLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetablePeriodInDay(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetablePeriodInDayAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetablePeriodInDayRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetablePeriodInDayLinks(data)

    @staticmethod
    def get(id: int):
        return TimetablePeriodInDay(
            self.engine.query(f"/v1/timetables/timetable-period-in-day/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetablePeriodInDay(data) for data in self.engine.query("/v1/timetables/timetable-period-in-day", "GET", params=params)["data"]
        ]

class TimetableRoomAttributes(api.Attributes):
    __slots__ = [
        "name",
        "capacity",
        "comment",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableRoomLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableRoom(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableRoomAttributes(data)

    def set_links(self, data: dict):
        self.links = TimetableRoomLinks(data)

    @staticmethod
    def get(id: int):
        return TimetableRoom(
            self.engine.query(f"/v1/timetables/timetable-room/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableRoom(data) for data in self.engine.query("/v1/timetables/timetable-room", "GET", params=params)["data"]
        ]

class TimetableStudentAttributes(api.Attributes):
    __slots__ = [
        "first_name",
        "last_name",
        "year",
        "gender"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableStudentRelationships(api.Relationships):
    __slots__ = [
        "core_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableStudentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableStudent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableStudentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableStudentRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableStudentLinks(data)

    @staticmethod
    def get(id: int):
        return TimetableStudent(
            self.engine.query(f"/v1/timetables/timetable-student/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableStudent(data) for data in self.engine.query("/v1/timetable/timetable-student", "GET", params=params)["data"]
        ]

class TimetableTeacherAttributes(api.Attributes):
    __slots__ = [
        "title",
        "first_name",
        "last_name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableTeacherRelationships(api.Relationships):
    __slots__ = [
        "core_staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableTeacherLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableTeacher(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableTeacherAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TimetableTeacherRelationships(data)

    def set_links(self, data: dict):
        self.links = TimetableTeacherLinks(data)

class TimetableSubjectAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableSubjectLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TimetableSubject(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TimetableSubjectAttributes(data)

    def set_links(self, data: dict):
        self.links = TimetableSubjectLinks(data)

    @staticmethod
    def get(id: int):
        return TimetableSubject(
            self.engine.query(f"/v1/timetables/timetable-subject/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            TimetableSubject(data) for data in self.engine.query("/v1/timetables/timetable-subject", "GET", params=params)["data"]
        ]
