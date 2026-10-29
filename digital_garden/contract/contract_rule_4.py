"""
Any other frontmatter field except the `tags`, `aliases`, `status` must:
- consist only of lowercase Latin alphanumeric characters or underscores (`_`),
- be considered "for internal usage" / "technical" and therefore be marked with the `_` prefix.
"""
import re
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule4(ContractRule):
    REGEX_FIELD = re.compile(r'^tags|aliases|status|_[a-z0-9_]*$')
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        if not all(cls.REGEX_FIELD.fullmatch(_) for _ in document.frontmatter):
            raise ContractViolationException(cls.description)
