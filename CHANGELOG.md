# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com), and
this project adheres to [Semantic Versioning](https://semver.org).


## [0.5.0] - 2019-11-28

Hiero parser, based off Katana one.

### Added

- `--hiero` for `colourise`.
- `gitignore` inclusion rule for `tests/resources/logs/*.log`

## [0.4.0] - 2019-11-02

Ping and some minor fixes.

### Added

- `--ping` for `colourise`.
- Mac Terminal colour environment variable.


### Changed

- CI job names to better reflect whether in terminal or not.


### Fixed

- Name of parser being printed at startup.


## [0.3.0] - 2019-10-25

Now available as rez package.

### Added

- `package.py` for [rez package](https://github.com/nerdvegas/rez).
- rez package install CI for Linux and OSX.
- Windows (bash) tests for CI


## [0.2.0] - 2019-10-25

### Added

- `--help` for `colour-test`.
- Initial CI GitHub Workflow Action.

### Fixed

- Made `colourise` and `colour-test` executable when `git clone`d.


## [0.1.0] - 2019-10-24

Initial release.

### Added

- `LICENSE`, `CHANGELOG.md`, `README.md` documents.
- `colourise` and `colour-test` scripts.
