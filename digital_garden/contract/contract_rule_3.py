"""
Field `status` must exist in the frontmatter and its value must be one of the allowed
document maturity stages: `seeds`, `sprout`, `evergreen`.
"""
from digital_garden.document_status import DocumentStatus
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule3(ContractRule):
    # noinspection unresolved-references
    description = __doc__.strip()

    @classmethod
    def check(cls, document):
        if document.frontmatter.get('status') not in DocumentStatus:
            raise ContractViolationException(cls.description)
