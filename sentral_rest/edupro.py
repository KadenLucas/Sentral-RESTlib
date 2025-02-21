from . import api

class StudentAcademicReportAttributes(api.Attributes):
    __slots__ = [
        "year",
        "semester",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportRelationships(api.Relationships):
    __slots__ = [
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReport(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentAcademicReportAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentAcademicReportRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentAcademicReportLinks(data)

    def get(self, id: int):
        return StudentAcademicReport(
            self.engine.query(f"/v1/edupro/student-academic-report/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            StudentAcademicReport(data) for data in self.engine.query("/v1/edupro/student-academic-report", "GET", params=params)["data"]
        ]

    def get_file(self) -> bytes:
        return self.engine.query(self.links.self + "/file", "GET", raw=True)
