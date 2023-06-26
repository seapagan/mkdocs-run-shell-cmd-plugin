# Examples

Below are some examples of the plugin in action. First is the required tag to
use in the Markdown file, then the output of the command.

Run the 'cowsay' command!

<code>\{\{ run-shell-cmd(cmd="cowsay This works!!!") }}</code>

{{ run-shell-cmd(cmd="cowsay This works!!!") }}

Show the build OS information:

<code>\{\{ run-shell-cmd(cmd='lsb_release -a') }}</code>

{{ run-shell-cmd(cmd='lsb_release -a') }}

Ping `google.com` 3 times and show the output.:

<code>\{\{ run-shell-cmd(cmd='ping -c 3 google.com') }}</code>

{{ run-shell-cmd(cmd='ping -c 3 google.com') }}
