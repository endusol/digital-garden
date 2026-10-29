"""Allowed document maturity statuses/stages."""
import enum


class DocumentStatus(enum.StrEnum):
    """Enum representing allowed document maturity statuses/stages."""
    SEEDS = 'seeds'
    SPROUT = 'sprout'
    EVERGREEN = 'evergreen'
