# TODO List

- [ ] Add configuration options
- [ ] Add tests
- [ ] Find a way to run on CI/CD without prompting the user, but in a safe way
  that doesn't allow arbitrary commands to be run. We can always check the `CI`
  environment variable, but it's still not good practice to run arbitrary code.
- [ ] Configure option to enable/disable only changing the first instance of a
  command in a document. Currently identical commands in the same document will
  be run each time instead of replacing the output of all with the first. This
  is a design decision, but it may be useful to have the option to change it.
- [x] Use [Rich](https://github.com/Textualize/rich) to emphasize the console
  output with color etc.
- [ ] Allow hiding the command line in the output (ie remove the first line).
