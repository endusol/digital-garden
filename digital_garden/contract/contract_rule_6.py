"""Field `aliases` must not contain duplicated values."""
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule6(ContractRule):
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        aliases = document.frontmatter.get('aliases')
        aliases = aliases if isinstance(aliases, list) else []
        if len(aliases) != len(set(aliases)):
            raise ContractViolationException(cls.description)
