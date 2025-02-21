from . import api
from . import core
from . import enrolments

class AcademicReportAssignmentMarkAttributes(api.Attributes):
    __slots__ = [
        "grade_weight",
        "calculated_grade_Weight"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportAssignmentMarkRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "report_schema_assignment",
        "report_grade",
        "report_calculated_grade",
        "core_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportAssignmentMarkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportAssignmentMark(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportAssignmentMarkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportAssignmentMarkRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportAssignmentMarkLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportAssignmentMark(
            self.engine.query(f"/v1/reports/academic-report-assignment-mark/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportAssignmentMark(data) for data in self.engine.query("/v1/reports/academic-report-assignment-mark", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "AcademicReportAssignmentMark"):
        return AcademicReportAssignmentMark(
            self.engine.query("/v1/reports/academic-report-assignment-mark", "POST", payload=payload.data)["data"]
        )

class AcademicReportClassAttributes(api.Attributes):
    __slots__ = [
        "name",
        "import_type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClassRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "core_class",
        "core_rollclass",
        "enrolment_class",
        "enrolment_rollclass",
        "report_cohorts"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClassLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClass(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportClassAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportClassRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportClassLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportClass(
            self.engine.query(f"/v1/reports/academic-report-class/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportClass(data) for data in self.engine.query("/v1/reports/academic-report-class", "GET", params=params)["data"]
        ]

    def get_report_cohorts(self):
        return [
            AcademicReportClassCohort(data) for data in self.engine.query(self.links.self + "/report-cohorts", "GET")
        ]

class AcademicReportClassCohortAttributes(api.Attributes):
    __slots__ = [
        "name",
        "class_name",
        "cohort_type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClassCohortRelationships(api.Relationships):
    __slots__ = [
        "report_class",
        "report_schema",
        "enrolment_students",
        "core_students"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClassCohortLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportClassCohort(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportClassCohortAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportClassCohortRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportClassCohortLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportClassCohort(
            self.engine.query(f"/v1/reports/academic-report-class-cohort/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportClassCohort(data) for data in self.engine.query("/v1/reports/academic-report-class-cohort", "GET", params=params)["data"]
        ]

    def get_core_students(self, params: dict = None):
        return [
            core.Student(data) for data in self.engine.query(self.links.self + "/core-students", "GET", params=params)["data"]
        ]

    def get_enrolment_students(self, params: dict = None):
        return [
            enrolments.Student(data) for data in self.engine.query(self.links.self + "/enrolment-students", "GET", params=params)["data"]
        ]

class AcademicReportCommentTypeAttributes(api.Attributes):
    __slots__ = [
        "label",
        "print_label",
        "comment_type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportCommentTypeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportCommentType(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportCommentTypeAttributes(data)

    def set_links(self, data: dict):
        self.links = AcademicReportCommentTypeLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportCommentType(
            self.engine.query(f"/v1/reports/acadeimc-report-comment-type/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportCommentType(data) for data in self.engine.query("/v1/reports/academic-report-comment-type", "GET", params=params)["data"]
        ]

class AcademicReportPeriodCommentAttributes(api.Attributes):
    __slots__ = [
        "comment"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportPeriodCommentRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "report_comment_type",
        "core_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportPeriodCommentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportPeriodComment(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportPeriodCommentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportPeriodCommentRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportPeriodCommentLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportPeriodComment(
            self.engine.query(f"/v1/reports/academic-report-period-comment/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportPeriodComment(data) for data in self.engine.query("/v1/reports/academic-report-period-comment", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "AcademicReportPeriodComment"):
        return AcademicReportPeriodComment(
            self.engine.query("/v1/reports/academic-report-period-comment", "POST", payload=payload.data)["data"]
        )

class AcademicReportScaleAttributes(api.Attributes):
    __slots__ = [
        "name",
        "scale",
        "type",
        "data_type",
        "sort"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScaleRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "report_grades"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScaleLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScale(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportScaleAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportScaleRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportScaleLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return AcademicReportScale(
            self.engine.query(f"/v1/reports/academic-report-scale/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportScale(data) for data in self.engine.query("/v1/reports/academic-report-scale", "GET", params=params)["data"]
        ]

    def get_report_grades(self):
        return [
            AcademicReportScaleGrade(data) for data in self.engine.query(self.links.self + "/report-grades", "GET")["data"]
        ]

class AcademicReportScaleGradeAttributes(api.Attributes):
    __slots__ = [
        "name",
        "short_name",
        "description",
        "grade",
        "weight"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScaleGradeRelationships(api.Relationships):
    __slots__ = [
        "report_scale"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScaleGradeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportScaleGrade(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportScaleGradeAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportScaleGradeRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportScaleGradeLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportScaleGrade(
            self.engine.query(f"/v1/reports/academic-report-scale-grade/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportScaleGrade(data) for data in self.engine.query("/v1/reports/academic-report-scale-grade", "GET", params=params)["data"]
        ]

class AcademicReportSchemaAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "report_achievement_scale",
        "report_effort_scale",
        "report_attitude_scale",
        "report_comment_types"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchema(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportSchemaAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportSchemaRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportSchemaLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return AcademicReportSchema(
            self.engine.query(f"/v1/reports/academic-report-schema/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportSchema(data) for data in self.engine.query("/v1/reports/academic-report-schema", "GET", params=params)["data"]
        ]

    def get_comment_types(self):
        return [
            AcademicReportCommentType(data) for data in self.engine.query(self.links.self + "/report-comment-types", "GET")["data"]
        ]

class AcademicReportSchemaAssignmentAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignmentRelationships(api.Relationships):
    __slots__ = [
        "report_period",
        "report_schema",
        "report_scale",
        "report_subject",
        "report_strand",
        "report_comment_types"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignmentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignment(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportSchemaAssignmentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportSchemaAssignmentRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportSchemaAssignmentLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return AcademicReportSchemaAssignment(
            self.engine.query(f"/v1/reports/academic-report-schema-assignment/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportSchemaAssignment(data) for data in self.engine.query("/v1/reports/academic-report-schema-assignment", "GET", params=params)["data"]
        ]

    def get_comment_types(self):
        return [
            AcademicReportCommentType(data) for data in self.engine.query(self.links.self + "/report-comment-types", "GET")["data"]
        ]

class AcademicReportSchemaAssignmentCommentAttributes(api.Attributes):
    __slots__ = [
        "comment",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignmentCommentRelationships(api.Relationships):
    __slots__ = [
        "schema_assignment",
        "report_comment_type",
        "core_student",
        "author"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignmentCommentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSchemaAssignmentComment(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportSchemaAssignmentCommentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportSchemaAssignmentCommentRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportSchemaAssignmentCommentLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportSchemaAssignmentComment(
            self.engine.query(f"/v1/reports/academic-report-schema-assignment-comment/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportSchemaAssignmentComment(data) for data in self.engine.query("/v1/reports/academic-report-schema-assignment-comment", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "AcademicReportSchemaAssignmentComment"):
        return AcademicReportSchemaAssignmentComment(
            self.engine.query("/v1/reports/academic-report-schema-assignment-comment", "POST", payload=payload.data)["data"]
        )

class AcademicReportStrandAttributes(api.Attributes):
    __slots__ = [
        "name",
        "short_name",
        "code"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportStrandRelationships(api.Relationships):
    __slots__ = [
        "report_subject"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportStrandLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportStrand(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportStrandAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportStrandRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportStrandLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportStrand(
            self.engine.query(f"/v1/reports/academic-report-strand/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportStrand(data) for data in self.engine.query("/v1/reports/academic-report-strand", "GET", params=params)["data"]
        ]

class AcademicReportSubjectAttributes(api.Attributes):
    __slots__ = [
        "name",
        "short_name",
        "code"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSubjectRelationships(api.Relationships):
    __slots__ = [
        "report_period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSubjectLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicReportSubject(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicReportSubjectAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AcademicReportSubjectRelationships(data)

    def set_links(self, data: dict):
        self.links = AcademicReportSubjectLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicReportSubject(
            self.engine.query(f"/v1/reports/academic-report-subject/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicReportSubject(data) for data in self.engine.query("/v1/reports/academic-report-subject", "GET", params=params)["data"]
        ]

    def get_schema_assignments(self, params: dict = None):
        return [
            AcademicReportSchemaAssignment(data) for data in self.engine.query(self.links.self + "/schema-assignments", "GET", params=params)["data"]
        ]

class StudentAcademicReportAttributes(api.Attributes):
    __slots__ = [
        "published_date_time",
        "year",
        "semester",
        "reporting_period",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportRelationships(api.Relationships):
    __slots__ = [
        "student",
        "period"
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

    @staticmethod
    def get(id: int):
        return StudentAcademicReport(
            self.engine.query(f"/v1/reports/student-academic-report/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentAcademicReport(data) for data in self.engine.query("/v1/reports/student-academic-report")["data"]
        ]

    def get_file(self) -> bytes:
        return self.engine.session.get(f"/v1/reports/student-academic-report/{self.id}/file").content

class StudentAcademicReportPeriodAttributes(api.Attributes):
    __slots__ = [
        "name",
        "year",
        "semester",
        "style",
        "attendance_import_type",
        "partial_attendance_grouping_type",
        "start_date",
        "end_date",
        "locked_date",
        "unlocked_until",
        "attendance_start_date",
        "attendance_end_date",
        "attendance_last_import_date",
        "is_filtered_by_start_date",
        "is_staff_signoff_enabled",
        "is_self_assessment_enabled",
        "is_overall_self_assessment_enabled",
        "is_subject_self_assessment_enabled",
        "is_showing_attendance_whole_day_tallies",
        "is_showing_attendance_partial_tallies",
        "is_showing_attendance_late_tallies",
        "is_showing_attendance_overall_tallies",
        "is_showing_attendance_explained_tallies",
        "is_showing_attendance_unexplained_tallies",
        "is_showing_attendance_exempt_tallies",
        "is_published",
        "is_using_decimal_values_in_course_results",
        "is_secondary_scales_enabled",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportPeriodRelationships(api.Relationships):
    __slots__ = [
        "reference_reporting_period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportPeriodLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentAcademicReportPeriod(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes =StudentAcademicReportPeriodAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentAcademicReportPeriodRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentAcademicReportPeriodLinks(data)

    @staticmethod
    def get(id: int):
        return StudentAcademicReportPeriod(
            self.engine.query(f"/v1/reports/student-academic-report-period/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentAcademicReportPeriod(data) for data in self.engine.query("/v1/reports/student-academic-report-period", "GET", params=params)["data"]
        ]

    def get_classes(self): # Sentral made a typo
        return [
            AcademicReportClass(data) for data in self.engine.query(self.links.self + "/c;asses", "GET")["data"]
        ]

    def get_scales(self, params: dict = None):
        return [
            AcademicReportScale(data) for data in self.engine.query(self.links.self + "/scales", "GET", params=params)["data"]
        ]

    def get_subjects(self, params: dict = None):
        return [
            AcademicReportSubject(data) for data in self.engine.query(self.links.self + "/subjects", "GET", params=params)["data"]
        ]
