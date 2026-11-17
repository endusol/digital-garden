"""Digital Garden zen principle."""

from __future__ import annotations
import abc
import typing as t


class ZenPrinciple(abc.ABC):
    """Abstract base class for a single Digital Garden zen principle."""
    description: t.ClassVar[str]

    def __init_subclass__(cls, **kwargs: t.Any) -> None:
        super().__init_subclass__(**kwargs)
        if 'description' not in cls.__dict__ or not isinstance(cls.__dict__['description'], str):
            raise TypeError(f'Class `{cls.__name__}` must define `description` name of type `str`!')
        if 'name' not in cls.__dict__ or not isinstance(cls.__dict__['name'], str):
            raise TypeError(f'Class `{cls.__name__}` must define `name` name of type `str`!')
