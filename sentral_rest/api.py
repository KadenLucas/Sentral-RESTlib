from urllib.parse import urlencode
from requests import Session
from . import utils
import json

class Engine:
    url = None
    session = None
    instance = None

    def __new__(cls, config_path: str):
        if cls.instance is None:
            cls.instance = super(Engine, cls).__new__(cls, config_path)
            cls.instance.init(config_path)

        return cls.instance

    @classmethod
    def init(cls, config_path: str):
        cls.session = Session()
        config = json.load(open(config_path, 'r'))

        cls.url = config.get("sentral_url")
        cls.session.headers.update(
            {
                "X-API-KEY": config.get("api_key"),
                "X-API-TENANT": config.get("tenant_code")
            }
        )

    @classmethod
    def query(cls, endpoint: str, method: str, payload: dict | None = None, params: dict = None, raw: bool = False):
        response = None

        match method:
            case "GET" | "get":
                response = cls.session.get(cls.url + endpoint, data=urlencode(payload) if payload else None, params=params)

            case "POST" | "post":
                response = cls.session.post(cls.url + endpoint, data=urlencode(payload)if payload else None, params=params)

            case "PATCH" | "patch":
                raise ValueError("PATCH method not yet implemented.")

            case "DELETE" | "delete":
                raise ValueError("DELETE method not yet implemented.")

        if response is None:
            raise ValueError("Unknown method.")

        if response.status_code not in [200, 204]:
            raise ValueError(response.text)

        if raw:
            return response.content

        try:
            data = json.loads(response.content)
        except json.decoder.JSONDecodeError:
            data = dict()

        return data

class Attributes:
    __slots__ = []

    def __init__(self, data: dict):
        if data is None:
            return

        for key in self.__slots__:
            attr = utils.camel_string(key)
            setattr(self, key, utils.type_check_string(data.get(attr)))

    def __repr__(self):
        return "<Attributes({})>".format(
            ', '.join(f"{slot}={repr(getattr(self, slot))}" for slot in self.__slots__ if hasattr(self, slot))
        )

class Relationships:
    __slots__ = []

    def __init__(self, data: dict):
        if data is None:
            return

        for key in self.__slots__:
            attr = utils.camel_string(key)
            setattr(self, key, data.get(attr))

    def __repr__(self):
        return "<Relationships({})>".format(
            ', '.join(f"{slot}={repr(getattr(self, slot))}" for slot in self.__slots__ if hasattr(self, slot))
        )

class Links:
    __slots__ = []

    def __init__(self, data: dict):
        if data is None:
            return

        for key in self.__slots__:
            attr = utils.camel_string(key)
            setattr(self, key, data.get(attr))

    def __repr__(self):
        return "<Links({})>".format(
            ', '.join(f"{slot}={repr(getattr(self, slot))}" for slot in self.__slots__ if hasattr(self, slot))
        )

class Route:
    __slots__ = [
        "id",
        "data",
        "type",
        "links",
        "attributes",
        "relationships"
    ]

    def __init__(self, data: dict, engine: Engine):
        self.data = {"data": data}
        self.engine = engine
        self.id = data.get("id")
        self.type = data.get("type")
        self.set_links(data.get("links"))
        self.set_attributes(data.get("attributes"))
        self.set_relationships(data.get("relationships"))

        self.data = data

    def set_links(self, data: dict): ...
    def set_attributes(self, data: dict): ...
    def set_relationships(self, data: dict): ...

    def __repr__(self):
        return "<{}({})>".format(
            self.__class__.__name__,
        ', '.join(f"{slot}={repr(getattr(self, slot))}" for slot in self.__slots__ if hasattr(self, slot) and (slot != "data"))
        )

class Object(Route):
    def __init__(self, data: dict, engine: Engine):
        super().__init__(data, engine)
