"""Digital Garden zen principle."""
from __future__ import annotations
import re
import abc
import typing as t


class ZenPrinciple(abc.ABC):
    """Abstract base class for a single Digital Garden zen principle."""
    name: t.ClassVar[str]
    description: t.ClassVar[str]
    REGEX_NAME = re.compile(r'[a-z\d-]+')
    REGEX_DESCRIPTION = re.compile(r'(?!\s).+(?<!\s)', re.DOTALL)

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if abc.ABC in cls.__bases__:
            return
        if 'name' not in cls.__dict__ or not isinstance(cls.__dict__['name'], str):
            raise TypeError(f'Class `{cls.__name__}` must define name `name` of type `str`!')
        if 'description' not in cls.__dict__ or not isinstance(cls.__dict__['description'], str):
            raise TypeError(f'Class `{cls.__name__}` must define name `description` of type `str`!')
        if not cls.REGEX_NAME.fullmatch(cls.__dict__['name']):
            raise TypeError(fr'Name `{cls.__name__}.name` must be in the following format: /^[a-z\d-]+$/!')
        if not cls.REGEX_DESCRIPTION.fullmatch(cls.__dict__['description']):
            raise TypeError(fr'Name `{cls.__name__}.description` must be in the following format: /^(?!\s).+(?<!\s)$/!')
