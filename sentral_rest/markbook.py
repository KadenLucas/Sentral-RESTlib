from . import api
from . import core
from . import enrolments

class MarkbookAttributes(api.Attributes):
    __slots__ = [
        "name",
        "year",
        "description",
        "external_source",
        "external_id"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MarkbookRelationships(api.Relationships):
    __slots__ = [
        "category",
        "created_by",
        "classes",
        "students"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MarkbookLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Markbook(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MarkbookAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MarkbookRelationships(data)

    def set_links(self, data: dict):
        self.links = MarkbookLinks(data)

    @staticmethod
    def get(id: int):
        return Markbook(
            self.engine.query(f"/v1/markbook/markbook/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Markbook(data) for data in self.engine.query("/v1/markbook/markbook", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "Markbook"):
        return Markbook(
            self.engine.query("/v1/markbook/markbook", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "Markbook"):
        return Markbook(
            self.engine.query(self.links.self, "GET", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def get_classes(self, params: dict = None):
        return [
            enrolments.Class(data) for data in self.engine.query(self.links.self + "/classes", "GET", params=params)["data"]
        ]

    def get_core_classes(self, params: dict = None):
        return [
            core.Class(data) for data in self.engine.query(self.links.self + "/core-classes", "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            enrolments.Student(data) for data in self.engine.query(self.links.self + "/students", "GET", params=params)["data"]
        ]

class CategoryAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CategoryRelationships(api.Relationships):
    __slots__ = [
        "created_by"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CategoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Category(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = CategoryAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = CategoryRelationships(data)

    def set_links(self, data: dict):
        self.links = CategoryLinks(data)

    @staticmethod
    def get(id: int):
        return Category(
            self.engine.query(f"/v1/markbook/markbook-category/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Category(data) for data in self.engine.query("/v1/markbook/markbook-category", "GET", params=params)["data"]
        ]

class ColumnAttributes(api.Attributes):
    __slots__ = [
        "name",
        "short_name",
        "type",
        "max_mark",
        "task_date",
        "display_precision"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ColumnRelationships(api.Relationships):
    __slots__ = [
        "markbook"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ColumnLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Column(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ColumnAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ColumnRelationships(data)

    def set_links(self, data: dict):
        self.links = ColumnLinks(data)

    @staticmethod
    def get(id: int):
        return Column(
            self.engine.query(f"/v1/markbook/markbook-column{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Column(data) for data in self.engine.query("/v1/markbook/markbook-column", "GET", params=params)["data"]
        ]

    def get_marks(self, params: dict = None):
        return [
            ColumnMark(data) for data in self.engine.query(self.links.self + "/marks", "GET", params=params)["data"]
        ]

class ColumnMarkAttributes(api.Attributes):
    __slots__ = [
        "mark"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ColumnMarkRelationships(api.Relationships):
    __slots__ = [
        "column",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ColumnMarkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ColumnMark(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ColumnMarkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ColumnMarkRelationships(data)

    def set_links(self, data: dict):
        self.links = ColumnMarkLinks(data)

    @staticmethod
    def get(id: int):
        return ColumnMark(
            self.engine.query(f"/v1/markbook/markbook-column-mark/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            ColumnMark(data) for data in self.engine.query("/v1/markbook/markbook-column-mark", "GET", params=params)["data"]
        ]
