from . import api
from . import enrolments

class ActivityResponse(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    @staticmethod
    def get(id: int):
        return ActivityResponse(
            self.engine.query(f"/v1/activities/activity-response/{id}", "GET")["data"]
        )

    def patch(self, payload: "ActivityResponse"):
        return ActivityResponse(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class FamilyChangeRequestAttributes(api.Attributes):
    __slots__ = [
        "external_id",
        "is_pending",
        "is_completed",
        "is_rejected",
        "date_actioned"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FamilyChangeRequestRelationships(api.Relationships):
    __slots__ = [
        "affected_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FamilyChangeRequestLinks(api.Links):
    __slots__ = [
        "self",
        "details"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FamilyChangeRequest(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FamilyChangeRequestAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = FamilyChangeRequestRelationships(data)

    def set_links(self, data: dict):
        self.links = FamilyChangeRequestLinks(data)

    @staticmethod
    def get(id: int):
        return FamilyChangeRequest(
            self.engine.query(f"/v1/portal/family-change-request/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            FamilyChangeRequest(data) for data in self.engine.query("/v1/portal/family-change-request", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "FamilyChangeRequest"):
        return FamilyChangeRequest(
            self.engine.query("/v1/portal/family-change-request", "GET", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def get_details(self, params: dict = None):
        return [
            FamilyChangeRequestDetail(data) for data in self.engine.query(self.links.details, "GET", params=params)["data"]
        ]

    def post_detail(self, payload: "FamilyChangeRequestDetail"):
        return FamilyChangeRequestDetail(
            self.engine.query(self.links.details, "POST", payload=payload.data)["data"]
        )

    def patch_details(self, detail_id: int, payload: "FamilyChangeRequestDetail"):
        return FamilyChangeRequestDetail(
            self.engine.query(self.links.details + f"/{detail_id}", "PATCH", payload=payload.data)["data"]
        )

    def get_detail(self, detail_id: int):
        return FamilyChangeRequestDetail(
            self.engine.query(self.links.details + f"/{detail_id}", "GET")["data"]
        )

    def delete_detail(self, detail_id: int):
        self.engine.query(self.links.details + f"/{detail_id}", "DELETE")

class FamilyChangeRequestDetailAttributes(api.Attributes):
    __slots__ = [
        "object_type",
        "object_id",
        "sub_object_type",
        "sub_object_id",
        "field",
        "value",
        "is_delete_operation"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FamilyChangeRequestDetailLinks(api.Links):
    __slots__ = [
        "self",
        "family_change_request"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FamilyChangeRequestDetail(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FamilyChangeRequestDetailAttributes(data)

    def set_links(self, data: dict):
        self.links = FamilyChangeRequestDetailLinks(data)

class MedicalChangeConditionRelationships(api.Relationships):
    __slots__ = [
        "change_request"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionLinks(api.Links):
    __slots__ = [
        "self",
        "care_plan_file",
        "doctors_letter_file"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeCondition(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    @staticmethod
    def match(data: dict):
        match data.get("type"):
            case "medicalChangeConditionAdd":
                return MedicalChangeConditionAdd(data)

            case "medicalChangeConditionAllergy":
                return MedicalChangeConditionAllergy(data)

            case "medicalChangeConditionAsthma":
                return MedicalChangeConditionAsthma(data)

            case "medicalChangeConditionDiabetes":
                return MedicalChangeConditionDiabetes(data)

            case "medicalChangeConditionEpilepsy":
                return MedicalChangeConditionEpilepsy(data)

            case "medicalChangeConditionOther":
                return MedicalChangeConditionOther(data)

    @staticmethod
    def get(id: int):
        for data in self.engine.query(f"/v1/portal/medical-change-condition/{id}", "GET")["oneOf"]:
            return MedicalChangeCondition.match(data["data"])

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalChangeCondition.match(data) for data in self.engine.query("/v1/portal/medical-change-condition", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload):
        return MedicalChangeCondition.match(
            self.engine.query("/v1/portal/medical-change-condition", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload):
        return MedicalChangeCondition.match(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def post_care_plan_file(self, file: bytes):
        # Upload a file via multipart/form-data?
        pass

    def get_care_plan_file(self) -> bytes:
        return self.engine.query(self.links.care_plan_file, "GET", raw=True)

    def post_doctors_letter_file(self, file: bytes):
        # Upload a file via multipart/form-data?
        pass

    def get_doctors_letter_file(self) -> bytes:
        return self.engine.query(self.links.doctors_letter_file, "GET", raw=True)

class MedicalChangeConditionAddAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "severity",
        "additional_information",
        "is_inattentive",
        "is_hyperactive",
        "is_medication_required",
        "is_doctors_letter_provided",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionAdd(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionAddAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionAllergyAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "additional_information",
        "has_care_plan_provided",
        "allergy_name",
        "severity",
        "is_prescribed_antihistamine",
        "is_prescribed_epi_pen",
        "has_epi_pen_registered",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionAllergy(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionAllergyAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionAsthmaAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "additional_information",
        "severity",
        "is_prescribed_salbutamol",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionAsthma(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionAsthmaAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionDiabetesAttributes(api.Attributes):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "has_insulin_injections",
        "has_insulin_pump",
        "has_glucagon",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionDiabetes(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionDiabetesAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionDietaryAttributes(api.Attributes):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "dietary_name",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionDietary(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionDietaryAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionEpilepsyAttributes(api.Attributes):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "type",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionEpilepsy(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionEpilepsyAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionOtherAttributes(api.Attributes):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionOther(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionOtherAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeConditionPhobiaAttributes(api.Attributes, MedicalChangeCondition):
    __slots__ = [
        "name",
        "severity",
        "details",
        "additional_information",
        "has_care_plan_provided",
        "phobia_name",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeConditionPhobia(MedicalChangeCondition, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeConditionPhobiaAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeConditionRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeConditionLinks(data)

class MedicalChangeDisability(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = None

    def set_relationships(self, data: dict):
        self.relationships = None

    def set_links(self, data: dict):
        self.links = None

    @staticmethod
    def get(id: int):
        for data in self.engine.query(f"/v1/portal/medical-change-disability/{id}", "GET")["oneOf"]:
            return MedicalChangeDisabilityOther(data["data"])

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalChangeDisabilityOther(data) for data in self.engine.query("/v1/portal/medical-change-disability", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "MedicalChangeDisabilityOther"):
        return MedicalChangeDisabilityOther(
            self.engine.query("/v1/portal/medical-change-disability", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "MedicalChangeDisabilityOther"):
        return MedicalChangeDisabilityOther(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def post_care_plan_file(self, payload: bytes):
        # Upload a file via multipart/form-data?
        pass

    def get_care_plan_file(self) -> bytes:
        return self.engine.query(self.links.care_plan_file, "GET", raw=True)

class MedicalChangeDisabilityOtherAttributes(api.Attributes):
    __slots__ = [
        "name",
        "details",
        "receives_funding",
        "has_care_plan_provided",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeDisabilityOtherRelationships(api.Relationships):
    __slots__ = [
        "change_request"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeDisabilityOtherLinks(api.Links):
    __slots__ = [
        "self",
        "care_plan_file"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeDisabilityOther(MedicalChangeDisability, api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeDisabilityOtherAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeDisabilityOtherRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeDisabilityOtherLinks(data)

class MedicalChangePrescribedMedicationAttributes(api.Attributes):
    __slots__ = [
        "name",
        "dosage",
        "type",
        "details",
        "is_prescribed",
        "is_taken_at_school",
        "is_long_term",
        "anticipated_stop_date",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangePrescribedMedicationRelationships(api.Relationships):
    __slots__ = [
        "change_request",
        "enrolment_prescribed_medication",
        "enrolment_condition"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangePrescribedMedicationLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangePrescribedMedication(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangePrescribedMedicationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangePrescribedMedicationRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangePrescribedMedicationLinks(data)

    @staticmethod
    def get(id: int):
        return MedicalChangePrescribedMedication(
            self.engine.query(f"/v1/portal/medical-change-prescribed-medication/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalChangePrescribedMedication(data) for data in self.engine.query("/v1/portal/medical-change-prescribed-medication", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "MedicalChangePrescribedMedication"):
        return MedicalChangePrescribedMedication(
            self.engine.query("/v1/portal/medical-change-prescribed-medication", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "MedicalChangePrescribedMedication"):
        return MedicalChangePrescribedMedication(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class MedicalChangeDoctorAttributes(api.Attributes):
    __slots__ = [
        "type",
        "name",
        "practice_name",
        "phone",
        "address",
        "consent_to_contact",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeDoctorRelationships(api.Relationships):
    __slots__ = [
        "affected_doctor"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeDoctor(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeDoctorAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeDoctorRelationships(data)

class MedicalChangeVaccinationAttributes(api.Attributes):
    __slots__ = [
        "name",
        "date_of_vaccination",
        "comment",
        "is_marked_for_deletion"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeVaccinationRelationships(api.Relationships):
    __slots__ = [
        "enrolment_vaccination"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeVaccination(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeVaccinationAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeVaccinationRelationships(data)

class MedicalChangeMiscAttributes(api.Attributes):
    __slots__ = [
        "was_medication_advice_form_received",
        "can_over_counter_salbutamol",
        "can_over_counter_paracetamol",
        "can_over_counter_ibuprofen",
        "can_over_counter_antihistamine",
        "has_parent_acknowledged",
        "has_long_term_medication",
        "are_vaccinations_up_to_date",
        "has_measles_exclusion",
        "last_date_of_tetanus_injection",
        "private_medical_fund_expiry_date",
        "medicare_expiry_date",
        "ambulance_cover_provider",
        "medicare_number",
        "medicare_position_on_card",
        "private_medical_fund",
        "private_medical_fund_number",
        "health_care_card_number",
        "has_ambulance_cover",
        "has_private_hosptial_cover"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeMisc(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeMiscAttributes(data)

class MedicalChangeRequestAttributes(api.Attributes):
    __slots__ = [
        "is_approved",
        "is_rejected",
        "date_submitted",
        "date_actioned"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeRequestRelationships(api.Relationships):
    __slots__ = [
        "enrolment_student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeRequestLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalChangeRequest(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalChangeRequestAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = MedicalChangeRequestRelationships(data)

    def set_links(self, data: dict):
        self.links = MedicalChangeRequestLinks(data)

    @staticmethod
    def match(data: dict):
        type_ = data.get("type")

        match type_:
            case "medicalChangeRequest":
                return MedicalChangeRequest(data)

            case "medicalChangeDoctor":
                return MedicalChangeDoctor(data)

            case "medicalChangeVaccination":
                return MedicalChangeVaccination(data)

            case "medicalChangeMisc":
                return MedicalChangeMisc(data)

        if type_.startswith("medicalChangeCondition"):
            return MedicalChangeCondition.match(data)

    @staticmethod
    def get(id: int):
        return MedicalChangeRequest(
            self.engine.query(f"/v1/portal/medical-change-request/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            MedicalChangeRequest(data) for data in self.engine.query("/v1/portal/medical-change-request", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload):
        return MedicalChangeRequest.match(
            self.engine.query("/v1/portal/medical-change-request", "POST", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def post_vaccination_certificate_file(self, file: bytes):
        # Upload a file via multipart/form-data?
        pass

    def get_condition(self, id: int, type_: str):
        match type_:
            case "add":
                return MedicalChangeConditionAdd(
                    self.engine.query(self.link.self + f"condition-add/{id}", "GET")["data"]
                )

            case "allergy":
                return MedicalChangeConditionAllergy(
                    self.engine.query(self.link.self + f"condition-allergy/{id}", "GET")["data"]
                )

            case "asthma":
                return MedicalChangeConditionAsthma(
                    self.engine.query(self.link.self + f"condition-asthma/{id}", "GET")["data"]
                )

            case "diabetes":
                return MedicalChangeConditionDiabetes(
                    self.engine.query(self.link.self + f"condition-diabetes/{id}", "GET")["data"]
                )

            case "epilepsy":
                return MedicalChangeConditionEpilepsy(
                    self.engine.query(self.link.self + f"condition-epilepsy/{id}", "GET")["data"]
                )

            case "other":
                return MedicalChangeConditionOther(
                    self.engine.query(self.link.self + f"condition-other/{id}", "GET")["data"]
                )

    def get_conditions(self, type_: str):
        match type_:
            case "add":
                return MedicalChangeConditionAdd(
                    self.engine.query(self.link.self + "condition-add", "GET")["data"]
                )

            case "allergy":
                return MedicalChangeConditionAllergy(
                    self.engine.query(self.link.self + "condition-allergy", "GET")["data"]
                )

            case "asthma":
                return MedicalChangeConditionAsthma(
                    self.engine.query(self.link.self + "condition-asthma", "GET")["data"]
                )

            case "diabetes":
                return MedicalChangeConditionDiabetes(
                    self.engine.query(self.link.self + "condition-diabetes", "GET")["data"]
                )

            case "epilepsy":
                return MedicalChangeConditionEpilepsy(
                    self.engine.query(self.link.self + "condition-epilepsy", "GET")["data"]
                )

            case "other":
                return MedicalChangeConditionOther(
                    self.engine.query(self.link.self + "condition-other", "GET")["data"]
                )

    def post_condition(self, payload, type_: str):
        match type_:
            case "add":
                return MedicalChangeConditionAdd(
                    self.engine.query(self.link.self + "condition-add", "POST", payload=payload.dict)["data"]
                )

            case "allergy":
                return MedicalChangeConditionAllergy(
                    self.engine.query(self.link.self + "condition-allergy", "POST", payload=payload.dict)["data"]
                )

            case "asthma":
                return MedicalChangeConditionAsthma(
                    self.engine.query(self.link.self + "condition-asthma", "POST", payload=payload.dict)["data"]
                )

            case "diabetes":
                return MedicalChangeConditionDiabetes(
                    self.engine.query(self.link.self + "condition-diabetes", "POST", payload=payload.dict)["data"]
                )

            case "epilepsy":
                return MedicalChangeConditionEpilepsy(
                    self.engine.query(self.link.self + "condition-epilepsy", "POST", payload=payload.dict)["data"]
                )

            case "other":
                return MedicalChangeConditionOther(
                    self.engine.query(self.link.self + "condition-other", "POST", payload=payload.dict)["data"]
                )

    def patch_condition(self, payload, id: int, type_: str):
        match type_:
            case "add":
                return MedicalChangeConditionAdd(
                    self.engine.query(self.link.self + f"condition-add/{id}", "PATCH", payload=payload.dict)["data"]
                )

            case "allergy":
                return MedicalChangeConditionAllergy(
                    self.engine.query(self.link.self + f"condition-allergy/{id}", "PATCH", payload=payload.dict)["data"]
                )

            case "asthma":
                return MedicalChangeConditionAsthma(
                    self.engine.query(self.link.self + f"condition-asthma/{id}", "PATCH", payload=payload.dict)["data"]
                )

            case "diabetes":
                return MedicalChangeConditionDiabetes(
                    self.engine.query(self.link.self + f"condition-diabetes/{id}", "PATCH", payload=payload.dict)["data"]
                )

            case "epilepsy":
                return MedicalChangeConditionEpilepsy(
                    self.engine.query(self.link.self + f"condition-epilepsy/{id}", "PATCH", payload=payload.dict)["data"]
                )

            case "other":
                return MedicalChangeConditionOther(
                    self.engine.query(self.link.self + f"condition-other/{id}", "PATCH", payload=payload.dict)["data"]
                )

    def delete_condition(self, id: int, type_: str):
        match type_:
            case "add":
                return MedicalChangeConditionAdd(
                    self.engine.query(self.link.self + f"condition-add/{id}", "DELETE")["data"]
                )

            case "allergy":
                return MedicalChangeConditionAllergy(
                    self.engine.query(self.link.self + f"condition-allergy/{id}", "DELETE")["data"]
                )

            case "asthma":
                return MedicalChangeConditionAsthma(
                    self.engine.query(self.link.self + f"condition-asthma/{id}", "DELETE")["data"]
                )

            case "diabetes":
                return MedicalChangeConditionDiabetes(
                    self.engine.query(self.link.self + f"condition-diabetes/{id}", "DELETE")["data"]
                )

            case "epilepsy":
                return MedicalChangeConditionEpilepsy(
                    self.engine.query(self.link.self + f"condition-epilepsy/{id}", "DELETE")["data"]
                )

            case "other":
                return MedicalChangeConditionOther(
                    self.engine.query(self.link.self + f"condition-other/{id}", "DELETE")["data"]
                )

    def get_condition_care_plan_file(self, id: int, type_: str) -> bytes:
        match type_:
            case "add":
                return self.engine.query(self.link.self + f"condition-add/{id}/care-plan-file", "GET", raw=True)

            case "allergy":
                return self.engine.query(self.link.self + f"condition-allergy/{id}/care-plan-file", "GET", raw=True)

            case "asthma":
                return self.engine.query(self.link.self + f"condition-asthma/{id}/care-plan-file", "GET", raw=True)

            case "diabetes":
                return self.engine.query(self.link.self + f"condition-diabetes/{id}/care-plan-file", "GET", raw=True)

            case "epilepsy":
                return self.engine.query(self.link.self + f"condition-epilepsy/{id}/care-plan-file", "GET", raw=True)

            case "other":
                return self.engine.query(self.link.self + f"condition-other/{id}/care-plan-file", "GET", raw=True)

    def post_care_plan_file(self, file: bytes, id: int, type_: str):
        match type_:
            case "add":
                # Upload a file via multipart/form-data?
                pass

            case "allergy":
                # Upload a file via multipart/form-data?
                pass

            case "asthma":
                # Upload a file via multipart/form-data?
                pass

            case "diabetes":
                # Upload a file via multipart/form-data?
                pass

            case "epilepsy":
                # Upload a file via multipart/form-data?
                pass

            case "other":
                # Upload a file via multipart/form-data?
                pass

    def get_doctor(self, id: int):
        return MedicalChangeDoctor(
            self.engine.query(self.links.self + f"/doctor/{id}", "GET")["data"]
        )

    def get_doctors(self):
        return [
            MedicalChangeDoctor(data) for data in self.engine.query(self.links.self + "/doctor", "GET")["data"]
        ]

class StudentEnrolmentDraftAttributes(api.Attributes):
    __slots__ = [
        "status",
        "created_at",
        "data",
        "original_data"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentEnrolmentDraftRelationships(api.Relationships):
    __slots__ = [
        "student",
        "created_by"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentEnrolmentDraftLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class StudentEnrolmentDraft(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = StudentEnrolmentDraftAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = StudentEnrolmentDraftRelationships(data)

    def set_links(self, data: dict):
        self.links = StudentEnrolmentDraftLinks(data)

    @staticmethod
    def get(id: int):
        return StudentEnrolmentDraft(
            self.engine.query(f"/v1/portal/student-enrolment-draft/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            StudentEnrolmentDraft(data) for data in self.engine.query("/v1/portal/student-enrolment-draft", "GET", params=params)["data"]
        ]

    @staticmethod
    def post(payload: "StudentEnrolmentDraft"):
        return StudentEnrolmentDraft(
            self.engine.query("/v1/portal/student-enrolment-draft", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "StudentEnrolmentDraft"):
        return StudentEnrolmentDraft(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")


    def get_attachments(self):
        return [
            enrolments.StudentDocument(data) for data in self.engine.query(self.links.self + "/attachment", "GET")["data"]
        ]

    def post_attachment(self, attachment: bytes, params: dict = None):
        # Upload via "multipart/form-data" under key "attachment"
        pass
