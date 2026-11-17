"""Digital Garden contract - strict rules, that may be checked."""
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.contract.contract_rule_1 import ContractRule1
from digital_garden.contract.contract_rule_2 import ContractRule2
from digital_garden.contract.contract_rule_3 import ContractRule3
from digital_garden.contract.contract_rule_4 import ContractRule4
from digital_garden.contract.contract_rule_5 import ContractRule5
from digital_garden.contract.contract_rule_6 import ContractRule6
from digital_garden.contract.contract_rule_7 import ContractRule7
from digital_garden.contract.contract_rule_8 import ContractRule8


CONTRACT: dict[int, type[ContractRule]] = {
    1: ContractRule1,
    2: ContractRule2,
    3: ContractRule3,
    4: ContractRule4,
    5: ContractRule5,
    6: ContractRule6,
    7: ContractRule7,
    8: ContractRule8
}
