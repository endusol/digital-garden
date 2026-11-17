"""Each `aliases` value must be a non-zero-length string that does not start or end with a whitespace character."""
import re
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule8(ContractRule):
    name = 'frontmatter-aliases-format'
    # noinspection unresolved-references
    description = __doc__.strip()
    REGEX_DIGITAL_GARDEN_ALIAS = re.compile(r'(?!\s).+(?<!\s)')

    @classmethod
    def check(cls, document):
        aliases = document.frontmatter.get('aliases')
        aliases = aliases if isinstance(aliases, list) else []
        invalid_aliases = {a for a in aliases if not cls.REGEX_DIGITAL_GARDEN_ALIAS.fullmatch(a)}
        if invalid_aliases:
            raise ContractViolationException(cls.description + f'\nInvalid aliases: {", ".join(invalid_aliases)}')
