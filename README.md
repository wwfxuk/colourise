# Colourise Terminal Output

[![CI Workflow Badge](https://github.com/wwfxuk/colourise/workflows/CI/badge.svg)](https://github.com/wwfxuk/colourise/actions?workflow=CI)
[![Rez Workflow Badge](https://github.com/wwfxuk/colourise/workflows/Rez/badge.svg)](https://github.com/wwfxuk/colourise/actions?workflow=Rez)

Colourise `stdin` using a specific `bash` script parser.

![image](https://user-images.githubusercontent.com/9294702/68074122-a1e80980-fd8f-11e9-8f14-60dae3d2bf09.png)

```bash
colourise [--shotgun-log|--katana|--ping]
```

Options         | Description
----------------|------------------------------------------
`--shotgun-log` | Colourise using parser for Shotgun logs.
`--katana`      | Colourise using parser for Katana stderr.
`--ping`        | Colourise using parser for ping.


## Examples

Colourise continuously a Shotgun log file:

```bash
tail -F ~/.shotgun/logs/tk-desktop.log | colourise --shotgun-log
```

Colourise continuously a Katana process, combining `stdout` and `stderr`
before piping into to `colourise`:

```bash
katana |& colourise --katana
# For Mac's Terminal: katana 2>&1 | colourise --katana
```

Colourise continuously a `ping` process, useful when ~~gaming~~ monitoring
server latency.

> Added in [0.4.0](https://github.com/wwfxuk/colourise/releases/tag/0.4.0)

```bash
ping www.google.com | colourise --ping
```

## Installation

Requires `bash` to be installed.

1. Download the `colourise` file
1. Make it executable e.g. `chmod a+x colourise`
1. Start using it! e.g. on Linux `katana |& /full/path/to/colourise --katana`

Top tip: add the the folder where you downloaded `colourise` script to the
`PATH` environment variable. Or just copy `colourise` to an existing folder
on `PATH` e.g. `/usr/local/bin`

### rez package

You can also install this a a [rez package](https://github.com/nerdvegas/rez)

1. Download or `git clone` this repository
1. From the extracted repository root, run `rez build --install`
1. Start using the `colourise` package e.g. on Mac OSX
   `katana 2>&1 | rez env colourise -- colourise --katana`


## Bonus script: colour-test

Use `colour-test` to check your current Terminal's 4-8 bit colour/styles
capabilities. Install in the same way as `colourise`.

If no arguments are given, all tests will be output.

![colour-test](https://user-images.githubusercontent.com/9294702/67518594-01159200-f69d-11e9-996f-93c8efee80a7.gif)

Usage: `colour-test [-1] [-2] [-3]`

Options           | Description
------------------|------------------------------------------
`-1`, `--retro`   | Test old-school, retro 4-bit colours and styles.
`-2`, `--combo`   | Test basic combinations of 8-bit colour.
`-3`, `--pretty`  | Test palette style combinations of 8-bit colour.
