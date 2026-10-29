"""Digital Garden contract rule."""
from __future__ import annotations
import abc
import typing as t
if t.TYPE_CHECKING:
    from digital_garden.document import Document


class ContractRule(abc.ABC):
    """Abstract base class for a single Digital Garden contract rule."""
    description: t.ClassVar[str]

    def __init_subclass__(cls, **kwargs: t.Any) -> None:
        super().__init_subclass__(**kwargs)
        if 'description' not in cls.__dict__ or not isinstance(cls.__dict__['description'], str):
            raise TypeError(f'Class `{cls.__name__}` must define `description` name of type `str`!')
        if 'check' not in cls.__dict__ or not isinstance(cls.__dict__['check'], classmethod):
            raise TypeError(f'Class `{cls.__name__}` must define `check` name of type `Callable[[Document], None]`!')

    @classmethod
    @abc.abstractmethod
    def check(cls, document: Document) -> None:
        """
        Check whether the document satisfies the rule.
        :param document: document to validate.
        :raises ContractViolationException: if the rule is violated.
        """
