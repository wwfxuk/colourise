# Colourise Terminal Output

Colourise `stdin` using a specific parser.

```bash
colourise [--shotgun-log|--katana]
```

Options         | Description
----------------|------------------------------------------
`--shotgun-log` | Colourise using parser for Shotgun logs.
`--katana`      | Colourise using parser for Katana stderr.


## Examples

Colourise continuously a Shotgun log file:

```bash
tail -F ~/.shotgun/logs/tk-desktop.log | colourise --shotgun-log
```

Colourise continuously a Katana process, combining `stdout` and `stderr`
before piping into to `colourise`:

```bash
katana |& colourise --katana
```


## Installation

1. Download the `colourise` file
1. Make it executable e.g. `chmod a+x colourise`
1. Start using it! e.g. `katana |& /full/path/to/colourise`

Top tip: add the the folder where you downloaded `colourise` script to the
`PATH` environment variable. Or just copy `colourise` to an existing folder
on `PATH` e.g. `/usr/local/bin`


## Bonus script: colour-test

Use `colour-test` to check your current Terminal's 4-8 bit colour/styles
capabilities. Install in the same way as `colourise`.

If no arguments are given, all tests will be output.

Usage: `colour-test [-1] [-2] [-3]`

Options           | Description
------------------|------------------------------------------
`-1`, `--retro`   | Test old-school, retro 4-bit colours and styles.
`-2`, `--combo`   | Test basic combinations of 8-bit colour.
`-3`, `--pretty`  | Test palette style combinations of 8-bit colour.
