"""
Each `tags` value must comply with the following structure:
- Tag starts with the `#` character.
- The `#` character is followed by a "tag body", where the "tag body":
    - is full lowercase,
    - is non-zero length,
    - consists only of Latin alphanumeric characters or dashes (`-`),
    - does not start with a digit (may start with a letter or a dash).
- There may be several "tag bodies" separated by a single `/` character
  (empty segments like `//` are not allowed).
"""
import re
from digital_garden.contract.contract_rule import ContractRule
from digital_garden.exceptions import ContractViolationException


class ContractRule7(ContractRule):
    name = 'all-tags-format'
    # noinspection unresolved-references
    description = __doc__.strip()
    REGEX_ESCAPED_CHAR       = re.compile(r'\\.')
    REGEX_HTML_TAG           = re.compile(r'<[^>]*>')
    REGEX_MD_CODE_BLOCKS     = re.compile(r'```[\s(\S)]*?```|`[^`\n]*`')
    REGEX_NO                 = re.compile(r'#\d+\b')
    REGEX_OBSIDIAN_TAG       = re.compile(r'#[\w/-]+')
    REGEX_DIGITAL_GARDEN_TAG = re.compile(r'^#(?!/)(?:/?[a-z\d-]+)+$')

    @classmethod
    def check(cls, document):
        content = document.content
        content = cls.REGEX_ESCAPED_CHAR  .sub('', content)
        content = cls.REGEX_HTML_TAG      .sub('', content)
        content = cls.REGEX_MD_CODE_BLOCKS.sub('', content)
        content = cls.REGEX_NO            .sub('', content)
        content_tags = cls.REGEX_OBSIDIAN_TAG.findall(content)
        frontmatter_tags = document.frontmatter.get('tags')
        frontmatter_tags = frontmatter_tags if isinstance(frontmatter_tags, list) else []
        tags = set(content_tags + frontmatter_tags)
        invalid_tags = {t for t in tags if not cls.REGEX_DIGITAL_GARDEN_TAG.fullmatch(t)}
        if invalid_tags:
            raise ContractViolationException(cls.description + f'\nList of invalid tags: {", ".join(invalid_tags)}')
