from . import api

class StudentPlanAttributes(api.Attributes):
    __slots__ = [
        "additional_information",
        "comments",
        "is_completed"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPlanRelationships(api.Relationships):
    __slots__ = [
        "student",
        "created_by",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPlanLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPlan(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentPlanAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentPlanRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentPlanLinks(data)

    @staticmethod
    def get(id: int):
        return StudentPlan(
            self.engine.query(f"/v1/plans/student-plan/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentPlan(data) for data in self.engine.query("/v1/plans/student-plan", "GET", params=params)["data"]
        ]

    def get_file(self) -> bytes:
        return self.engine.query(self.links.self + "/published-file", "GET", raw=True)

class StudentPlanTypeAttributes(api.Attributes):
    __slots__ = [
        "display_name",
        "is_signature_required",
        "is_confidential",
        "show_in_parent_portal",
        "show_in_student_portal",
        "is_hidden"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPlanTypeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPlanType(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentPlanTypeAttributes(data)

    def set_links(self, data: dict):
        self.links = StudentPlanTypeLinks(data)

    @staticmethod
    def get(id: int):
        return StudentPlanType(
            self.engine.query(f"/v1/plans/student-plan-type/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentPlanType(data) for data in self.engine.query("/v1/plans/student-plan-type", "GET", params=params)["data"]
        ]
