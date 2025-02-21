from . import timetables
from . import api

class AdministrativeUserAttributes(api.Attributes):
    __slots__ = [
        "username",
        "title",
        "first_name",
        "last_name",
        "email",
        "provider",
        "provider_id",
        "external_id",
        "external_source",
        "created_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AdministrativeUserLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AdministrativeUser(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AdministrativeUserAttributes(data)

    def set_links(self, data: dict):
        self.links = AdministrativeUserLinks(data)

    @staticmethod
    def get(id: int):
        return AdministrativeUser(
            self.engine.query(f"/v1/core/core-administrative-user/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AdministrativeUser(data) for data in self.engine.query("/v1/core/core-administrative-user", "GET", params=params)["data"]
        ]

class ClassAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "year",
        "school_year",
        "external_id",
        "external_source",
        "ref_id",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ClassRelationships(api.Relationships):
    __slots__ = [
        "teacher",
        "assigned_students",
        "assigned_staff",
        "core_subject",
        "timetable_class"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ClassLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Class(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ClassAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ClassRelationships(data)

    def set_links(self, data: dict):
        self.links = ClassLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Class(
            self.engine.query(f"/v1/core/core-class/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Class(data) for data in self.engine.query("/v1/core/core-classes", "GET", params=params)["data"]
        ]

    def get_assigned_staff(self, params: dict = None):
        return [
            Staff(data) for data in self.engine.query(self.links.self + "/assigned-staff", "GET", params=params)["data"]
        ]

    def get_assigned_students(self, params: dict = None):
        return [
            Student(data) for data in self.engine.query(self.links.self + "/assigned-students", "GET", params=params)["data"]
        ]

class FamilyAttributes(api.Attributes):
    __slots__ = [
        "address_title",
        "address_po_box",
        "address_street_no",
        "address_street",
        "address_suburb",
        "address_state",
        "address_post_code",
        "is_out_of_area",
        "phone",
        "email_address",
        "contact_1_title",
        "contact_1_gender",
        "contact_1_surname",
        "contact_1_given_names",
        "contact_1_home_phone",
        "contact_1_work_phone",
        "contact_1_mobile",
        "contact_1_email",
        "contact_1_occupation",
        "contact_1_occupation_group",
        "contact_1_country_of_birth",
        "contact_1_nationality",
        "contact_1_language_home",
        "contact_1_language_other_1",
        "contact_1_language_other_2",
        "contact_1_interpreter_required",
        "contact_1_school_education",
        "contact_1_nonschool_education",
        "contact_2_title",
        "contact_2_gender",
        "contact_2_surname",
        "contact_2_given_names",
        "contact_2_home_phone",
        "contact_2_work_phone",
        "contact_2_mobile",
        "contact_2_email",
        "contact_2_occupation",
        "contact_2_occupation_group",
        "contact_2_country_of_birth",
        "contact_2_nationality",
        "contact_2_language_home",
        "contact_2_language_other_2",
        "contact_2_language_other_2",
        "contact_2_interpreter_required",
        "contact_2_school_education",
        "contact_2_nonschool_education",
        "emergency_contact_1_name",
        "emergency_contact_1_phone",
        "emergency_contact_1_mobile",
        "emergency_contact_1_email",
        "emergency_contact_1_relationship",
        "emergency_contact_2_name",
        "emergency_contact_2_phone",
        "emergency_contact_2_mobile",
        "emergency_contact_2_email",
        "emergency_contact_2_relationship",
        "external_id",
        "external_source",
        "ref_id",
        "created_at",
        "is_active"
    ]

class FamilyLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Family(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FamilyAttributes(data)

    def set_links(self, data: dict):
        self.links = FamilyLinks(data)

    @staticmethod
    def get(id: int):
        return Family(
            self.engine.query(f"/v1/core/core-family/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiuple(params: dict = None):
        return [
            Family(data) for data in self.engine.query("/v1/core/core-families", "GET", params=params)["data"]
        ]

class HolidayAttributes(api.Attributes):
    __slots__ = [
        "date",
        "name",
        "is_reoccuring",
        "is_whole_school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HolidayLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Holiday(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = HolidayAttributes(data)

    def set_links(self, data: dict):
        self.links = HolidayLinks(data)

    @staticmethod
    def get(id: int):
        return Holiday(
            self.engine.query(f"/v1/core/core-holiday/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Holiday(data) for data in self.engine.query("/v1/core/core-holiday", "GET", params=params)["data"]
        ]

class HouseAttributes(api.Attributes):
    __slots__ = [
        "name",
        "short_name",
        "colour",
        "external_source",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class House(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = HouseAttributes(data)

    def set_link(self, data: dict):
        self.links = HouseLinks(data)

    @staticmethod
    def get(id: int):
        return House(
            self.engine.query(f"/v1/core/core-house/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            House(data) for data in self.engine.query("/v1/core/core-house", "GET", params=params)["data"]
        ]

class PersonAttributes(api.Attributes):
    __slots__ = [
        "first_name",
        "last_name",
        "title",
        "preferred_name",
        "gender",
        "external_id",
        "is_deceased",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonRelationships(api.Relationships):
    __slots__ = [
        "enrolment_person",
        "student_contacts"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Person(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Person(
            self.engine.query(f"/v1/core/core-person/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Person(data) for data in self.engine.query("/v1/core/core-person", "GET", params=params)["data"]
        ]

    def get_student_contacts(self):
        return [
            StudentPersonRelation(data) for data in self.engine.query(self.links.self + "/contacts", "GET")["data"]
        ]

class StudentPersonRelationAttributes(api.Attributes):
    __slots__ = [
        "relationship",
        "is_residential_guardian",
        "is_emergency_contact",
        "is_authorised_pickup",
        "can_contact_via_sms",
        "can_contact_via_email",
        "can_contact_via_phone",
        "can_contact_via_letter",
        "can_receive_correspondence",
        "can_receive_portal_access",
        "can_receive_reports",
        "can_receive_sms",
        "can_receive_absences",
        "do_not_contact",
        "sequence",
        "external_id",
        "external_source"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPersonRelationRelationships(api.Relationships):
    __slots__ = [
        "core_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPersonRelationLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentPersonRelation(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentPersonRelationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentPersonRelationRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentPersonRelationLinks(data)

class RollClassAttributes(api.Attributes):
    __slots__ = [
        "name",
        "year",
        "external_id",
        "external_source",
        "ref_id",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollClassRelationships(api.Relationships):
    __slots__ = [
        "teacher",
        "assigned_students",
        "assigned_staff",
        "enrolment_rollclass"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollClassLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollClass(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = RollClassAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = RollClassRelationships(data)

    def set_links(self, data: dict):
        self.links = RollClassLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return RollClass(
            self.engine.query(f"/v1/core/core-rollclass/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return RollClass(
            self.engine.query("/v1/core/core-rollclass", "GET", params=params)["data"]
        )

class StaffAttributes(api.Attributes):
    __slots__ = [
        "title",
        "given_names",
        "last_name",
        "preferred_title",
        "preferred_first_name",
        "preferred_last_name",
        "gender",
        "date_of_birth",
        "mobile_phone",
        "phone_number",
        "phone_number_type",
        "email",
        "username",
        "emplyoment_status",
        "external_id",
        "external_source",
        "ref_id",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffRelationships(api.Relationships):
    __slots__ = [
        "enrolment_staff",
        "assigned_classes"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Staff(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Staff(
            self.engine.query(f"/v1/core/core-staff/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Staff(data) for data in self.engine.query("/v1/core/core-staff", "GET", params=params)["data"]
        ]

    def get_assigned_classes(self, params: dict = None):
        return [
            Class(data) for data in self.engine.query(self.links.self + "/assigned-classes", "GET", params=params)["data"]
        ]

class StudentAttributes(api.Attributes):
    __slots__ = [
        "first_name",
        "last_name",
        "preferred_name",
        "gender",
        "barcode",
        "exam_id",
        "school_year",
        "date_of_birth",
        "allergies",
        "medical_conditions",
        "external_id",
        "external_source",
        "username",
        "email",
        "mobile",
        "ref_id",
        "esl_support_needed",
        "esl_date_assessed",
        "is_esl_support_received",
        "enrol_date",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentRelationships(api.Relationships):
    __slots__ = [
        "enrolment_student",
        "additional_details",
        "core_roll_class",
        "attended_classes",
        "holidays",
        "student_relationships",
        "core_house",
        "family",
        "non_residential_family",
        "contacts"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Student(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Student(
            self.engine.query(f"/v1/core/core-student/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Student(data) for data in self.engine.query("/v1/core/core-student", "GET", params=params)["data"]
        ]

    def get_attended_classes(self, params: dict = None):
        return [
            Class(data) for data in self.engine.query(self.link.self + "/attended-classes", "GET", params=params)["data"]
        ]

    def get_contacts(self, params: dict = None):
        return [
            StudentPersonRelation(data) for data in self.engine.query(self.links.self + "/contacts", "GET", params=params)["data"]
        ]

    def get_photo(self, params: dict = None) -> bytes:
        return self.engine.query(self.links.self + "/photo", "GET", params=params, raw=True)

    def get_timetable_classes(self, params: dict = None):
        return [
            timetables.TimetableClass(data) for data in self.engine.query(self.links.self + "/time-table-classes", "GET", params=params)["data"]
        ]

class StudentRelationshipAttributes(api.Attributes):
    __slots__ = [
        "relationship",
        "is_residential_guardian",
        "is_emergency_contact",
        "sequence",
        "core_preson",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentRelationshipRelationships(api.Relationships):
    __slots__ = [
        "core_student",
        "core_person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentRelationshipLinks(api.Links):
    __slots__ = [
        "self",
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentRelationship(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentRelationshipAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentRelationshipRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentRelationshipLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return StudentRelationship(
            self.engine.query(f"/v1/core/core-student-relationship/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentRelationship(data) for data in self.engine.query("/v1/core/core-student-relationships", "GET", params=params)["data"]
        ]

class SubjectAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "external_id",
        "external_source",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SubjectLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Subject(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = SubjectAttributes(data)

    def set_links(self, data: dict):
        self.links = SubjectLinks(data)

    @staticmethod
    def get(id: int):
        return Subject(
            self.engine.query(f"/v1/core/core-subject/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Subject(data) for data in self.engine.query("/v1/core/core-subject", "GET", params=params)["data"]
        ]

class TermAttributes(api.Attributes):
    __slots__ = [
        "year",
        "term",
        "start_date",
        "end_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TermLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Term(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TermAttributes(data)

    def set_links(self, data: dict):
        self.links = TermLinks(data)

    @staticmethod
    def get(id: int):
        return Term(
            self.engine.query(f"/v1/core/core-term/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Term(data) for data in self.engine.query("/v1/core/core-terms", "GET", params=params)["data"]
        ]

class DateAttributes(api.Attributes):
    __slots__ = [
        "term",
        "week",
        "code"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DateLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Date(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = data

    def set_links(self, data: dict):
        self.links = data

    @staticmethod
    def get(id: int):
        return Date(
            self.engine.query(f"/v1/core/date/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Date(data) for data in self.engine.query("/v1/core/date", "GET", params=params)["data"]
        ]
