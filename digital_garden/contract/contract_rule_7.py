"""Each `tags` value must be a lowercase non-zero length string consisting of Latin alphanumeric characters or dashes (`-`); prefixed by the hashtag character (`#`); and not starting with a digit."""
import re
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule7(ContractRule):
    REGEX_TAG = re.compile(r'^#[a-z-][a-z0-9-/]*$')
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        tags = document.frontmatter.get('tags')
        tags = tags if isinstance(tags, list) else []
        if not all(cls.REGEX_TAG.fullmatch(_) for _ in tags):
            raise ContractViolationException(cls.description)
