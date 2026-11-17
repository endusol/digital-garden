"""Digital Garden Contract - strict rules, that may be checked."""
import copy
import typing as t
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.contract.contract_rule_1 import ContractRule1
from digital_garden.contract.contract_rule_2 import ContractRule2
from digital_garden.contract.contract_rule_3 import ContractRule3
from digital_garden.contract.contract_rule_4 import ContractRule4
from digital_garden.contract.contract_rule_5 import ContractRule5
from digital_garden.contract.contract_rule_6 import ContractRule6
from digital_garden.contract.contract_rule_7 import ContractRule7
from digital_garden.contract.contract_rule_8 import ContractRule8


_RULES: list[type[ContractRule]] = [
    ContractRule1,
    ContractRule2,
    ContractRule3,
    ContractRule4,
    ContractRule5,
    ContractRule6,
    ContractRule7,
    ContractRule8
]
_NAMES = [_.name for _ in _RULES]
assert len(_NAMES) == len(set(_NAMES)), 'Contract name collision!'
_CONTRACT: dict[str, type[ContractRule]] = {r.name: r for r in _RULES}


def get_contract(request: t.Collection[t.Union[str, int]] | None = None) -> dict[str, type[ContractRule]]:
    """
    Returns a contract subset containing only requested elements. Returns a full contract by default.
    :param request: Requested elements - collection of names or indexes (starting from 1: 1..N).
    :return: Contract subset.
    :raises: TypeError if passed request is not a collection.
    """
    if request is None:
        return copy.copy(_CONTRACT)
    if not isinstance(request, t.Collection):
        raise TypeError('Passed elements must be a collection!')
    return {
        name: rule
        for idx, (name, rule) in enumerate(_CONTRACT.items())
        if name in request or idx + 1 in request
    }
