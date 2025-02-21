from . import enrolments
from . import portal
from . import api

class ActivityAttributes(api.Attributes):
    __slots__ = [
        "name",
        "report_name",
        "description",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "permission_form_due_date",
        "is_restricted_by_term",
        "is_restricted_by_year",
        "show_reports",
        "show_attendance",
        "show_portal",
        "self_registration",
        "approval_required",
        "maximum_places",
        "waiting_list_places",
        "archived",
        "risk_assessment",
        "registration_type",
        "portal_description",
        "available_terms",
        "available_years",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityRelationships(api.Relationships):
    __slots__ = [
        "cycles",
        "instances",
        "organisers",
        "venue",
        "category"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityLinks(api.Links):
    __slots__ = [
        "self",
        "cycles",
        "instances"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Activity(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityLinks(data)

    def get(self, id: int, params: dict = None):
        return Activity(
            self.engine.query(f"/v1/activities/activity/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            Activity(data) for data in self.engine.query("/v1/activities/activity", "GET", params=params)["data"]
        ]

    def get_cycles(self, params: dict = None):
        return [
            CycleInstance(data) for data in self.engine.query(self.links.cycles, "GET", params=params)["data"]
        ]

    def get_cycle_attendee_links(self, cycle_id: int, params: dict = None):
        return [
            AttendeeLink(data) for data in self.engine.query(self.links.cycles + f"/{cycle_id}/attendee-links", "GET", params=params)["data"]
        ]

    def get_instances(self, params: dict = None):
        return [
            ActivityInstance(data) for data in self.engine.query(self.links.instances, "GET", params=params)["data"]
        ]

    def get_sport_events(self, params: dict = None):
        return [
            ActivitySportEvent(data) for data in self.engine.query(self.links.self + "/sport-events", "GET", params=params)["data"]
        ]

class ActivityCategoryAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityCategoryLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(self, data)

class ActivityCategory(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityCategoryAttributes(data)

    def set_links(self, data: dict):
        self.links = ActivityCategoryLinks(data)

    def get(self, id: int):
        return ActivityCategory(
            self.engine.query(f"/v1/activities/activity-category/{id}", "GET")
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityCategory(data) for data in self.engine.query("/v1/activities/activity-category", "GET", params=params)["data"]
        ]

class ActivityGuardianLinkAttributes(api.Attributes):
    __slots__ = [
        "start_time",
        "end_time"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityGuardianLinkLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityGuardianLinkRelationships(api.Relationships):
    __slots__ = [
        "activity_instance",
        "staff",
        "person"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityGuardianLink(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityGuardianLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityGuardianLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityGuardianLinkLinks(data)

    def get(self, id: int):
        return ActivityGuardianLink(
            self.engine.query(f"/v1/activities/activity-guardian/{id}", "GET")
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityGuardianLink(data) for data in self.engine.query("/v1/activities/activity-guardian", "GET", params=params)["data"]
        ]

class ActivityInstanceAttributes(api.Attributes):
    __slots__ = [
        "status",
        "year",
        "name",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "is_published_to_portal",
        "is_payment_required",
        "is_permission_required",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityInstanceLinks(api.Links):
    __slots__ = [
        "self",
        "rolls"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityInstanceRelationships(api.Relationships):
    __slots__ = [
        "activity",
        "rolls"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityInstance(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityInstanceAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityInstanceRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityInstanceLinks(data)

    def get(self, id: int, params: dict = None):
        return ActivityInstance(
            self.engine.query(f"/v1/activities/activity-instance/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityInstance(data) for data in self.engine.query("/v1/activities/activity-instance", "GET", params=params)["data"]
        ]

    def get_attendee_links(self, params: dict = None):
        return [
            AttendeeLink(data) for data in self.engine.query(self.links.self + "/attendee-links", "GET", params=params)["data"]
        ]

    def post_activity_instance_attendee_link(self, payload: "AttendeeLink"):
        return AttendeeLink(
            self.engine.query(self.links.self + "/attendee-links", "POST", payload=payload.data)["data"]
        )

    def get_guardian_links(self, params: dict = None):
        return [
            ActivityGuardianLink(data) for data in self.engine.query(self.links.self + "/guardian-links", "GET", params=params)["data"]
        ]

    def get_responses(self, params: dict = None):
        return [
            portal.ActivityResponse(data) for data in self.engine.query(self.links.self + "/responses", "GET", params=params)["data"]
        ]

    def post_activity_response(self, payload: "portal.ActivityResponse"):
        return portal.ActivityResponse(
            self.engine.query(self.links.self + "/responses", "POST", payload=payload.data)["data"]
        )

    def get_rolls(self, params: dict = None):
        return Roll(
            self.engine.query(self.links.rolls, "GET", params=params)["data"]
        )

class ActivityPositionAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPositionRelationships(api.Relationships):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPositionLinks(api.Links):
    __slots__ = [
        "group"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPosition(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityPositionAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityPositionRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityPositionLinks(data)

    def get(self, id: int):
        return ActivityPosition(
            self.engine.query(f"/v1/activities/activity-position/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityPosition(data) for data in self.engine.query("/v1/activities/activity-position", "GET", params=params)["data"]
        ]

class ActivityPositionGroupAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPositionGroupRelationships(api.Relationships):
    __slots__ = [
        "positions"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPositionGroupLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityPositionGroup(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityPositionGroupAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityPositionGroupRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityPositionGroupLinks(data)

    def get(self, id: int):
        return ActivityPositionGroup(
            self.engine.query(f"/v1/activities/activity-position-group/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityPositionGroup(data) for data in self.engine.query("/v1/activities/activity-position-group", "GET", params=params)["data"]
        ]

    def get_positions(self, params: dict = None):
        return [
            ActivityPosition(data) for data in self.engine.query(self.links.self + "/positions", "GET", params=params)["data"]
        ]

class ActivitySportEventAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "is_whole_day",
        "place_type",
        "opposition",
        "players_type",
        "type",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivitySportEventRelationships(api.Relationships):
    __slots__ = [
        "activity",
        "venues",
        "grounds",
        "coaches",
        "vehicles",
        "teams",
        "transport_events"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivitySportEventLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivitySportEvent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivitySportEventAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivitySportEventRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivitySportEventLinks(data)

    def get(self, id: int, params: dict = None):
        return ActivitySportEvent(
            self.engine.query(f"/v1/activities/activity-sport-event/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivitySportEvent(data) for data in self.engine.query("/v1/activities/activity-sport-event", "GET", params=params)["data"]
        ]

    def get_coaches(self, params: dict = None):
        return [
            enrolments.Staff(data) for data in self.engine.query(self.links.self + "/coaches", "GET", params=params)["data"]
        ]

    def get_grounds(self, params: dict = None):
        return [
            VenueGrounds(data) for data in self.engine.query(self.links.self + "/grounds", "GET", params=params)["data"]
        ]

    def get_teams(self, params: dict = None):
        return [
            ActivityTeam(data) for data in self.engine.query(self.links.self + "/teams", "GET", params=params)["data"]
        ]

    def get_transport_events(self, params: dict = None):
        return [
            ActivityTransportEvent(data) for data in self.engine.query(self.links.self+ "/transport-events", "GET", params=params)["data"]
        ]

    def get_vehicles(self, params: dict = None):
        return [
            ActivityVehicle(data) for data in self.engine.query(self.links.self + "/vehicles", "GET", params=params)["data"]
        ]

    def get_venues(self, params: dict = None):
        return [
            Venue(data) for data in self.engine.query(self.links.self + "/venues", "GET", params=params)["data"]
        ]

class ActivityTeamAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeamRelationships(api.Relationships):
    __slots__ = [
        "activity",
        "coaches",
        "team_members",
        "team_member_positions"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeamLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeam(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityTeamAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityTeamRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityTeamLinks(data)

    def get(self, id: int, params: dict = None):
        return ActivityTeam(
            self.engine.query(f"/v1/activities/activity-team/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityTeam(data) for data in self.engine.query("/v1/activities/activity-team", "GET", params=params)["data"]
        ]

    def get_coaches(self, params: dict = None):
        return [
            enrolments.Staff(data) for data in self.engine.query(self.links.self + "/coaches", "GET", params=params)["data"]
        ]

    def get_members(self, params: dict = None):
        return [
            ActivityTeamMember(data) for data in self.engine.query(self.links.self + "/team-members", "GET", params=params)["data"]
        ]

class ActivityTeamMemberAttributes(api.Attributes):
    __slots__ = [
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeamMemberRelationships(api.Relationships):
    __slots__ = [
        "attendee_link",
        "team",
        "position",
        "cycle_instance",
        "student"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeamMemberLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTeamMember(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityTeamMemberAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityTeamMemberRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityTeamMemberLinks(data)

    def get(self, id: int):
        return ActivityTeamMember(
            self.engine.query(f"/v1/activities/activity-team-member/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityTeamMember(data) for data in self.engine.query("/v1/activities/activity-team-member", "GET", params=params)["data"]
        ]

class ActivityTransportEventAttributes(api.Attributes):
    __slots__ = [
        "date",
        "time",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTransportEventRelationships(api.Relationships):
    __slots__ = [
        "activity",
        "vehicle",
        "sport_event"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTransportEventLinks(api.Links):
    __slots__ = [
        "links"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityTransportEvent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityTransportEventAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityTransportEventRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityTransportEventLinks(data)

    def get(self, id: int):
        return ActivityTransportEvent(
            self.engine.query(f"/v1/activities/activity-transport-event/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityTransportEvent(data) for data in self.engine.query("/v1/activities/activity-transport-event", "GET", params=params)["data"]
        ]

class ActivityVehicleAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "use_date",
        "vehicle_identifier",
        "capacity",
        "type"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityVehicleRelationships(api.Relationships):
    __slots__ = [
        "activity",
        "transport_events"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityVehicleLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ActivityVehicle(api.Route):
    def __init__(self, data: dict):
        super().__ini__(data)

    def set_attributes(self, data: dict):
        self.attributes = ActivityVehicleAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = ActivityVehicleRelationships(data)

    def set_links(self, data: dict):
        self.links = ActivityVehicleLinks(data)

    def get(self, id: int):
        return ActivityVehicle(
            self.engine.query(f"/v1/activities/activity-vehicle/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            ActivityVehicle(data) for data in self.engine.query("/v1/activities/activity-vehicle", "GET", params=params)["data"]
        ]

class AttendeeLinkAttributes(api.Attributes):
    __slots__ = [
        "attendee_type",
        "show_in_reports",
        "points",
        "permission_given",
        "paid",
        "paid_amount"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AttendeeLinkRelationships(api.Relationships):
    __slots__ = [
        "student",
        "activity_instance",
        "activity",
        "cycle_instance"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AttendeeLinkLinks(api.Links):
    __slots__ = [
        "self",
        "enrolment_attendee"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class AttendeeLink(api.Route):
    def __init__(self, data: dict):
            super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = AttendeeLinkAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = AttendeeLinkRelationships(data)

    def set_links(self, data: dict):
        self.links = AttendeeLinkLinks(data)

    def get(self, id: int):
        return AttendeeLink(
            self.engine.query(f"/v1/activities/attendee-link/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            AttendeeLink(data) for data in self.engine.query("/v1/activities/attendee-link", "GET", params=params)["data"]
        ]

    def get_student(self, params: dict = None):
        return enrolments.Student(
            self.engine.query(self.links.enrolment_attendee, "GET", params=params)["data"]
        )

    def patch_attendee_link(self, payload: "AttendeeLink"):
        return AttendeeLink(
            self.engine.query(self.links.self, "PATCH", payload.data)["data"]
        )

class CycleInstanceAttributes(api.Attributes):
    __slots__ = [
        "name",
        "year",
        "cycle",
        "period"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CycleInstanceLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class CycleInstance(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = CycleInstanceAttributes(data)

    def set_links(self, data: dict):
        self.links = CycleInstanceLinks(data)

    def get(self, id: int):
        return CycleInstance(
            self.engine.query(f"/v1/activities/cycle-instance/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            CycleInstance(data) for data in self.engine.query("/v1/activities/cycle-instance", "GET", params=params)["data"]
        ]

class RollAttributes(api.Attributes):
    __slots__ = [
        "name",
        "roll_date",
        "is_submitted"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollRelationships(api.Relationships):
    __slots__ = [
        "activity_instance"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class RollLinks(api.Links):
    __slots__ = [
        "self",
        "activity_instance",
        "ui_mark_rolls"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Roll(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = RollAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = RollRelationships(data)

    def set_links(self, data: dict):
        self.links = RollLinks(data)

    def get(self, id: int):
        return Roll(
            self.engine.query(f"/v1/activities/roll/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            Roll(data) for data in self.engine.query("/v1/activities/roll", "GET", params=params)["data"]
        ]

    def get_activity_instance(self, params: dict = None):
        return ActivityInstance(
            self.engine.query(self.links.activity_instance, "GET", params=params)["data"]
        )

class VenueAttributes(api.Attributes):
    __slots__ = [
        "name",
        "address",
        "map_url"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueRelationships(api.Relationships):
    __slots__ = [
        "group",
        "grounds"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Venue(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = VenueAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = VenueRelationships(data)

    def set_links(self, data: dict):
        self.links = VenueLinks(data)

    def get(self, id: int, params: dict = None):
        return Venue(
            self.engine.query(f"/v1/activities/venue/{id}", "GET", params=params)["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            Venue(data) for data in self.engine.query("/v1/activities/venue", "GET", params=params)["data"]
        ]

    def get_grounds(self, params: dict = None):
        return [
            VenueGrounds(data) for data in self.engine.query(self.links.self + "/grounds", "GET", params=params)["data"]
        ]

class VenueGroundsAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGroundsRelationships(api.Relationships):
    __slots__ = [
        "venue"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGroundsLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGrounds(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = VenueGroundsAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = VenueGroundsRelationships(data)

    def set_links(self, data: dict):
        self.links = VenueGroundsLinks(data)

    def get(self, id: int):
        return VenueGrounds(
            self.engine.query(f"/v1/activities/venue-grounds/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            VenueGrounds(data) for data in self.engine.query("/v1/activities/venue-grounds", "GET", params=params)["data"]
        ]

class VenueGroupAttributes(api.Attributes):
    __slots__ = [
        "name"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGroupRelationships(api.Attributes):
    __slots__ = [
        "venues"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGroupLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class VenueGroup(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = VenueGroupAttributes(data)

    def get_relationships(self, data: dict):
        self.relationships = VenueGroupRelationships(data)

    def get_links(self, data: dict):
        self.links = VenueGroupLinks(data)

    def get(self, id: int):
        return VenueGroup(
            self.engine.query(f"/v1/activities/venue-group/{id}", "GET")["data"]
        )

    def get_multiple(self, params: dict = None):
        return [
            VenueGroup(data) for data in self.engine.query("/v1/activities/venue-group", "GET", params=params)["data"]
        ]

    def get_venues(self, params: dict = None):
        return [
            Venue(data) for data in self.engine.query(self.links.self + "/venues", "GET", params=params)["data"]
        ]
