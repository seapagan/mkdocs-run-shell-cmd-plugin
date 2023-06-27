# MkDocs Plugin : `run-shell-cmd`

This is an [MkDocs](https://www.mkdocs.org/){:target="_blank"} plugin that runs
a specified command (or commands) during the `build`, `serve` and `publish`
process and injects the command and output into the generated site in a fenced
block.

It's very useful for documenting command-line programs, expecially during
development where the command line may change frequently.

See the [examples](../examples) page for several examples of the plugin in
action.

!!! danger "IMPORTANT"

    This plugin allows running arbitrary commands on your system. It does
    **NOT** check the command for safety, and it does **NOT** run the command in
    a sandbox. However, it does ask you if you want to run each command, and it
    does allow you to disable all commands from running again for the duration
    of the session.

    Also commands are not run using a shell, so your environment variables are
    not available to the command.

    Commands are set in the markdown file, so they are not run unless you build,
    serve or publish the site.

    If you are using a CI/CD pipeline to generate your docs, you should be aware
    that some standard commands may be missing or blocked, and the CI will
    probably hang due to waiting for input. Generating the docs on a local
    machine and then pushing them up to your hosting is probably a better idea.

## Installation

Install the package with pip:

```bash
pip install mkdocs-run-shell-cmd-plugin
```

or, if you are using [Poetry](https://python-poetry.org){:target="_blank"}:

```bash
poetry add mkdocs-run-shell-cmd-plugin --group dev
```

## Usage

Activate the plugin in your `mkdocs.yml`:

```yaml
plugins:
  - run-shell-cmd
```

!!! warning "Note"
    If you have no `plugins` entry in your config file yet, you'll likely also
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
your environment, unless you dont want the basic console syntax highlighting
similar to GitHub markdown.

Then, in your template, you can use the <code>\{\{
run-shell-cmd(cmd="my-command") }}</code> command:

<pre>
  # My Project

  Below is the output of `my-program --help`:

  &#x007B;{ run-shell-cmd(cmd='my-program --help') }}
</pre>

The spaces around the tag are optional and it is case insensitive, also you can
use either double or single quotes around the command string.

All the below strings have identical output:

<code>\{\{ run-shell-cmd(cmd='my-program --help') }}</code>

<code>\{\{ run-shell-cmd(cmd="my-program --help") }}</code>

<code>\{\{RUN-SHELL-CMD(cmd='my-program --help')}}</code>

<code>\{\{run-shell-cmd(cmd="my-program --help")}}</code>

<code>\{\{ run-SHELL-cmd(cmd="my-program --help")}}</code>

When the site is built, the progress will stop for each command discovered, and
the user will be asked if it should be run or not :

```console
INFO     -  You are using the 'run-shell-cmd' Plugin.
            This will RUN SHELL COMMANDS that are specified in the markdown files!
            You will be asked to CONFIRM each command, or you can specify (a)lways or (d)isable.
            Visit https://seapagan.github.io/mkdocs-run-shell-cmd-plugin for more info.
INFO     -  Building documentation...
INFO     -  Cleaning site directory
[Run Shell Command] - Run "cowsay This works!!!"? [y/n/a/d/yes/no/always/disable] (yes):
[Run Shell Command] - Run "lsb_release -a"? [y/n/a/d/yes/no/always/disable] (yes): a
INFO     -  Documentation built in 6.78 seconds
INFO     -  [09:56:25] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [09:56:25] Serving on http://127.0.0.1:8000/
```

You can choose Yes, No, Always, or Disable. If you choose Always, you will never
be asked again **FOR THIS SESSION** and all further commands will be run. If you
choose Disable, you will never be asked again **FOR THIS SESSION** and NO
further commands will be run.

!!! note

    Be aware, if you do not choose **Always** or **Disable**, you will be asked
    again for each command whenever you change a file and the site is rebuilt
    under `mkdocs serve`, even if the page with the command has not changed.

    To fix this you can either choose one of the options above or you can use
    the `--dirtyreload` option to `mkdocs serve` The latter option will only
    re-create markdown files that have actually changed, but note the warning
    that this **may** cause navigation issues. I have not seen this myself, this
    is never usually an issue while serving the site locally.

!!! danger "IMPORTANT"

    There will **NEVER** be an option to run all commands by default without
    user oversight, as this would be a massive security risk.

## Configuration

At this time there are no configuration options. I intend to add at least the
following options:

- disable wrapping in a fence
- choose a specific title for the output, it will be the same for all.

## License

This is released under the MIT License. See the bundled LICENSE file for more
details.
