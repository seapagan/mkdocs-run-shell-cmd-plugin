"""Main Class for this Plugin."""
from typing import Literal

from mkdocs.plugins import BasePlugin


class LatestGitTagPlugin(BasePlugin):
    """Class for the 'mkdocs-latest-git-tag-plugin'."""

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.
        """

    def on_page_markdown(self, markdown: str, page, **kwargs) -> str | None:
        """Modify the markdown if our tag is present."""
        # process the markdown and substitute the tag for generated text

        return markdown
