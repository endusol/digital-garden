"""Field `tags` must not contain duplicated values."""
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule5(ContractRule):
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        tags = document.frontmatter.get('tags')
        tags = tags if isinstance(tags, list) else []
        if len(tags) != len(set(tags)):
            raise ContractViolationException(cls.description)
