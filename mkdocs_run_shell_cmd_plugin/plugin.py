"""Main Class for this Plugin."""
import re
import shlex
import subprocess  # nosec
from typing import Literal

from mkdocs.plugins import BasePlugin
from rich import print  # pylint: disable=redefined-builtin
from rich.prompt import Prompt


class RunShellCmdPlugin(BasePlugin):
    """Class for the 'mkdocs-run-shell-cmd-plugin'."""

    def __init__(self):
        """Set up variables for this plugin."""
        self.plugin_tag = "run-shell-cmd"

        self.always_run = False
        self.disable_run = False

    def ok_to_run(self, command: str):
        """Return True if we should run on this command.

        The User is asked yes/no/always/disable.
        """
        if self.disable_run:
            return False
        if self.always_run:
            return True

        run_this = Prompt.ask(
            f'[green][Run Shell Command][/green] - Run "[red]{command}[/red]"?',
            choices=["y", "n", "a", "d", "yes", "no", "always", "disable"],
            default="yes",
        )

        if run_this.lower() in ["a", "always"]:
            self.always_run = True
        elif run_this.lower() in ["d", "disable"]:
            self.disable_run = True

        return bool(
            run_this == ""
            or run_this.lower() in ["y", "yes"]
            or (
                self.always_run and not self.disable_run
            )  # disable has priority, should never be set together anyway.
        )

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.
        """
        print(
            "INFO     -  [green]You are using the '[red]run-shell-cmd[/red]"
            "[green]' Plugin."
        )
        print(
            "            [bold]This will [red]RUN SHELL COMMANDS[/red] that "
            "are specified in the markdown files!"
        )
        print(
            "            You will be asked to [red]CONFIRM[/red] each command,"
            " or you can specify [red](a)lways[/red] or [red](d)isable[/red]."
        )
        print(
            "            Visit [green]https://seapagan.github.io/mkdocs-run"
            "-shell-cmd-plugin[/green] for more info."
        )

    def on_page_markdown(self, markdown: str, **kwargs) -> str | None:
        """Modify the markdown if our tag is present."""
        cmds = re.finditer(
            pattern=(
                rf"{{{{\s*{self.plugin_tag}"
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
                except subprocess.CalledProcessError as exc:
                    cmd_result = exc.stderr
                    print(exc)

                output = (
                    "\n\n```{.console linenums='0' title=''}"
                    f"\n$ {match.group(1)}\n{cmd_result}\n```\n"
                )
                # we only replace the first occurrence of the tag, in case
                # multiple tags are present in the markdown. This allows
                # commands that have different output when run again to be
                # shown. It would slow the build down if the same command is run
                # multiple times without output changing but that is acceptable.
                # Maybe we can add a config option to control this in the
                # future.
                markdown = markdown.replace(match.group(0), output, 1)

        return markdown
