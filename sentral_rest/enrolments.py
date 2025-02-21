from . import api
from . import core
from . import edupro
from . import reports
from . import enterprise
from . import timetables
from . import attendance
from . import activities
from . import welfare

class AbilityAttributes(api.Attributes):
    __slots__ = [
        "type",
        "level",
        "details",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AbilityLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Ability(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AbilityAttributes(data)

    def set_link(self, data: dict):
        self.links = AbilityLinks(data)

    @staticmethod
    def get(id: int):
        return Ability(
            self.engine.query(f"/v1/enrolments/ability/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Ability(data) for data in self.engine.query("/v1/enrolments/ability", "GET", params=params)["data"]
        ]

class AcademicPeriodAttributes(api.Attributes):
    __slots__ = [
        "name",
        "year",
        "start_date",
        "end_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicPeriodLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AcademicPeriod(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AcademicPeriodAttributes(data)

    def set_links(self, data: dict):
        self.links = AcademicPeriodLinks(data)

    @staticmethod
    def get(id: int):
        return AcademicPeriod(
            self.engine.query(f"/v1/enrolments/academic-period/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            AcademicPeriod(data) for data in self.engine.query("/v1/enrolments/academic-period", "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            Student(data) for data in self.engine.query(self.links.self + "/students", "GET", params=params)["data"]
        ]

class CampusAttributes(api.Attributes):
    __slots__ = [
        "name",
        "created_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CampusRelationships(api.Relationships):
    __slots__ = [
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CampusLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Campus(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = CampusAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = CampusRelationships(data)

    def set_links(self, data: dict):
        self.links = CampusLinks(data)

    @staticmethod
    def get(id: int):
        return Campus(
            self.engine.query(f"/v1/enrolments/campus/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Campus(data) for data in self.engine.query("/v1/enrolments/campus", "GET", params=params)["data"]
        ]

class ClassAttributes(api.Attributes):
    __slots__ = [
        "name",
        "identifier"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ClassRelationships(api.Relationships):
    __slots__ = [
        "teachers",
        "students",
        "subject"
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
    def get(id: int):
        return Class(
            self.engine.query(f"/v1/enrolments/class/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Class(data) for data in self.engine.query("/v1/enrolments/class", "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            Student(data) for data in self.engine.query(self.links.self + "/students", "GET", params=params)["data"]
        ]

class ClassSubjectAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ClassSubjectLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ClassSubject(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ClassSubjectAttributes(data)

    def set_links(self, data: dict):
        self.links = ClassSubjectLinks(data)

    @staticmethod
    def get(id: int):
        return ClassSubject(
            self.engine.query(f"/v1/enrolments/class-subject/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            ClassSubject(data) for data in self.engine.query("/v1/enrolments/class-subject", "GET", params=params)["data"]
        ]

class ConsentAttributes(api.Attributes):
    __slots__ = [
        "type",
        "details",
        "default_expire_on",
        "is_default_consent",
        "is_active",
        "in_inactive"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ConsentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Consent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ConsentAttributes(data)

    def set_links(self, data: dict):
        self.links = ConsentLinks(data)

    @staticmethod
    def get(id: int):
        return Consent(
            self.engine.query(f"/v1/enrolments/consent/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Consent(data) for data in self.engine.query("/v1/enrolments/consent", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "Consent"):
        return Consent(
            self.engine.query("/v1/enrolments/consent", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "Consent"):
        return Consent(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class CourtOrderAttributes(api.Attributes):
    __slots__ = [
        "type",
        "case_id",
        "title",
        "school_notes",
        "order_notes",
        "start_date",
        "review_date",
        "end_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CourtOrderRelationships(api.Relationships):
    __slots__ = [
        "schools",
        "students",
        "persons"
    ]

    def __init__(self, data: dict):
        super().__init__(self)

class CourtOrderLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CourtOrder(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = CourtOrderAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = CourtOrderRelationships(data)

    def set_links(self, data: dict):
        self.links = CourtOrderLinks(data)

    @staticmethod
    def get(id: int):
        return CourtOrder(
            self.engine.query(f"/v1/enrolments/court-order/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            CourtOrder(data) for data in self.engine.query("/v1/enrolments/court-order", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "CourtOrder"):
        return CourtOrder(
            self.engine.query("/v1/enrolments/court-order", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "CourtOrder"):
        return CourtOrder(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class DisabilityOtherAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "receives_funding",
        "has_care_plan_provided"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DisabilityOtherRelationships(api.Relationships):
    __slots__ = [
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DisabilityOtherLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DisabilityOther(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DisabilityOtherAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = DisabilityOtherRelationships(data)

    def set_links(self, data: dict):
        self.links = DisabilityOtherLinks(data)

    @staticmethod
    def get(id: int):
        return DisabilityOther(
            self.engine.query(f"/v1/enrolments/disability-other/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            DisabilityOther(data) for data in self.engine.query("/v1/enrolments/disability-other", "GET", params=params)["data"]
        ]

    def get_care_plan_file(self) -> bytes:
        return self.engine.query(self.links.self + "/care-plan-file", "GET", raw=True)

class DoctorAttributes(api.Attributes):
    __slots__ = [
        "type",
        "name",
        "practice_name",
        "address",
        "phone",
        "consent_to_contact"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DoctorRelationships(api.Relationships):
    __slots__ = [
        "patient"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DoctorLinks(api.Links):
    __slots__ = [
        "self",
        "patient"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Doctor(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DoctorAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = DoctorRelationships(data)

    def set_links(self, data: dict):
        self.links = DoctorLinks(self)

    @staticmethod
    def get(id: int):
        return Doctor(
            self.engine.query(f"/v1/enrolments/doctor/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Doctor(data) for data in self.engine.query("/v1/enrolments/doctor", "GET", params=params)["data"]
        ]

    def get_related_person(self, params: dict = None):
        return Person(
            self.engine.query(self.links.self + "/person", "GET", params=params)["data"]
        )

class EmergencyContactLinkAttributes(api.Attributes):
    __slots__ = [
        "priority",
        "name",
        "phone",
        "alt_phone",
        "address",
        "relationship"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EmergencyContactLinkRelationships(api.Relationships):
    __slots__ = [
        "person",
        "person_to_contact"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EmergencyContactLinkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EmergencyContactLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EmergencyContactLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = EmergencyContactLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = EmergencyContactLinkLinks(data)

    @staticmethod
    def get(id: int):
        return EmergencyContactLink(
            self.engine.query(f"/v1/enrolments/emergency-contact-link/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            EmergencyContactLink(data) for data in self.engine.query("/v1/enrolments/emergency-contact-link", "GET", params=params)["data"]
        ]

class EnrolmentAttributes(api.Attributes):
    __slots__ = [
        "start_date",
        "end_date",
        "status",
        "school",
        "school_year",
        "roll_class",
        "is_boarding",
        "boarding_house",
        "tutor_group",
        "fte_amount",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentRelationships(api.Relationships):
    __slots__ = [
        "student",
        "house",
        "rollclass",
        "classes",
        "school",
        "year_level",
        "academic_period",
        "campus"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentLinks(api.Links):
    __slots__ = [
        "self",
        "house",
        "classes",
        "rollclass"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Enrolment(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EnrolmentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = EnrolmentRelationships(data)

    def set_links(self, data: dict):
        self.links = EnrolmentLinks(data)

    @staticmethod
    def get(id: int):
        return Enrolment(
            self.engine.query(f"/v1/enrolments/enrolment/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Enrolment(data) for data in self.engine.query("/v1/enrolments/enrolment", "GET", params=params)["data"]
        ]

    def patch(self, payload: "Enrolment"):
        return Enrolment(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def get_classes(self, params: dict = None):
        return [
            Class(data) for data in self.engine.query(self.links.classes, "GET", params=params)["data"]
        ]

    def get_house(self):
        return House(
            self.engine.query(self.links.house, "GET")["data"]
        )

    def get_rollclass(self):
        return Rollclass(
            self.engine.query(self.links.rollclass, "GET")["data"]
        )

class EnrolmentClassLinkRelationships(api.Relationships):
    __slots__ = [
        "enrolment",
        "class_"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentClassLinkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentClassLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_relationships(self, data: dict):
        self.relationships = EnrolmentClassLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = EnrolmentClassLinkLinks(data)

    @staticmethod
    def get(id: int):
        return EnrolmentClassLink(
            self.engine.query(f"/v1/enrolments/enrolment-class-link/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            EnrolmentClassLink(data) for data in self.engine.query("/v1/enrolments/enrolment-class-link", "GET", params=params)["data"]
        ]

class EnrolmentPriorityAttributes(api.Attributes):
    __slots__ = [
        "name",
        "code",
        "description",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentPriorityLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentPriority(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EnrolmentPriorityAttributes(data)

    def set_links(self, data: dict):
        self.links = EnrolmentPriorityLinks(data)

    @staticmethod
    def get(id: int):
        return EnrolmentPriority(
            self.engine.query(f"/v1/enrolments/enrolment-priority/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            EnrolmentPriority(data) for data in self.engine.query("/v1/enrolments/enrolment-priority", "GET", params=params)["data"]
        ]

class EnrolmentSpecialityAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentSpecialityRelationships(api.Relationships):
    __slots__ = [
        "category"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentSpecialityLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentSpeciality(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EnrolmentSpecialityAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = EnrolmentSpecialityRelationships(data)

    def set_links(self, data: dict):
        self.links = EnrolmentSpecialityLinks(data)

    @staticmethod
    def get(id: int):
        return EnrolmentSpeciality(
            self.engine.query(f"/v1/enrolments/enrolment-speciality/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            EnrolmentSpeciality(data) for data in self.engine.query("/v1/enrolments/enrolment-speciality", "GET", params=params)["data"]
        ]

class EnrolmentSpecialityCategoryAttributes(api.Attributes):
    __slots__ = [
        "name",
        "is_built_in"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentSpecialityCategoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnrolmentSpecialityCategory(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EnrolmentSpecialityCategoryAttributes(data)

    def set_links(self, data: dict):
        self.links = EnrolmentSpecialityCategoryLinks(data)

    @staticmethod
    def get(id: int):
        return EnrolmentSpecialityCategory(
            self.engine.query(f"/v1/enrolments/enrolment-speciality-category/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            EnrolmentSpecialityCategory(data) for data in self.engine.query("/v1/enrolments/enrolment-speciality-category", "GET", params=params)["data"]
        ]

class FlagAttributes(api.Attributes):
    __slots__ = [
        "internal_name",
        "name",
        "color",
        "show_in_sentral",
        "show_in_fees",
        "is_disabled",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FlagRelationships(api.Relationships):
    __slots__ = [
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FlagLinks(api.Links):
    __slots__ = [
        "self",
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Flag(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FlagAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = FlagRelationships(data)

    def set_links(self, data: dict):
        self.links = FlagLinks(data)

    @staticmethod
    def get(id: int):
        return Flag(
            self.engine.query(f"/v1/enrolments/flag/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Flag(data) for data in self.engine.query("/v1/enrolments/flag", "GET", params=params)["data"]
        ]

    def get_school(self, params: dict = None):
        return School(
            self.engine.query(self.links.school, "GET", params=params)["data"]
        )

class HouseAttributes(api.Attributes):
    __slots__ = [
        "name",
        "sequence"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseRelationships(api.Relationships):
    __slots__ = [
        "students",
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseLinks(api.Links):
    __slots__ = [
        "self",
        "students"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class House(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = HouseAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = HouseRelationships(data)

    def set_links(self, data: dict):
        self.links = HouseLinks(data)

    @staticmethod
    def get(id: int):
        return House(
            self.engine.query(f"/v1/enrolments/house/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            House(data) for data in self.engine.query("/v1/enrolments/house", "GET", params=params)["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            Student(data) for data in self.engine.query(self.links.students, "GET", params=params)["data"]
        ]

class HouseholdAttributes(api.Attributes):
    __slots__ = [
        "householed_code",
        "address",
        "mailing_title"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseholdRelationships(api.Relationships):
    __slots__ = [
        "addresses"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseholdLinks(api.Links):
    __slots__ = [
        "self",
        "addresses"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Household(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = HouseholdAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = HouseholdRelationships(data)

    def set_links(self, data: dict):
        self.links = HouseholdLinks(data)

    @staticmethod
    def get(id: int):
        return Household(
            self.engine.query(f"/v1/enrolments/household/{id}", "GET")["data"]
        )

    @staticmethod
    def get_mutliple(params: dict = None):
        return [
            Household(data) for data in self.engine.query("/v1/enrolments/household", "GET", params=params)["data"]
        ]

    def get_addresses(self):
        return [
            HouseholdAddress(data) for data in self.engine.query(self.links.addresses, "GET")["data"]
        ]

class HouseholdAddressAttributes(api.Attributes):
    __slots__ = [
        "type",
        "lot_number",
        "unit_number",
        "street_number",
        "house_number",
        "block_number",
        "floor_number",
        "property_name",
        "street_name",
        "street_type",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "suburb",
        "section",
        "city",
        "state",
        "country",
        "postcode",
        "comment",
        "locality",
        "province",
        "start_date",
        "end_date",
        "mailing_title",
        "is_billing_address",
        "is_valid",
        "is_simple_address"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseholdAddressRelationships(api.Relationships):
    __slots__ = [
        "household"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseholdAddressLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class HouseholdAddress(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = HouseholdAddressAttributes(data)

    def set_relationships(self, data: dict):
        self.relatioships = HouseholdAddressRelationships(data)

    def set_links(self, data: dict):
        self.links = HouseholdAddressLinks(data)

    @staticmethod
    def get(id: int):
        return HouseholdAddress(
            self.engine.query(f"/v1/enrolments/household-address/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            HouseholdAddress(data) for data in self.engine.query("/v1/enrolments/household-address", "GET", params=params)["data"]
        ]

class MedicalConditionRelationships(api.Relationships):
    __slots__ = [
        "person",
        "care_plan_file",
        "doctors_letter"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionLinks(api.Links):
    __slots__ = [
        "self",
        "person",
        "care_plan_file",
        "doctors_letter"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalCondition(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    @staticmethod
    def match(data: dict):
        match data.get("type"):
            case "medicalConditionAdd":
                return MedicalConditionAdd(data)

            case "medicalConditionAllergy":
                return MedicalConditionAllergy(data)

            case "medicalConditionAsthma":
                return MedicalConditionAsthma(data)

            case "medicalConditionDiabetes":
                return MedicalConditionDiabetes(data)

            case "medicalConditionEpilepsy":
                return MedicalConditionEpilepsy(data)

            case "medicalConditionOther":
                return MedicalConditionOther(data)

    @staticmethod
    def get(id: int):
        for data in self.engine.query(f"/v1/enrolments/medical-condition/{id}", "GET")["oneOf"]:
            return MedicalCondition.match(data["data"])

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalCondition.match(data) for data in self.engine.query("/v1/enrolments/medical-condition", "GET", params=params)["data"]
        ]

    def get_care_plan_file(self) -> bytes:
        return self.engine.query(self.links.care_plan_file, "GET", raw=True)

    def get_doctors_letter(self) -> bytes:
        return self.engine.query(self.links.doctors_letter, "GET", raw=True)

class MedicalConditionAddAttributes(api.Attributes):
    __slots__ = [
        "name",
        "has_care_plan_provided",
        "severity",
        "is_inattentive",
        "is_hyperactive",
        "is_medication_required",
        "is_doctors_letter_provided",
        "details",
        "additional_information"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionAdd(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionAddAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionAllergyAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "additional_information",
        "has_care_plan_provided",
        "allergy_name",
        "severity",
        "is_prescribed_antihistamine",
        "is_prescribed_epi_pen",
        "has_epi_pen_registered"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionAllergy(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionAllergyAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionAsthmaAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "additional_information",
        "severity",
        "dosage",
        "type",
        "has_care_plan_provided",
        "is_prescribed_salbutamol"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionAsthma(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionAsthmaAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionDiabetesAttributes(api.Attributes):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "has_care_plan_provided",
        "has_insulin_injections",
        "has_insuling_pump",
        "has_glucagon"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionDiabetes(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionDiabetesAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionEpilepsyAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "severity",
        "additional_information",
        "has_care_plan_provided",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionEpilepsy(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionEpilepsyAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionOtherAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "severity",
        "additional_information",
        "has_care_plan_provided"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionOther(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionOtherAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionLinks(data)

class MedicalConditionTypeAttributes(api.Attributes):
    __slots__ = [
        "name",
        "enorlment_model_name",
        "change_model_name",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionTypeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalConditionType(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalConditionTypeAttributes(data)

    def set_links(self, data: dict):
        self.links = MedicalConditionTypeLinks(data)

    @staticmethod
    def get(id: int):
        return MedicalConditionType(
            self.engine.query(f"/v1/enrolments/medical-condition-type/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalConditionType(data) for data in self.engine.query("/v1/enrolments/medical-condition-type", "GET", params=params)["data"]
        ]

class NoteTypeAttributes(api.Attributes):
    __slots__ = [
        "name",
        "is_built_in"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoteTypeRelationships(api.Relationships):
    __slots__ = [
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoteTypeLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class NoteType(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = NoteTypeAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = NoteTypeRelationships(data)

    def set_links(self, data: dict):
        self.links = NoteTypeLinks(data)

    @staticmethod
    def get(id: int):
        return NoteType(
            self.engine.query(f"/v1/enrolments/note-type/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            NoteType(data) for data in self.engine.query("/v1/enrolments/note-type", "GET", params=params)["data"]
        ]

class PersonAttributes(api.Attributes):
    __slots__ = [
        "external_id",
        "ref_id",
        "contact_code",
        "name",
        "surname",
        "first_name",
        "middle_names",
        "last_name",
        "legal_last_name",
        "email",
        "title",
        "preferred_name",
        "given_names",
        "gender",
        "gender_description",
        "gender_code",
        "date_of_birth",
        "date_of_death",
        "crn",
        "other_langauge",
        "other_language_code",
        "language_spoken_at_home",
        "language_spoken_at_home_code",
        "indigenous_status",
        "indigenous_status_code",
        "nationality",
        "nationality_code",
        "country_of_citizenship",
        "country_of_citizenship_code",
        "religion",
        "religion_code",
        "country_of_birth",
        "country_of_birth_code",
        "ethnic_group",
        "ethnic_group_code",
        "place_of_birth",
        "residential_status",
        "residential_status_code",
        "is_deceased",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonRelationships(api.Relationships):
    __slots__ = [
        "primary_household",
        "student_primary_enrolment",
        "staff",
        "student",
        "contact_details",
        "other_households",
        "student_contacts",
        "student_tenants",
        "prescribed_medication",
        "doctors",
        "associated_students",
        "emails",
        "phone_numbers",
        "given_consents",
        "given_consent_links",
        "emergency_contact_links",
        "abilities",
        "additional_fields"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonLinks(api.Links):
    __slots__ = [
        "self",
        "primary_household",
        "other_households",
        "staff",
        "student",
        "student_contacts",
        "medical_summary",
        "medical_conditions",
        "prescribed_medications",
        "doctors",
        "associated_students"
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

    def set_link(self, data: dict):
        self.links = PersonLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Person(
            self.engine.query(f"/v1/enrolments/person/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Person(data) for data in self.engine.query("/v1/enrolments/person", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "Person"):
        return Person(
            self.engine.query("/v1/enrolments/person", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "Person"):
        return Person(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def get_associated_students(self, params: dict = None):
        return [
            core.StudentPersonRelation(data) for data in self.engine.query(self.links.associated_students, "GET", params=params)["data"]
        ]

    def get_disabilities(self, params: dict = None):
        return [
            DisabilityOther(data) for data in self.engine.query(self.links.self + "/disabilities", "GET", params=params)["data"]
        ]

    def get_doctors(self, params: dict = None):
        return [
            Doctor(data) for data in self.engine.query(self.links.doctors, "GET", params=params)["data"]
        ]

    def get_given_consent_links(self, params: dict = None):
        return [
            PersonConsentLink(data) for data in self.engine.query(self.links.self + "/given-consent-links", "GET", params=params)["data"]
        ]

    def get_given_consents(self, params: dict = None):
        return [
            Consent(data) for data in self.engine.query(self.links.self + "/given-consents", "GET", params=params)["data"]
        ]

    def get_medical_conditions(self, params: dict = None):
        return [
            MedicalCondition.match(data) for data in self.engine.query(self.links.medical_conditions, "GET", params=params)["data"]
        ]

    def get_medical_summary(self, params: dict = None):
        return [
            MedicalSummary.match(data) for data in self.engine.query(self.links.medical_summary, "GET", params=params)["data"]
        ]

    def get_other_households(self, params: dict = None):
        return [
            Household(data) for data in self.engine.query(self.links.other_households, "GET", params=params)["data"]
        ]

    def get_contact_details(self):
        return PersonContactDetails(
            self.engine.query(self.links.self + "/person-contact-details", "GET")["data"]
        )

    def get_prescribed_medications(self, params: dict = None):
        return [
            PrescribedMedication(data) for data in self.engine.query(self.links.prescribed_medications, "GET", params=params)["data"]
        ]

    def get_primary_household(self, params: dict = None):
        return Household(
            self.engine.query(self.links.primary_household, "GET", params=params)["data"]
        )

    def get_staff(self, params: dict = None):
        return Staff(
            self.engine.query(self.links.staff, "GET", params=params)["data"]
        )

    def get_student(self, params: dict = None):
        return Student(
            self.engine.query(self.links.student, "GET", params=params)["data"]
        )

    def get_student_contacts(self, params: dict = None):
        return core.StudentPersonRelation(
            self.engine.query(self.links.student_contacts, "GET", params=params)["data"]
        )

    def get_vaccinations(self, params: dict = None):
        return [
            Vaccination(data) for data in self.engine.query(self.links.self + "/vaccinations", "GET", params=params)["data"]
        ]

    @staticmethod
    def get_by_code(id: int, params: dict = None):
        return Person(
            self.engine.query(f"/v1/enrolments/person-by-code/{id}", "GET", params=params)["data"]
        )

class MedicalSummary(api.Route):
    @staticmethod
    def match(data: dict):
        type_ = data.get("type")

        if type_.starswith("medicalCondition"):
            return MedicalCondition.match(data)

        match type_:
            case "vaccination":
                return Vaccination(data)

            case "doctor":
                return Doctor(data)

            case "prescribedMedication":
                return PrescribedMedication(data)

class PersonAddressAttributes(api.Attributes):
    __slots__ = [
        "type",
        "lot_number",
        "unit_number",
        "street_number",
        "house_number",
        "block_number",
        "floor_number",
        "property_name",
        "street_name",
        "street_type",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "suburb",
        "section",
        "city",
        "state",
        "country",
        "postcode",
        "comment",
        "locality",
        "province",
        "start_date",
        "end_date",
        "mailing_title",
        "is_billing_address",
        "is_valid",
        "is_simple_address",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonAddressRelationships(api.Relationships):
    __slots__ = [
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonAddressLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonAddress(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonAddressAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonAddressRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonAddressLinks(data)

    @staticmethod
    def get(id: int):
        return PersonAddress(
            self.engine.query(f"/v1/enrolments/person-address/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonAddress(data) for data in self.engine.query("/v1/enrolments/person-address", "GET", params=params)["data"]
        ]

class PersonConsentLinkAttributes(api.Attributes):
    __slots__ = [
        "consent_date",
        "consent_given",
        "expire_on",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonConsentLinkRelationships(api.Relationships):
    __slots__ = [
        "person",
        "consent",
        "consented_by"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonConsentLinkLinks(api.Links):
    __slots__ = [
        "self",
        "person",
        "consent"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonConsentLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonConsentLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonConsentLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonConsentLinkRelationships(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return PersonConsentLink(
            self.engine.query(f"/v1/enrolments/person-consent-link/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonConsentLink(data) for data in self.engine.query("/v1/enrolments/person-consent-link", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "PersonConsentLink"):
        return PersonConsentLink(
            self.engine.query("/v1/enrolments/person-consent-link", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "PersonConsentLink"):
        return PersonConsentLink(
            self.engine.query("/v1/enrolments/person-consent-link", "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class PersonContactDetailsAttributes(api.Attributes):
    __slots__ = [
        "education_level",
        "tertiary_education_level",
        "occupation",
        "employer",
        "employment_type",
        "workplace_location",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonContactDetailsRelationships(api.Relationships):
    __slots__ = [
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonContactDetailsLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonContactDetails(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonContactDetailsAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonContactDetailsRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonContactDetailsLinks(data)

    @staticmethod
    def get(id: int):
        return PersonContactDetails(
            self.engine.query(f"/v1/enrolments/person-contact-details/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonContactDetails(data) for data in self.engine.query("/v1/enrolments/person-contact-details", "GET", params=params)["data"]
        ]

    def patch(self, payload: "PersonContactDetails"):
        return PersonContactDetails(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class PersonEmailAttributes(api.Attributes):
    __slots__ = [
        "email",
        "type",
        "type_name",
        "can_contact"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonEmailRelationships(api.Relationships):
    __slots__ = [
        "owner"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonEmailLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonEmail(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attirbutes = PersonEmailAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonEmailRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonEmailLinks(data)

    @staticmethod
    def get(id: int):
        return PersonEmail(
            self.engine.query(f"/v1/enrolments/person-email/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonEmail(data) for data in self.engine.query("/v1/enrolments/person-email", "GET")["data"]
        ]

    @staticmethod
    def post(payload: "PersonEmail"):
        return PersonEmail(
            self.engine.query("/v1/enrolments/person-email", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "PersonEmail"):
        return PersonEmail(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")["data"]

class PersonFieldAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type",
        "value_type",
        "area",
        "min_length",
        "max_length"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonFieldRelationships(api.Relationships):
    __slots__ = [
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonFieldLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonField(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonFieldAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonFieldRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonFieldLinks(data)

    @staticmethod
    def get(id: int):
        return PersonField(
            self.engine.query(f"/v1/enrolments/person-field/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple():
        return [
            PersonField(data) for data in self.engine.query("/v1/enrolments/person-field", "GET")["data"]
        ]

class PersonFieldValueAttributes(api.Attributes):
    __slots__ = [
        "value"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonFieldValueRelationships(api.Relationships):
    __slots__ = [
        "person",
        "field"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonFieldValueLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonFieldValue(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonFieldValueAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonFieldValueRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonFieldValueLinks(data)

    @staticmethod
    def get(id: int):
        return PersonFieldValue(
            self.engine.query(f"/v1/enrolments/person-field-value/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple():
        return [
            PersonFieldValue(data) for data in self.engine.query("/v1/enrolments/person-field-value", "GET")["data"]
        ]

class PersonHouseholdRelationAttributes(api.Attributes):
    __slots__ = [
        "is_primary_household",
        "is_primary_contact",
        "is_authorised_contact",
        "is_authorised_pickup",
        "residential_household"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonHouseholdRelationRelationships(api.Relationships):
    __slots__ = [
        "person",
        "household"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonHouseholdRelationLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonHouseholdRelation(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonHouseholdRelationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonHouseholdRelationRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonHouseholdRelationLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return PersonHouseholdRelation(
            self.engine.query(f"/v1/enrolments/person-household-relation/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonHouseholdRelation(data) for data in self.engine.query("/v1/enrolments/person-household-relation", "GET", params=params)["data"]
        ]

class PersonMedicalMiscAttributes(api.Attributes):
    __slots__ = [
        "has_long_term_medication",
        "was_medication_advice_form_received",
        "last_date_of_tetanus_injection",
        "can_over_counter_medicine_salbutamol",
        "can_over_counter_medicine_paracetamol",
        "can_over_counter_medicine_ibuprofen",
        "can_over_counter_medicine_antihistamine",
        "ambulance_cover_provider",
        "medicare_number",
        "medicare_expiry_date",
        "medicare_position_on_card",
        "private_medical_fund",
        "private_medical_fund_number",
        "private_medical_fund_expiry_date",
        "has_parent_acknowledged",
        "are_vaccinations_up_to_date",
        "has_measles_exclusion",
        "has_ambulance_cover",
        "has_private_hospital_cover",
        "health_care_card_number"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonMedicalMiscRelationships(api.Relationships):
    __slots__ = [
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonMedicalMiscLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonMedicalMisc(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonMedicalMiscAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonMedicalMiscRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonMedicalMiscLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return PersonMedicalMisc(
            self.engine.query(f"/v1/enrolments/person-medical-misc/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonMedicalMisc(data) for data in self.engine.query("/v1/enrolments/person-medical-misc", "GET")["data"]
        ]

class PersonNameAttributes(api.Attributes):
    __slots__ = [
        "family_name",
        "legal_family_name",
        "first_name",
        "middle_name",
        "preferred_name",
        "authority_for_name_change",
        "name_type",
        "date_of_name_change"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonNameRelationships(api.Relationships):
    __slots__ = [
        "named_person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonNameLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonName(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonNameAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonNameRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonNameLinks(data)

    @staticmethod
    def get(id: int):
        return PersonName(
            self.engine.query(f"/v1/enrolments/person-name/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonName(data) for data in self.engine.query("/v1/enrolments/person-name", "GET")["data"]
        ]

class PersonPassportAttributes(api.Attributes):
    __slots__ = [
        "number",
        "country",
        "country_code",
        "is_primary",
        "issue_date",
        "expirey_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPassportRelationships(api.Relationships):
    __slots__ = [
        "holder",
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPassportLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPassport(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonPassportAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonPassportRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonPassportLinks(data)

    @staticmethod
    def get(id: int):
        return PersonPassport(
            self.engine.query(f"/v1/enrolments/person-passport/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonPassport(data) for data in self.engine.query("/v1/enrolments/person-passport", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "PersonPassport"):
        return PersonPassport(
            self.engine.query("/v1/enrolments/person-passport", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "PersonPassport"):
        return PersonPassport(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class PersonPhoneAttributes(api.Attributes):
    __slots__ = [
        "number",
        "extensions",
        "type",
        "type_name",
        "is_listed",
        "can_contact"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPhoneRelationships(api.Relationships):
    __slots__ = [
        "owner"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPhoneLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonPhone(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonPhoneAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonPhoneRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonPhoneLinks(data)

    @staticmethod
    def get(id: int):
        return PersonPhone(
            self.engine.query(f"/v1/enrolments/person-phone/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonPhone(data) for data in self.engine.query("/v1/enrolments/person-phone", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "PersonPhone"):
        return PersonPhone(
            self.engine.query("/v1/enrolments/person-phone", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "PersonPhone"):
        return PersonPhone(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class PersonSpecialityLinkAttributes(api.Attributes):
    __slots__ = [
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonSpecialityLinkRelationships(api.Relationships):
    __slots__ = [
        "person",
        "speciality"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonSpecialityLinkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonSpecialityLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonSpecialityLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonSpecialityLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonSpecialityLinkLinks(data)

    @staticmethod
    def get(id: int):
        return PersonSpecialityLink(
            self.engine.query(f"/v1/enrolments/person-speciality-link/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonSpecialityLink(data) for data in self.engine.query("/v1/enrolments/person-speciality-link", "GET")["datas"]
        ]

class PersonVisaAttributes(api.Attributes):
    __slots__ = [
        "visa_class",
        "visa_sub_class",
        "grant_number",
        "statistical_code",
        "issue_date",
        "expiry_date",
        "application_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonVisaRelationships(api.Relationships):
    __slots__ = [
        "holder"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonVisaLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PersonVisa(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PersonVisaAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PersonVisaRelationships(data)

    def set_links(self, data: dict):
        self.links = PersonVisaLinks(data)

    @staticmethod
    def get(id: int):
        return PersonVisa(
            self.engine.query(f"/v1/enrolments/person-visa/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PersonVisa(data) for data in self.engine.query("/v1/enrolments/person-visa}", "GET")["data"]
        ]

    @staticmethod
    def post(payload: dict = None):
        return PersonVisa("/v1/enrolments/person-visa", "GET", payload=payload.data)

    def patch(self, payload: "PersonVisa"):
        return PersonVisa(self.links.self, "PATCH", payload=payload.dict)

class PrescribedMedicationAttributes(api.Attributes):
    __slots__ = [
        "name",
        "dosage",
        "type",
        "details",
        "is_prescribed",
        "is_taken_at_school",
        "is_long_term",
        "anticipated_stop_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PrescribedMedicationRelationships(api.Relationships):
    __slots__ = [
        "person",
        "condition"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PrescribedMedicationLinks(api.Links):
    __slots__ = [
        "self",
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PrescribedMedication(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PrescribedMedicationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = PrescribedMedicationRelationships(data)

    def set_links(self, data: dict):
        self.links = PrescribedMedicationLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return PrescribedMedication(
            self.engine.query(f"/v1/enrolments/prescribed-medication/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            PrescribedMedication(data) for data in self.engine.query("/v1/enrolments/prescribed-medication", "GET")["data"]
        ]

class RollclassAttributes(api.Attributes):
    __slots__ = [
        "name",
        'is_pastoral_care',
        "pastoral_care",
        "ref_id",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollclassRelationships(api.Relationships):
    __slots__ = [
        "teacher",
        "school",
        "academic_period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollclassLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Rollclass(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = RollclassAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = RollclassRelationships(data)

    def set_links(self, data: dict):
        self.links = RollclassLinks(data)

    @staticmethod
    def get(id: int):
        return Rollclass(
            self.engine.query(f"/v1/enrolments/rollclass/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Rollclass(data) for data in self.engine.query("/v1/enrolments/rollclass", "GET")["data"]
        ]

    def get_students(self, params: dict = None):
        return [
            Student(data) for data in self.engine.query(self.links.self + "/students", "GET", params=params)["data"]
        ]

class SchoolAttributes(api.Attributes):
    __slots__ = [
        "name",
        "school_code",
        "sequence",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SchoolRelationships(api.Relationships):
    __slots__ = [
        "tenant"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SchoolLinks(api.Links):
    __slots__ = [
        "self",
        "tenant"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class School(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = SchoolAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = SchoolRelationships(data)

    def set_links(self, data: dict):
        self.links = SchoolLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return School(
            self.engine.query(f"/v1/enrolments/school/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            School(data) for data in self.engine.query("/v1/enrolments/school", "GET", params=params)["data"]
        ]

    def get_tenant(self, params: dict = None):
        return enterprise.Tenant(
            self.engine.query(self.links.tenant, "GET", params=params)["data"]
        )

class SpecialNeedsProgramAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SpecialNeedsProgramRelationships(api.Relationships):
    __slots__ = [
        "school",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SpecialNeedsProgramLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class SpecialNeedsProgram(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = SpecialNeedsProgramAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = SpecialNeedsProgramRelationships(data)

    def set_links(self, data: dict):
        self.links = SpecialNeedsProgramLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return SpecialNeedsProgram(
            self.engine.query(f"/v1/enrolments/special-needs-program/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            SpecialNeedsProgram(data) for data in self.engine.query("/v1/enrolments/special-needs-program", "GET", params=params)["data"]
        ]

class StaffAttributes(api.Attributes):
    __slots__ = [
        "staff_code",
        "timetable_code",
        "barcode",
        "emergency_contact_name",
        "emergency_contact_phone",
        "emergency_contact_mobile",
        "employment_status",
        "employment_classification",
        "job_title",
        "contract_commencement_date",
        "contract_expiry_date",
        "w_w_c_c_number",
        "w_w_c_c_status",
        "w_w_c_c_expiry_date",
        "code_of_conduct_date_signed",
        "social_networking_policy_date_signed",
        "child_protection_policy_date_signed",
        "i_c_t_policy_date_signed",
        "first_aid_expiry_date",
        "resuscitation_expiry_date",
        "public_liability_expiry_date",
        "a_g_s_number",
        "position_number",
        "pay_rate",
        "staff_activity",
        "staff_activity_code",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffRelationships(api.Relationships):
    __slots__ = [
        "person",
        "absences",
        "qualifications",
        "employments"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffLinks(api.Links):
    __slots__ = [
        "self",
        "person",
        "absences"
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
            self.engine.query(f"/v1/enrolments/staff/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Staff(data) for data in self.engine.query("/v1/enrolments/staff", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(self, payload: "Staff"):
        return Staff(
            self.engine.query(f"/v1/enrolments/staff/{id}", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "Staff"):
        return Staff(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def get_absences(self, params: dict = None):
        return [
            attendance.StaffAbsence(data) for data in self.engine.query(self.links.absences, "GET", params=params)["data"]
        ]

    def get_person(self, params: dict = None):
        return Person(
            self.engine.query(self.links.person, "GET", params=params)["data"]
        )

    def get_photo(self, params: dict = None) -> bytes:
        return self.engine.query(self.links.self + "/photo", "GET", params=params, raw=True)

    def get_qualifications(self):
        return [
            StaffQualification(data) for data in self.engine.query(self.links.self + "/qualifications", "GET")["data"]
        ]

    def get_lessons(self, params: dict = None):
        return [
            timetables.TimetableLesson(data) for data in self.engine.query(self.links.self + "/timetable-lessons", "GET", params=params)["data"]
        ]

class StaffCarAttributes(api.Attributes):
    __slots__ = [
        "make",
        "model",
        "colour",
        "insurer",
        "number_plate"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffCarRelationships(api.Relationships):
    __slots__ = [
        "staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffCarLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffCar(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffCarAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffCarRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffCarLinks(data)

    @staticmethod
    def get(id: int):
        return StaffCar(
            self.engine.query(f"/v1/enrolments/staff-car/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffCar(data) for data in self.engine.query("/v1/enrolments/staff-car", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StaffCar"):
        return StaffCar(
            self.engine.query("/v1/enrolments/staff-car", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StaffCar"):
        return StaffCar(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        return StaffCar(
            self.engine.query(self.links.self, "DELETE")["data"]
        )

class StaffDocumentAttributes(api.Attributes):
    __slots__ = [
        "file_name",
        "is_confidential"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffDocumentRelationships(api.Relationships):
    __slots__ = [
        "category",
        "staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffDocumentLinks(api.Links):
    __slots__ = [
        "self",
        "file"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffDocument(api.Route):
    def __init__(self, data: dict):
        super().__init__()

    def set_attributes(self, data: dict):
        self.attributes = StaffDocumentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffDocumentRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffDocumentLinks(data)

    @staticmethod
    def get(id: int):
        return StaffDocument(
            self.engine.query(f"/v1/enrolments/staff-document/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffDocument(data) for data in self.engine.query("/v1/enrolments/staff-document", "GET", params=params)["data"]
        ]

class StaffDocumentCategoryAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffDocumentCategoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffDocumentCategory(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffDocumentCategoryAttributes(data)

    def set_links(self, data: dict):
        self.links = StaffDocumentCategoryLinks(data)

    @staticmethod
    def get(id: int):
        return StaffDocumentCategory(
            self.engine.query(f"/v1/enrolments/staff-document-category/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffDocumentCategory(data) for data in self.engine.query("/v1/enrolments/staff-document-category", "GET")["data"]
        ]

class StaffEmploymentAttributes(api.Attributes):
    __slots__ = [
        "role",
        "job_title",
        "employment_status",
        "employment_classification",
        "contract_commencement_date",
        "contract_expiry_date",
        "are_qualifications_provided",
        "is_w_w_c_c_completed",
        "w_w_c_c_number",
        "w_w_c_c_type",
        "w_w_c_c_status",
        "w_w_c_c_result_date",
        "w_w_c_c_expiry_date",
        "code_of_conduct_date_signed",
        "social_networking_policy_date_signed",
        "child_protection_policy_date_signed",
        "i_c_t_policy_date_signed",
        "first_aid_expiry_date",
        "resuscitation_expiry_date",
        "public_liability_expiry_date",
        "a_g_s_number",
        "position_number",
        "pay_rate",
        "employment_category",
        "teacher_registration_number",
        "username",
        "start_date",
        "end_date",
        "is_main_school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffEmploymentRelationships(api.Relationships):
    __slots__ = [
        "staff",
        "school",
        "campus_locations",
        "house"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffEmploymentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffEmployment(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffEmploymentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffEmploymentRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffEmploymentLinks(data)

    @staticmethod
    def get(id: int):
        return StaffEmployment(
            self.engine.query(f"/v1/enrolments/staff-employment/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffEmployment(data) for data in self.engine.query("/v1/enrolments/staff-employment", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StaffEmployment"):
        return StaffEmployment(
            self.engine.query("/v1/enrolments/staff-employment", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StaffEmployment"):
        return StaffEmployment(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class StaffLearningLogAttributes(api.Attributes):
    __slots__ = [
        "course_name",
        "course_type",
        "vendor",
        "focus",
        "key_learning_area",
        "hours",
        "cost",
        "is_funded_by_school",
        "start_date",
        "anticipated_end_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffLearningLogRelationships(api.Relationships):
    __slots__ = [
        "staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffLearningLogLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffLearningLog(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffLearningLogAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffLearningLogRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffLearningLogLinks(data)

    @staticmethod
    def get(id: int):
        return StaffLearningLog(
            self.engine.query(f"/v1/enrolments/staff-learning-log/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffLearningLog(data) for data in self.engine.query("/v1/enrolments/staff-learning-log", "GET", params=params)["data"]
        ]

class StaffQualificationAttributes(api.Attributes):
    __slots__ = [
        "qualification",
        "type",
        "from",
        "aitsl_teacher_accreditation_level",
        "next_aitsl_teacher_accreditation_level",
        "date_achieved",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffQualificationRelationships(api.Relationships):
    __slots__ = [
        "staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffQualificationLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StaffQualification(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StaffQualificationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StaffQualificationRelationships(data)

    def set_links(self, data: dict):
        self.links = StaffQualificationLinks(data)

    @staticmethod
    def get(id: int):
        return StaffQualification(
            self.engine.query(f"/v1/enrolments/staff-qualification/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StaffQualification(data) for data in self.engine.query("/v1/enrolments/staff-qualification", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StaffQualification"):
        return StaffQualification(
            self.engine.query("/v1/enrolments/staff-qualification", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StaffQualification"):
        return StaffQualification(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class StudentAttributes(api.Attributes):
    __slots__ = [
        "student_code",
        "barcode",
        "is_eligible_for_discount",
        "permission_to_photograph",
        "exam_number",
        "usi_id",
        "acara_id",
        "system_student_id",
        "username",
        "ref_id",
        "eal_stage",
        "eal_is_receiving_support",
        "eal_last_assessment_at",
        "is_subject_to_court_orders",
        "court_order_information",
        "student_first_language",
        "student_first_language_desc",
        "indigenous_status",
        "language_other_than_english_spoken_at_home",
        "student_mainly_speaks_english_at_home",
        "lote_background",
        "is_paying_international_fee",
        "cpsf_is_in_care",
        "cpsf_case_manager",
        "cpsf_district",
        "cpsf_contact_number",
        "created_at",
        "updated_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentRelationships(api.Relationships):
    __slots__ = [
        "primary_enrolment",
        "person",
        "activities",
        "activity_instances",
        "activity_links",
        "documents",
        "tenants",
        "flags",
        "flag_links",
        "awards",
        "award_links",
        "contacts",
        "holidays",
        "special_needs_program",
        "school_history",
        "households"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentLinks(api.Links):
    __slots__ = [
        "self",
        "primary_enrolment",
        "person",
        "activities",
        "activity_links",
        "photo",
        "documents",
        "tenants",
        "flags",
        "flag_links"
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
            self.engine.query(f"/v1/enrolments/student/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Student(data) for data in self.engine.query("/v1/enrolments/student", "GET", params=params)["data"]
        ]

    def patch(self, payload: "Student"):
        return Student(
            self.engine.query(self.links.self, "GET", payload=payload.data)
        )

    def get_absences(self, params: dict = None):
        return [
            attendance.Absence(data) for data in self.engine.query(self.links.self + "/absences", "GET", params=params)["data"]
        ]

    def get_reports(self, params: dict = None):
        return [
            reports.StudentAcademicReport(data) for data in self.engine.query(self.links.self + "/academic-reports", "GET", params=params)["data"]
        ]

    def get_activities(self, params: dict = None):
        return [
            activities.Activity(data) for data in self.engine.query(self.links.activities, "GET", params=params)["data"]
        ]

    def get_activity_links(self, params: dict = None):
        return [
            activities.ActivityLink(data) for data in self.engine.query(self.links.activity_links, "GET", params=params)["data"]
        ]

    def get_award_links(self, params: dict = None):
        return [
            welfare.StudentAwardLink(data) for data in self.engine.query(self.links.self + "/award-links", "GET", params=params)["data"]
        ]

    def get_awards(self, params: dict = None):
        return [
            welfare.Award(data) for data in self.engine.query(self.links.self + "/awards", "GET", params=params)["data"]
        ]

    def get_documents(self, params: dict = None):
        return [
            StudentDocument(data) for data in self.engine.query(self.links.documents, "GET", params=params)["data"]
        ]

    def get_edupro_reports(self, params: dict = None):
        return [
            edupro.StudentAcademicReport(data) for data in self.engine.query(self.links.self + "/edupro-academic-reports", "GET", params=params)["data"]
        ]

    def get_enrolments(self, params: dict = None):
        return [
            Enrolment(data) for data in self.engine.query(self.links.self + "/enrolments", "GET", params=params)["data"]
        ]

    def get_flag_links(self, params: dict = None):
        return [
            StudentFlagLinks(data) for data in self.engine.query(self.links.flag_links, "GET", params=params)["data"]
        ]

    def get_flags(self, params: dict = None):
        return [
            Flag(data)for data in self.engine.query(self.links.flags, "GET", params=params)["data"]
        ]

    def get_households(self, params: dict = None):
        return [
            StudentHousehold(data) for data in self.engine.query(self.links.self + "/households", "GET", params=params)["data"]
        ]

    def get_person(self, params: dict = None):
        return Person(
            self.engine.query(self.links.person, "GET", params=params)["data"]
        )

    def get_photo(self, params: dict = None) -> bytes:
        return self.engine.query(self.links.photo, "GET", params=params, raw=True)

    def get_primary_enrolment(self, params: dict = None):
        return Enrolment(
            self.engine.query(self.links.primary_enrolment, "GET", params=params)["data"]
        )

    def get_special_needs_programs(self, params: dict = None):
        return [
            SpecialNeedsProgram(data) for data in self.engine.query(self.links.self + "/special-needs-program")["data"]
        ]

    def tenants(self, params: dict = None):
        return [
            enterprise.Tenant(data) for data in self.engine.query(self.links.tenants, "GET", params=params)["data"]
        ]

    def get_timetable_lessons(self, params: dict = None):
        return [
            timetables.TimetableLesson(data) for data in self.engine.query(self.links.self + "/timetable-lessons")["data"]
        ]

class StudentContactAttributes(api.Attributes):
    __slots__ = [
        "student_id",
        "person_id",
        "priority",
        "is_authorised_pickup",
        "is_emergency_contact",
        "is_financially_responsible",
        "is_financially_responsible_for_activities",
        "fee_split_percentage",
        "is_primary_contact",
        "lives_with",
        "relation_type",
        "relation_name",
        "receives_mail",
        "receives_reports",
        "receves_portal_access",
        "portal_access_level",
        "is_custom_level",
        "receives_correspondence",
        "receives_absences",
        "do_not_contact"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentContactRelationships(api.Relationships):
    __slots__ = [
        "student",
        "student_person",
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentContactLinks(api.Links):
    __slots__ = [
        "self",
        "student",
        "portal_access_level"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentContact(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentContactAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentContactRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentContactLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return StudentContact(
            self.engine.query(f"/v1/enrolments/student-contact/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentContact(data) for data in self.engine.query("/v1/enrolments/student-contact", "GET", params=params)["data"]
        ]

    def get_student(self, params: dict = None):
        return Student(
            self.engine.query(self.links.student, "GET", params=params)["data"]
        )

    def patch(self, payload: "StudentContact"):
        return StudentContact(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class StudentDocumentAttributes(api.Attributes):
    __slots__ = [
        "file_name",
        "is_confidential"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentDocumentRelationships(api.Relationships):
    __slots__ = [
        "category"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentDocumentLinks(api.Links):
    __slots__ = [
        "self",
        "file"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentDocument(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentDocumentAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentDocumentRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentDocumentLinks(data)

    @staticmethod
    def get(id: int):
        return StudentDocument(
            self.engine.query(f"/v1/enrolments/student-document/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentDocument(data) for data in self.engine.query("/v1/enrolments/student-document", "GET", params=params)["data"]
        ]

    def delete(self):
        self.engine.query(self.links.self, "GET")

    def get_file(self):
        return self.engine.query(self.links.file, "GET", raw=True)

class StudentDocumentCategoryAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentDocumentCategoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentDocumentCategory(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentDocumentCategoryAttributes(data)

    def set_links(self, data: dict):
        self.links = StudentDocumentCategoryLinks(data)

    @staticmethod
    def get(id: int):
        return StudentDocumentCategory(
            self.engine.query(f"/v1/enrolments/student-document-category/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentDocumentCategory(data) for data in self.engine.query("/v1/enrolments/student-document-cateogry", "GET", params=params)["data"]
        ]

class StudentFlagLinksAttributes(api.Attributes):
    __slots__ = [
        "comment",
        "expiry_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentFlagLinksRelationships(api.Relationships):
    __slots__ = [
        "student",
        "flag"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentFlagLinksLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentFlagLinks(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentFlagLinksAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentFlagLinksRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentFlagLinksLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return StudentFlagLinks(
            self.engine.query(f"/v1/enrolments/student-flag-links/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentFlagLinks(data) for data in self.engine.query("/v1/enrolments/student-flag-links", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StudentFlagLinks"):
        return StudentFlagLinks(
            self.engine.query("/v1/enrolments/student-flag-links", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StudentFlagLinks"):
        return StudentFlagLinks(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

class StudentHouseholdAttributes(api.Attributes):
    __slots__ = [
        "student_id",
        "household_id",
        "residential_household"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentHouseholdRelationships(api.Relationships):
    __slots__ = [
        "student",
        "household"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentHouseholdLinks(api.Links):
    __slots__ = [
        "self",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentHousehold(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentHouseholdAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentHouseholdRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentHouseholdLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return StudentHousehold(
            self.engine.query(f"/v1/enrolments/student-household/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentHousehold(data) for data in self.engine.query("/v1/enrolments/student-household", "GET", params=params)["data"]
        ]

class StudentNccdRecordAttributes(api.Attributes):
    __slots__ = [
        "category",
        "category_code",
        "category_updated_at",
        "adjustment_level",
        "adjustment_level_code",
        "adjustment_level_updated_at",
        "education_type",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNccdRecordRelationships(api.Relationships):
    __slots__ = [
        "student",
        "school",
        "academic_period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNccdRecordLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNccdRecord(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentNccdRecordAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentNccdRecordRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentNccdRecordLinks(data)

    @staticmethod
    def get(id: int):
        return StudentNccdRecord(
            self.engine.query(f"/v1/enrolments/student-nccd-record/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentNccdRecord(data) for data in self.engine.query("/v1/enrolments/student-nccd-record", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StudentNccdRecord"):
        return StudentNccdRecord(
            self.engine.query("/v1/enrolments/student-nccd-record", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StudentNccdRecord"):
        return StudentNccdRecord(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )


    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class StudentNoteAttributes(api.Attributes):
    __slots__ = [
        "contents",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNoteRelationships(api.Relationships):
    __slots__ = [
        "student",
        "note_type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNoteLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentNote(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentNoteAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentNoteRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentNoteLinks(data)

    @staticmethod
    def get(id: int):
        return StudentNote(
            self.engine.query(f"/v1/enrolments/student-note/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentNote(data) for data in self.engine.query("/v1/enrolments/student-note", "GET", params=params)["data"]
        ]

class StudentSchoolHistoryAttributes(api.Attributes):
    __slots__ = [
        "previous_school",
        "destination_school",
        "start_date",
        "end_date",
        "country",
        "reason_for_change",
        "are_records_received",
        "is_expelled_or_suspended",
        "has_learning_disability"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolHistoryRelationships(api.Relationships):
    __slots__ = [
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolHistoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolHistory(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentSchoolHistoryAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentSchoolHistoryRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentSchoolHistoryLinks(data)

    @staticmethod
    def get(id: int):
        return StudentSchoolHistory(
            self.engine.query(f"/v1/enrolments/student-school-history/{id}", "GET")["data"]
        )

    def get_multiple(params: dict = None):
        return [
            StudentSchoolHistory(data) for data in self.engine.query("/v1/enrolments/student-school-history", "GET", params=params)["data"]
        ]

class StudentSchoolLinkAttributes(api.Attributes):
    __slots__ = [
        "enrolment_date",
        "exit_date",
        "expected_graduation_year",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolLinkRelationships(api.Relationships):
    __slots__ = [
        "student",
        "school",
        "entry_year_level",
        "exit_year_level"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolLinkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentSchoolLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentSchoolLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentSchoolLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentSchoolLinkLinks(data)

    @staticmethod
    def get(id: int):
        return StudentSchoolLink(
            self.engine.query(f"/v1/enrolments/student-school-link/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentSchoolLink(data) for data in self.engine.query("/v1/enrolments/student-school-link", "GET", params=params)["data"]
        ]

class StudentTransferAttributes(api.Attributes):
    __slots__ = [
        "reason_leaving",
        "enrolment_end_date",
        "handover_complete_date",
        "status"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentTransferRelationships(api.Relationships):
    __slots__ = [
        "student",
        "source_school",
        "destination_school",
        "year_level",
        "academic_period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentTransferLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentTransfer(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentTransferAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentTransferRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentTransferLinks(data)

    @staticmethod
    def get(id: int):
        return StudentTransfer(
            self.engine.query(f"/v1/enrolments/student-transfer/{id}", "GET")
        )

    @staticmethod
    def post(payload: "StudentTransfer"):
        return StudentTransfer(
            self.engine.query("/v1/enrolments/student-transfer", "POST", payload=payload.data)["data"]
        )

class VaccinationAttributes(api.Attributes):
    __slots__ = [
        "name",
        "has_certificate",
        "date_of_vaccination",
        "comment"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VaccinationRelationships(api.Relationships):
    __slots__ = [
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VaccinationLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Vaccination(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = VaccinationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = VaccinationRelationships(data)

    def set_links(self, data: dict):
        self.links = VaccinationLinks(data)

    @staticmethod
    def get(id: int, params: dict = None):
        return Vaccination(
            self.engine.query(f"/v1/enrolments/vaccination/{id}", "GET", params=params)["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Vaccination(data) for data in self.engine.query("/v1/enrolments/vaccination", "GET", params=params)["data"]
        ]

class YearLevelAttributes(api.Attributes):
    __slots__ = [
        "name",
        "code",
        "census_year",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class YearLevelRelationships(api.Relationships):
    __slots__ = [
        "school"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class YearLevelLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class YearLevel(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        super().__init__(data)

    def set_relationships(self, data: dict):
        super().__init__(data)

    def set_links(self, data: dict):
        super().__init__(data)

    @staticmethod
    def get(id: int):
        return YearLevel(
            self.engine.query(f"/v1/enrolments/year-level/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            YearLevel(data) for data in self.engine.query("/v1/enrolments/year-level", "GET", params=params)["data"]
        ]
