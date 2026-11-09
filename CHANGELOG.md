# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-11-09

### Added
- `greet(name, punctuation="!")` now accepts a custom ending such as `greet("Hee", ".")`; existing `greet("Hee")` calls still return `Hello, Hee!`.

### Fixed
- `greet("")` and whitespace-only names now return `Hello, world!` instead of a greeting with a blank name such as `Hello, !`.

## [0.1.0] - 2026-11-09

### Added
- Add `greet(name)` and a command-line greeting: previously unavailable, now return or print `Hello, <name>!`.
