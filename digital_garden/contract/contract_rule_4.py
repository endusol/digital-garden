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
        invalid_fields = {f for f in document.frontmatter if not cls.REGEX_FIELD.fullmatch(f)}
        if invalid_fields:
            raise ContractViolationException(cls.description + f'\nInvalid fields: {", ".join(invalid_fields)}')
