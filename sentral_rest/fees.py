from . import api

class ConfigAttributes(api.Attributes):
    __slots__ = [
        "name",
        "value"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class ConfigLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Config(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = ConfigAttributes(data)

    def set_links(self, data: dict):
        self.links = ConfigLinks(data)

    @staticmethod
    def get(id: int):
        return Config(
            self.engine.query(f"/v1/fees/config/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Config(data) for data in self.engine.query("/v1/fees/config", "GET", params=params)["data"]
        ]

class DebtorAttributes(api.Attributes):
    __slots__ = [
        "debtor_type",
        "billing_identifier",
        "name",
        "email",
        "reference1",
        "reference2"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DebtorRelationships(api.Relationships):
    __slots__ = [
        "debtor_status",
        "donor_status",
        "invoives"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DebtorLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Debtor(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DebtorAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = DebtorRelationships(data)

    def set_links(self, data: dict):
        self.links = DebtorLinks(data)

    @staticmethod
    def get(id: int):
        return Debtor(
            self.engine.query(f"/v1/fees/debtor/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Debtor(data) for data in self.engine.query("/v1/fees/debtor", "GET", params=params)["data"]
        ]

    def get_invoices(self, params: dict = None):
        return [
            Invoice(data) for data in self.engine.query(self.links.self + "/invoices", "GET", params=params)["data"]
        ]

class DebtorStatusAttributes(api.Attributes):
    __slots__ = [
        "name",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DebtorStatusLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DebtorStatus(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DebtorStatusAttributes(data)

    def set_links(self, data: dict):
        self.links = DebtorStatusLinks(data)

    @staticmethod
    def get(id: int):
        return DebtorStatus(
            self.engine.query(f"/v1/fees/debtor-status/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            DebtorStatus(data) for data in self.engine.query("/v1/fees/debtor-status", "GET", params=params)["data"]
        ]

class DonorStatusAttributes(api.Attributes):
    __slots__ = [
        "name",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DonorStatusLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class DonorStatus(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = DonorStatusAttributes(data)

    def set_links(self, data: dict):
        self.links = DonorStatusLinks(data)

    @staticmethod
    def get(id: int):
        return DonorStatus(
            self.engine.query(f"/v1/fees/donor-status/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            DonorStatus(data) for data in self.engine.query("/v1/fees/donor-status", "GET", params=params)["data"]
        ]

class FeeStatusAttributes(api.Attributes):
    __slots__ = [
        "name",
        "type",
        "is_active"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FeeStatusLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class FeeStatus(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = FeeStatusAttributes(data)

    def set_links(self, data: dict):
        self.links = FeeStatusLinks(data)

    @staticmethod
    def get(id: int):
        return FeeStatus(
            self.engine.query(f"/v1/fees/fee-status/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            FeeStatus(data) for data in self.engine.query("/v1/fees/fee-status", "GET", params=params)["data"]
        ]

class InvoiceAttributes(api.Attributes):
    __slots__ = [
        "invoice_no",
        "amount_paid",
        "invoice_date",
        "due_date",
        "fully_paid_date"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InvoiceRelationships(api.Relationships):
    __slots__ = [
        "debtor",
        "status",
        "items"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InvoiceLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class Invoice(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InvoiceAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = InvoiceRelationships(data)

    def set_links(self, data: dict):
        self.links = InvoiceLinks(data)

    @staticmethod
    def get(id: int):
        return Invoice(
            self.engine.query(f"/v1/fees/invoice/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            Invoice(data) for data in self.engine.query("/v1/fees/invoice", "GET", params=params)["data"]
        ]

    def get_items(self, params: dict = None):
        return [
            InvoiceItem(data) for data in self.engine.query(self.links.self + "/items", "GET", params=params)["data"]
        ]

class InvoiceItemAttributes(api.Attributes):
    __slots__ = [
        "description",
        "quantity",
        "unit_amount",
        "tax_amount",
        "line_amount",
        "discount"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InvoiceItemRelationships(api.Relationships):
    __slots__ = [
        "invoice"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InvoiceItemLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class InvoiceItem(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = InvoiceItemAttributes(data)

    def set_relationships(self, data: dict):
        self.relationships = InvoiceItemRelationships(data)

    def set_links(self, data: dict):
        self.links = InvoiceItemLinks(data)

    @staticmethod
    def get(id: int):
        return InvoiceItem(
            self.engine.query(f"/v1/fees/invoice-item/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            InvoiceItem(data) for data in self.engine.query("/v1/fees/invoice-item", "GET", params=params)["data"]
        ]

class OnlineBillAttributes(api.Attributes):
    __slots__ = [
        "bill_date",
        "bill_due_date",
        "description",
        "unit_amount",
        "quantity",
        "tax_amount",
        "discount_amount",
        "total_amount",
        "total_amount_due",
        "total_amount_paid",
        "total_amount_credit",
        "fully_paid_on",
        "external_id",
        "status_name",
        "is_paid",
        "is_voided",
        "is_deleted",
        "created_at",
        "updated_at"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OnlineBillLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OnlineBill(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = OnlineBillAttributes(data)

    def set_links(self, data: dict):
        self.links = OnlineBillLinks(data)

    @staticmethod
    def get(id: int):
        return OnlineBill(
            self.engine.query(f"/v1/fees/online-bill/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            OnlineBill(data) for data in self.engine.query("/v1/fees/online-bill", "GET", params=params)["data"]
        ]

class OnlinePaymentAttributes(api.Attributes):
    __slots__ = [
        "name",
        "description",
        "date",
        "due_date",
        "buyer_country",
        "seller_country",
        "payment_method",
        "currency",
        "amount",
        "total_amount",
        "total_outstanding",
        "buyer_fees",
        "seller_fees",
        "credit_card_fee",
        "direct_debit_fee",
        "paypal_fee",
        "payment_providerr_fee",
        "refunded_amount",
        "is_reconciled",
        "status",
        "created_at",
        "updated_at",
        "external_source",
        "external_id"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OnlinePaymentLinks(api.Links):
    __slots__ = [
        "self"
    ]

    def __init__(self, data: dict):
        super().__init__(data)

class OnlinePayment(api.Route):
    def __init__(self, data: dict):
        super().__init__(data)

    def set_attributes(self, data: dict):
        self.attributes = OnlinePaymentAttributes(data)

    def set_links(self, data: dict):
        self.links = OnlinePaymentLinks(data)

    @staticmethod
    def get(id: int):
        return OnlinePayment(
            self.engine.query(f"/v1/fees/online-payment/{id}", "GET")["data"]
        )

    @staticmethod
    def get_multiple(params: dict = None):
        return [
            OnlinePayment(data) for data in self.engine.query("/v1/fees/online-payment", "GET", params=params)["data"]
        ]
