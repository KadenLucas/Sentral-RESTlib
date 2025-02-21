from . import api

class Sentral(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def deprovision_tentant(id: int):
        self.engine.query(f"/v1/sentral/deprovision-tenant/{id}", "DELETE")

    def provision_tenant(payload):
        return self.engine.query("/v1/sentral/provision-tenants", "POST", payload=payload.data)

    def revoke_key():
        self.engine.query("/v1/sentral/revoke-key", "DELETE")

class Schema(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def get(self, params: dict = None):
        return self.engine.query(
            "/v1/sentral/schema", "GET", params=params
        )

    def get_action_summary():
        return self.engine.query("/v1/sentral/schema/action-summary", "GET")

    def get_model_summary():
        return self.engine.query("/v1/sentral/schema/model-summary", "GET")

    def get_namespaces():
        return self.engine.query("/v1/sentral/schema/namespaces", "GET")

class Status(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def get(self, ):
        return self.engine.query("/v1/sentral/status", "GET")

class APIHealthAttributes(api.Attributes):
    __slots__ = [
        "webhooks",
        "server_time"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class APIHealthLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class APIHealth(api.Object):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = APIHealthAttributes(data)

    def set_links(self, data: dict):
        self.links = APIHealthLinks(data)
