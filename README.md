# greet-release

A small greeting program with tests, CI, and reviewed dependency updates.
Version strategy: Semantic Versioning (MAJOR.MINOR.PATCH).

Run all commands from the repository root.

```bash
uv sync --locked
uv run --locked python greet.py Hee
uv run --locked python greet.py
uv run --locked python greet.py ''
uv run --locked pytest -q greet.py
uv build
```

`greet()` returns text; `main()` reads arguments and prints it.
CI runs tests on Python 3.11 and 3.12; Dependabot proposes weekly updates.
