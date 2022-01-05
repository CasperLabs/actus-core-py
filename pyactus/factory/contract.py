from pyactus.domain import ContractAttributeSet
from pyactus.domain import ContractType


from pyactus.factory.contract_attribute import create_attribute


def create_attribute_set(contract_type: ContractType, obj: dict) -> ContractAttributeSet:
    return ContractAttributeSet(
        contract_type=contract_type,
        attributes=[create_attribute(contract_type, k, v) for k, v in obj.items()]
        )


_PARSERS1 = {
    ContractType.PAM: {
        "ContractRole": ("contractRole", to_contract_role, ValueError),
        "ContractType": ("contractType", to_contract_type, ValueError),
        "contractType": to_contract_type,
        "statusDate": to_iso_datetime_T24,
        "feeRate": to_optional("feeRate", to_rate, float())
    }
}
