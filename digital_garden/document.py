"""Document class representing a single note in the digital garden."""

import copy
import pathlib
import frontmatter
from digital_garden.document_status import DocumentStatus


class Document:
    """TODO: fill in later"""

    def __init__(self, path: pathlib.Path):
        """
        Read the document from the given path.
        :param path: path to the document/note.
        """
        self._path = path
        self._document = frontmatter.load(path)

    @property
    def content(self) -> str:
        """Document content."""
        return self._document.content

    @content.setter
    def content(self, content: str):
        self._document.content = str(content)

    @property
    def frontmatter(self) -> dict[str, object]:
        """Document frontmatter."""
        return copy.deepcopy(self._document.metadata)

    def set_status(self, status: DocumentStatus):
        """
        Set the status of the document.
        :param status: new status.
        :return:
        """
        assert status in DocumentStatus, (
            f"Passed status ``{status}`` is not supported by the contract!"
        )
        self._document.metadata["status"] = str(status)

    def add_tag(self, tag: str):
        """
        Add a tag to the document frontmatter.
        :param tag: new tag to add.
        """

    def drop_tag(self, tag: str): ...

    def add_alias(self, alias: str): ...

    def drop_alias(self, alias: str): ...

    def add_frontmatter_field(self, name: str, value): ...

    def drop_frontmatter_field(self, name: str): ...
