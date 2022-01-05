from pyactus.domain import ContractAttributeSet
from pyactus.domain import ContractRole
from pyactus.domain import ContractType
from pyactus.factory import create_attribute_set


class TestContract():
    def __init__(self, idx: int, obj: dict):
        self.idx = idx
        self.obj = obj

    def __str__(self):
        return f"{self.idx} :: {self.type.name} :: {self.role.name} :: {self.id}"

    @property
    def attribute_set(self) -> ContractAttributeSet:
        return create_attribute_set(self.type, self.terms)

    @property
    def id(self) -> str:
        return self.terms["contractID"]

    @property
    def results(self) -> str:
        return self.obj["results"]

    @property
    def terms(self) -> str:
        return self.obj["terms"]

    @property
    def role(self) -> ContractRole:
        return ContractRole[self.terms["contractRole"]]

    @property
    def type(self) -> ContractType:
        return ContractType[self.terms["contractType"]]
