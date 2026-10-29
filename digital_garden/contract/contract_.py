"""Digital Garden contract - strict rules, that may be checked."""
from __future__ import annotations
import argparse
import re
import textwrap
import typing as t
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from digital_garden.document import Document


RE = argparse.Namespace()
RE.FIELD = re.compile(r'^tags|aliases|status|_[a-z0-9_]*$')
RE.TAG = re.compile(r'^#[a-z-][a-z0-9-]*$')


def _rule(rule: t.Callable) -> str:
    return textwrap.dedent(rule.__doc__).strip()


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
