"""Main Class for this Plugin."""
import re
import shlex
import subprocess  # nosec
from typing import Literal

from mkdocs.plugins import BasePlugin


class RunShellCmdPlugin(BasePlugin):
    """Class for the 'mkdocs-run-shell-cmd-plugin'."""

    def ok_to_run(self, command: str):
        """Return True if we should run on this command.

        The User is asked yes/no/always/disable.
        """
        if self.disable_run:
            return False
        elif self.always_run:
            return True

        run_this = input(
            f'"{command}" - Run this command? '
            "[(Y)/(N)/(A)lways/(D)isable] [y]: "
        )
        if run_this.lower() in ["a", "always"]:
            self.always_run = True
        elif run_this.lower() in ["d", "disable"]:
            self.disable_run = True

        return (
            True
            if (
                run_this == ""
                or run_this.lower() in ["y", "yes"]
                or (
                    self.always_run and not self.disable_run
                )  # disable has priority, should never be set together anyway.
            )
            else False
        )

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.
        """
        self.PLUGIN_TAG = "run-shell-cmd"

        self.always_run = False
        self.disable_run = False

    def on_page_markdown(self, markdown: str, **kwargs) -> str | None:
        """Modify the markdown if our tag is present."""
        cmds = re.finditer(
            pattern=(
                rf"{{{{\s*{self.PLUGIN_TAG}"
                rf"\(cmd=[\"|\'](.+)[\"|\']\).*\s*}}}}"
            ),
            string=markdown,
            flags=re.IGNORECASE,
        )
        if cmds:
            for match in cmds:
                try:
                    if not self.ok_to_run(match.group(1)):
                        continue
                    cmd_output = subprocess.run(
                        shlex.split(match.group(1)),
                        capture_output=True,
                        text=True,
                        check=True,
                    )  # nosec
                    cmd_result = cmd_output.stdout
                except subprocess.CalledProcessError as e:
                    cmd_result = e.stderr
                    print(e)

                output = (
                    "\n\n```{.console linenums='0' title=''}"
                    f"\n$ {match.group(1)}\n{cmd_result}\n```\n"
                )
                markdown = markdown.replace(match.group(0), output)

        return markdown
