# MkDocs Plugin : `run-shell-cmd`

<!-- [![PyPI version](https://badge.fury.io/py/mkdocs-latest-git-tag-plugin.svg)](https://badge.fury.io/py/mkdocs-latest-git-tag-plugin) -->

This is an [MkDocs](https://www.mkdocs.org/) plugin that runs the specified
command during the build process and injects the command and output into the
generated site.

Status: **Currently a blank shell with no functionality**

## Installation

Install the package with pip:

```bash
pip install mkdocs-run-shell-cmd-plugin
```

or, if you are using [Poetry](https://python-poetry.org):

```bash
poetry add mkdocs-run-shell-cmd-plugin --group dev
```

## Usage

Activate the plugin in your `mkdocs.yml`:

```yaml
plugins:
  - run-shell-cmd
```

 > If you have no `plugins` entry in your config file yet, you'll likely also
want to add the `search` plugin. MkDocs enables it by default if  here is no
`plugins` entry set.

Then, in your template, you can use the `{{ run-shell-cmd }}` variable:

```markdown
# My Project

{{ run-shell-cmd 'my-program --help' }}
```

The spaces around the tag are optional and it is case insensitive.

## Configuration

At this time there are no configuration options. I intend to add at least the
following optons:

- 'fence' wrap the output with a markdown code block, default: `true`. sub
  options to choose 'console' or 'bash' syntax highlighting. Will need optional
  dependency on `pygments`.

## License

This is released under the MIT License. See the bundled LICENSE file for more
details.

## TODO

- [ ] Fill in this shell
- [ ] Add configuration options
- [ ] Add tests
