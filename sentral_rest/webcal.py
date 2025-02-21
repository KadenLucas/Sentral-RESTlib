from . import api

class WebcalCalendarAttributes(api.Attributes):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarRelationships(api.Relationships):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarLinks(api.Links):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendar(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = WebcalCalendarAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = WebcalCalendarRelationships(data)

    def set_links(self, data: dict):
        self.links = WebcalCalendarLinks(data)

class WebcalCalendarEventAttributes(api.Attributes):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarEventRelationships(api.Relationships):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarEventLinks(api.Links):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarEvent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = WebcalCalendarEventAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = WebcalCalendarEventRelationships(data)

    def set_links(self, data: dict):
        self.links = WebcalCalendarEventLinks(data)

class WebcalCalendarRecurringEventAttributes(api.Attributes):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarRecurringEventRelationships(api.Relationships):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarRecurringEventLinks(api.Links):
    __slots__ = [

    ]

    def __init__(self, data: dict):
        super().__init__(data)

class WebcalCalendarRecurringEvent(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = WebcalCalendarRecurringEventAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = WebcalCalendarRecurringEventRelationships(data)

    def set_links(self, data: dict):
        self.links = WebcalCalendarRecurringEventLinks(data)
