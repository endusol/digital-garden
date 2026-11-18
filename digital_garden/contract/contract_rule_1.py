"""Field `tags` must exist in the frontmatter and its value must be a list of strings."""
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule1(ContractRule):
    name = 'frontmatter-tags-presence-and-type'
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        # noinspection not-iterable
        if False \
                or not 'tags' in document.frontmatter \
                or not isinstance(document.frontmatter['tags'] or [], list) \
                or not all(isinstance(_, str) for _ in document.frontmatter['tags'] or []):
            raise ContractViolationException(cls.description)
