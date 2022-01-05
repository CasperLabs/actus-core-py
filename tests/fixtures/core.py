import json
import os
import pathlib
import typing

import pytest

from pyactus.domain import ContractType
from pyactus.domain import ContractAttributeSet

from tests.fixtures.domain import TestContract


_ACTUS_TESTS_REPO: pathlib.Path = pathlib.Path(os.getenv("ACTUS_TESTS_HOME")) / "tests"


@pytest.fixture(scope="session")
def test_contracts():
    return list(_yield_contracts())


def _yield_contracts() -> typing.Iterator[typing.Tuple[ContractType, dict]]:
    for contract_type in ContractType:
        if contract_type != ContractType.PAM:
            continue
        for idx, obj in enumerate(_read_fixture(contract_type)):
            yield TestContract(idx + 1, obj)


def _read_fixture(contract_type: ContractType) -> typing.List[dict]:
    fpath: pathlib.Path = _ACTUS_TESTS_REPO / f"actus-tests-{contract_type.name.lower()}.json"
    if not fpath.exists():
        return []

    with open(fpath, "r") as fstream:
        return json.loads(fstream.read()).values()
