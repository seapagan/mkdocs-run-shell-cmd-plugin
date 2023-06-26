# Test

Run the 'cowsay' command!

{{ run-shell-cmd(cmd="cowsay This works!!!") }}

Show the build OS information:

{{ run-shell-cmd(cmd='lsb_release -a') }}

Ping `google.com` 3 times and show the output.:

{{ run-shell-cmd(cmd='ping -c 3 google.com') }}
