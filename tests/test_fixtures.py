from tests.fixtures.domain import TestContract


def test_core_fixtures(test_contracts):
    for test_contract in test_contracts:
        assert len(test_contract.attribute_set) > 0
        assert test_contract.attribute_set["contractType"] == test_contract.attribute_set.contractType
        for attribute in test_contract.attribute_set:
            assert attribute.name in test_contract.attribute_set

    raise ValueError()
