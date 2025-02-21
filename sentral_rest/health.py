from . import api
from . import enrolments

class MedicalCertificateAttributes(api.Attributes):
    __slots__ = [
        "description",
        "start_date",
        "end_date",
        "source"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalCertificateLinks(api.Links):
    __slots__ = [
        "self",
        "student",
        "attachments"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalCertificate(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = MedicalCertificateAttributes(data)

    def set_links(self, data: dict):
        self.links = MedicalCertificateLinks(data)

    def get(self, id: int):
        return MedicalCertificate(
            self.engine.query(f"/v1/health/medical-certificate/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            MedicalCertificate(data) for data in self.engine.query("/v1/health/medical-certificate", "GET", params=params)["data"]
        ]

    def post_attachment(self, payload: "MedicalCertificateAttachment"):
        return MedicalCertificate(
            self.engine.query(self.links.attachments, "POST", payload=payload.data)["data"]
        )

    def get_attachments(self, params: dict = None):
        return [
            MedicalCertificateAttachment(data) for data in self.engine.query(self.links.attachments, "GET", params=params)["data"]
        ]

    def get_student(self, params: dict = None):
        return enrolments.Student(
            self.engine.query(self.links.student, "GET", params=params)["data"]
        )

class MedicalCertificateAttachmentAttributes(api.Attributes):
    __slots__ = [
        "size",
        "file_name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalCertificateAttachmentLinks(api.Links):
    __slots__ = [
        "self",
        "file",
        "certificate"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class MedicalCertificateAttachment(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def get(self, id: int):
        return MedicalCertificateAttachment(
            self.engine.query(f"/v1/health/medical-certificate-attachment/{id}", "GET")["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

    def get_certificate(self):
        return MedicalCertificate(
            self.engine.query(self.links.certificate, "GET")["data"]
        )

    def get_file(self) -> bytes:
        return self.engine.query(self.links.file, "GET", raw=True)
