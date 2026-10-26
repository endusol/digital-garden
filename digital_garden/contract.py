"""Digital Garden contract - strict rules, that may be checked."""
import argparse
import re
import textwrap
import typing as t
from digital_garden.document import Document


RE = argparse.Namespace()
RE.FIELD = re.compile(r'^tags|aliases|status|_[a-z0-9_]*$')
RE.TAG = re.compile(r'^#[a-z-][a-z0-9-]*$')


def _rule(rule: t.Callable) -> str:
    return textwrap.dedent(rule.__doc__).strip()


def check_rule_1(d: Document) -> None | str:
    """Field `tags` must exist in the frontmatter and its value must be a list of strings."""
    # noinspection not-iterable
    return None if True \
            and 'tags' in d.frontmatter \
            and isinstance(d.frontmatter['tags'], list) \
            and all(isinstance(_, str) for _ in d.frontmatter['tags']) \
        else _rule(check_rule_1)


def check_rule_2(d: Document) -> None | str:
    """Field `aliases` must exist in the frontmatter and its value must be a list of strings."""
    # noinspection not-iterable
    return None if True \
            and 'aliases' in d.frontmatter \
            and isinstance(d.frontmatter['aliases'], list) \
            and all(isinstance(_, str) for _ in d.frontmatter['aliases']) \
        else _rule(check_rule_2)


def check_rule_3(d: Document) -> None | str:
    """Field `status` must exist in the frontmatter and its value must be a string."""
    return None if True \
            and 'status' in d.frontmatter \
            and isinstance(d.frontmatter['status'], str) \
        else _rule(check_rule_3)


def check_rule_4(d: Document) -> None | str:
    """
    Any other frontmatter field except the `tags`, `aliases`, `status` must:
    - consist only of lowercase Latin alphanumeric characters or underscores (`_`),
    - be considered "for internal usage" / "technical" and be marked with the `_` prefix.
    """
    return None if all(RE.FIELD.fullmatch(_) for _ in d.frontmatter) else _rule(check_rule_4)


def check_rule_5(d: Document) -> None | str:
    """Field `tags` must not contain duplicated values."""
    tags = d.frontmatter.get('tags')
    tags = tags if isinstance(tags, list) else []
    return None if len(tags) == len(set(tags)) else _rule(check_rule_5)


def check_rule_6(d: Document) -> None | str:
    """Field `aliases` must not contain duplicated values."""
    aliases = d.frontmatter.get('aliases')
    aliases = aliases if isinstance(aliases, list) else []
    return None if len(aliases) == len(set(aliases)) else _rule(check_rule_6)


def check_rule_7(d: Document) -> None | str:
    """
    Each `tags` value must be a lowercase non-zero length string consisting of Latin alphanumeric characters
    or dashes (`-`); prefixed by the hashtag character (`#`); and not starting with a digit.
    """
    tags = d.frontmatter.get('tags')
    tags = tags if isinstance(tags, list) else []
    return None if all(RE.TAG.fullmatch(_) for _ in tags) else _rule(check_rule_7)

# 6) Each tag always start with `#` followed by a Latin alphanumeric characters or dashes (`-`)
#    with optional slashes (`/`) in the middle. Note: slashes are prohibited at the very
#    start and the very end of the tag: /^#(?=(?:[^\W_]|-))(?:[^\W_]|[\/-])+(?<=(?:[^\W_]|-))$/
# 7) Each alias is a non-zero-length string not starting
#    nor ending with a whitespace character: /^(?!\s).*(?<!\s)$/
# 8) Status is one of the allowed statuses (`digital_gardent.document_status.DocumentStatus`).

def check_contract(document: Document) -> None | str:
    """
    Checks all the rules of the contract
    :param document: document to check
    :return:
    """

CONTRACT = {
    1: check_rule_1.__doc__
}
FULL_CONTRACT = '\n\n'.join(f'# RULE #{idx}\n{rule}' for idx, rule in CONTRACT.items())


