"""Return greetings and provide a small command-line entry point."""

import sys


def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting; blank names use world and punctuation is optional."""
    # Check for blank input without changing nonblank names.
    if not name.strip():
        name = "world"
    return f"Hello, {name}{punctuation}"


def main() -> int:
    """Read the first argument, print one greeting, and report success."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet():
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank():
    assert greet(" ") == "Hello, world!"
    assert greet("") == "Hello, world!"


def test_greet_punctuation():
    assert greet("Hee", ".") == "Hello, Hee."


# Importing this module defines functions; direct execution calls main.
if __name__ == "__main__":
    raise SystemExit(main())
