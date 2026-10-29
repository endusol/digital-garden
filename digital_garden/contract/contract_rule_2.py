"""Field `aliases` must exist in the frontmatter and its value must be a list of strings."""
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule2(ContractRule):
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        # noinspection not-iterable
        if False \
                or 'aliases' not in document.frontmatter \
                or not isinstance(document.frontmatter['aliases'], list) \
                or not all(isinstance(_, str) for _ in document.frontmatter['aliases']):
            raise ContractViolationException(cls.description)
