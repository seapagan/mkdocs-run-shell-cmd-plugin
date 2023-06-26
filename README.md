# MkDocs Plugin : `run-shell-cmd` <!-- omit in toc -->

This is an [MkDocs](https://www.mkdocs.org/) plugin that runs the specified
command during the build and serve process and injects the command and output
into the generated site.

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [TODO](#todo)

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

To activate the console highlighting you will need to add the following to the
`markdown_extensions` section of your `mkdocs.yml`:

```yaml
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight
```

You will also need the `pymdown-extensions` and `pygments` packages installed in
your environment.

Then, in your template, you can use the **`{{ run-shell-cmd(cmd="my-command") }}`**
command:

```markdown
# My Project

Below is the output of `my-program --help`:

{{ run-shell-cmd(cmd='my-program --help') }}
```

The spaces around the tag are optional and it is case insensitive, also you can
use either double or single quotes around the command string.

All the below strings have identical output:

```markdown
{{ run-shell-cmd(cmd='my-program --help') }}
{{ run-shell-cmd(cmd="my-program --help") }}
{{RUN-SHELL-CMD(cmd='my-program --help')}}
{{run-shell-cmd(cmd="my-program --help")}}
{{ run-SHELL-cmd(cmd="my-program --help")}}
```

When the site is built, the progress will stop for each command discovered, and
the user will be asked if it should be run or not :

```console
INFO     -  Building documentation...
INFO     -  Cleaning site directory
"cowsay This works!!!" - Run this command? "[(Y)/(N)/(A)lways/(D)isable] [y]:  a
INFO     -  Documentation built in 1.91 seconds
INFO     -  [15:31:49] Watching paths for changes: 'docs', 'mkdocs.yml'

```

You can choose Yes, No, Always, or Disable. If you choose Always, you will never
be asked again **FOR THIS SESSION** and all further commands will be run. If you
choose Disable, you will never be asked again **FOR THIS SESSION** and NO
further commands will be run.

> There will **NEVER** be an option to run all commands by default without user
> choice, as this would be a massive security risk.

## Configuration

At this time there are no configuration options. I intend to add at least the
following options:

- disable wrapping in a fence
- choose a specific title for the output, it will be the same for all.

## License

This is released under the MIT License. See the bundled LICENSE file for more
details.

## TODO

- [ ] Fill in this shell
- [ ] Add configuration options
- [ ] Add tests
