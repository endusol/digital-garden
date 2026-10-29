"""Digital Garden contract - strict rules, that may be checked."""

from digital_garden.contract.contract_rule import ContractRule
from digital_garden.contract.contract_rule_1 import ContractRule1
from digital_garden.contract.contract_rule_2 import ContractRule2
from digital_garden.contract.contract_rule_3 import ContractRule3
from digital_garden.contract.contract_rule_4 import ContractRule4
from digital_garden.contract.contract_rule_5 import ContractRule5
from digital_garden.contract.contract_rule_6 import ContractRule6
from digital_garden.contract.contract_rule_7 import ContractRule7

CONTRACT: list[type[ContractRule]] = [
    ContractRule1,
    ContractRule2,
    ContractRule3,
    ContractRule4,
    ContractRule5,
    ContractRule6,
    ContractRule7,
]
