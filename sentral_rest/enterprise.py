from . import api
from . import enrolments

class AdministrativeUserAttributes(api.Attributes):
    __slots__ = [
        "provider",
        "provider_id",
        "external_id",
        "guid",
        "username",
        "title",
        "first_name",
        "last_name",
        "email",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AdministrativeUserRelationships(api.Relationships):
    __slots__ = [
        "staff"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AdministrativeUserLinks(api.Links):
    __slots__ = [
        "links"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AdministrativeUser(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AdministrativeUserAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AdministrativeUserRelationships(data)

    def set_links(self, data: dict):
        self.links = AdministrativeUserLinks(data)

    def get(self, id: int):
        return AdministrativeUser(
            self.engine.query(f"/v1/enterprise/administrative-user/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            AdministrativeUser(data) for data in self.engine.query("/v1/enterprise/administrative-user", "GET", params=params)["data"]
        ]

class EnterpriseTermAttributes(api.Attributes):
    __slots__ = [
        "region",
        "year",
        "term",
        "start_date",
        "end_date",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnterpriseTermLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class EnterpriseTerm(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = EnterpriseTermAttributes(data)

    def set_links(self, data: dict):
        self.links = EnterpriseTermLinks(data)

    def get(self, id: int):
        return EnterpriseTerm(
            self.engine.query(f"/v1/enterprise/enterprise-term/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            EnterpriseTerm(data) for data in  self.engine.query("/v1/enterprise/enterprise-term", "GET", params=params)["data"]
        ]

class PortalAccessLevelAttributes(api.Attributes):
    __slots__ = [
        "name",
        "level",
        "is_default"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PortalAccessLevel(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PortalAccessLevelAttributes(data)

    def get(self, id: int):
        return PortalAccessLevel(
            self.engine.query(f"/v1/enterprise/portal-access-level/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            PortalAccessLevel(data) for data in self.engine.query("/v1/enterprise/portal-access-level", "GET", params=params)["data"]
        ]

class PortalUserAttributes(api.Attributes):
    __slots__ = [
        "provider",
        "provider_id",
        "username",
        "user_type",
        "guid",
        "title",
        "first_name",
        "surname",
        "email",
        "phone",
        "address",
        "mobile",
        "legal_first_name",
        "legal_surname",
        "legal_email",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PortalUserLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class PortalUser(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = PortalUserAttributes(data)

    def set_links(self, data: dict):
        self.links = PortalUserLinks(data)

    def get(self, id: int):
        return PortalUser(
            self.engine.query(f"/v1/enterprise/portal-user/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            PortalUser(data) for data in self.engine.query("/v1/enterprise/portal-user", "GET", params=params)["data"]
        ]

class TenantAttributes(api.Attributes):
    __slots__ = [
        "name",
        "code",
        "region",
        "key",
        "timezone",
        "provisioning_status",
        "provisioning_completed_at",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TenantRelationships(api.Relationships):
    __slots__ = [
        "schools",
        "term_dates"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class TenantLinks(api.Links):
    __slots__ = [
        "self",
        "schools"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Tenant(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = TenantAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = TenantRelationships(data)

    def set_links(self, data: dict):
        self.links = TenantLinks(data)

    def get(self, id: int, params: dict = None):
        return Tenant(
            self.engine.query(f"/v1/enterprise/tenant/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            Tenant(data) for data in self.engine.query("/v1/enterprise/tenant", "GET", params=params)["data"]
        ]

    def patch(self, payload: "Tenant"):
        return Tenant(
            self.engine.query(self.links.self, "GET", payload=payload.data)
        )

    def get_schools(self, params: dict = None):
        return [
            enrolments.School(data) for data in self.engine.query(self.links.schools, "GET", params=params)["data"]
        ]

    def get_enterprise_terms(self):
        return [
            EnterpriseTerm(data) for data in self.engine.query(self.links.self + "/term-dates", "GET")["data"]
        ]

class UserCalendarAttributes(api.Attributes):
    __slots__ = [
        "calendar_name",
        "external_source",
        "external_id",
        "ref_id",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendarRelationships(api.Relationships):
    __slots__ = [
        "owner",
        "portal_owner"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendarLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendar(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = UserCalendarAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = UserCalendarRelationships(data)

    def set_links(self, data: dict):
        self.links = UserCalendarLinks(data)

    def get(self, id: int):
        return UserCalendar(
            self.engine.query(f"/v1/enterprise/user-calendar/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            UserCalendar(data) for data in  self.engine.query("/v1/enterprise/user-calendar", "GET", params=params)["data"]
        ]

    def post(payload: "UserCalendar"):
        return UserCalendar(
            self.engine.query("/v1/enterprise/user-calendar", "POST", payload=payload.data)["data"]
        )

    def post_event(self, event_id: int):
        self.engine.query(self.links.self + "/event/{event_id}", "POST")

    def delete_event(self, event_id: int):
        self.engine.query(self.links.self + "/event/{event_id}")

    def patch(self, payload: "UserCalendar"):
        return UserCalendar(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")

class UserCalendarEventAttributes(api.Attributes):
    __slots__ = [
        "title",
        "description",
        "event_type",
        "record_type",
        "record_subtype",
        "location",
        "timezone",
        "starts_at",
        "ends_at",
        "created_at",
        "updates_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendarEventRelationships(api.Relationships):
    __slots__ = [
        "tenant",
        "creator"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendarEventLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class UserCalendarEvent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = UserCalendarEventAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = UserCalendarEventRelationships(data)

    def set_links(self, data: dict):
        self.links = UserCalendarEventLinks(data)

    def get(self, id: int):
        return UserCalendarEvent(
            self.engine.query(f"/v1/enterprise/user-calendar-event/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            UserCalendarEvent(data) for data in self.engine.query("/v1/enterprise/user-calendar-event", "GET", params=params)["data"]
        ]

    def post(payload: "UserCalendarEvent"):
        return UserCalendarEvent(
            self.engine.query("/v1/enterprise/user-calendar-event", "POST", payload=payload.data)["data"]
        )

    def patch(self, payload: "UserCalendarEvent"):
        return UserCalendarEvent(
            self.engine.query(self.links.self, "PATCH", payload=payload.data)["data"]
        )

    def delete(self):
        self.engine.query(self.links.self, "DELETE")
