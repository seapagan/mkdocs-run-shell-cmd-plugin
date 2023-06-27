# MkDocs Plugin : `run-shell-cmd` <!-- omit in toc -->

[![PyPI version](https://badge.fury.io/py/mkdocs-run-shell-cmd-plugin.svg)](https://badge.fury.io/py/mkdocs-run-shell-cmd-plugin)

This is an [MkDocs](https://www.mkdocs.org/) plugin that runs a specified
command (or commands) during the `build` and `serve` process and injects the
command and output into the generated site in a fenced block.

It's very useful for documenting command-line programs, expecially during
development where the command line may change frequently.

**See the [Website][website] for examples and full documentation.**

- [IMPORTANT](#important)
- [Installation](#installation)
- [Configuration and Usage](#configuration-and-usage)
- [License](#license)
- [TODO](#todo)

## IMPORTANT

  > This plugin allows running arbitrary commands on your system. It does
  > **NOT** check the command for safety, and it does **NOT** run the command in
  > a sandbox. However, it does ask you if you want to run each command, and it
  > does allow you to disable all commands from running again for the duration
  > of the session. Also commands are not run using a shell, so your environment
  > variables are not available to the command. Commands are set in the markdown
  > file, so they are not run unless you build, serve or publish the site. If
  > you are using a CI/CD pipeline to generate your docs, you should be aware
  > that some standard commands may be missing or blocked, and the CI will
  > probably hang due to waiting for input. Generating the docs on a local
  > machine and then pushing them up to your hosting is probably a better idea.

## Installation

Install the package with pip:

```bash
pip install mkdocs-run-shell-cmd-plugin
```

or, if you are using [Poetry](https://python-poetry.org):

```bash
poetry add mkdocs-run-shell-cmd-plugin --group dev
```

## Configuration and Usage

See the [Website][website] for
full usage information.

## License

This is released under the MIT License. See the bundled LICENSE file for more
details.

## TODO

See [TODO.md](TODO.md) for a list of outstanding tasks or ideas.

[website]: https://seapagan.github.io/mkdocs-run-shell-cmd-plugin/
