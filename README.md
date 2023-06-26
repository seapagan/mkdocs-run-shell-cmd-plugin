# MkDocs Plugin : `run-shell-cmd` <!-- omit in toc -->

This is an [MkDocs](https://www.mkdocs.org/) plugin that runs the specified
command during the `build` and `serve` process and injects the command and
output into the generated site in a fenced block.

It's very useful for documenting command-line programs, expecially during
development where the command line may change frequently.

See the [demo](https://seapagan.github.io/mkdocs-run-shell-cmd-plugin/) for an example.

- [IMPORTANT](#important)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
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
  > probably hang. Generating the docs on a local machine and then pushing them
  > up to your hosting is probably a better idea.

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

- [ ] Add configuration options
- [ ] Add tests
- [ ] Find a way to run on CI/CD without prompting the user, but in a safe way
  that doesn't allow arbitrary commands to be run. We can always check the `CI`
  environment variable, but it's still not good practice to run arbitrary code.
