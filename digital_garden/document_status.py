"""Allowed by the contract document statuses."""
import enum


class DocumentStatus(enum.StrEnum):
    """Enum representing the status of the note."""
    SEEDS = 'seeds'
    SPROUT = 'sprout'
    EVERGREEN = 'evergreen'
