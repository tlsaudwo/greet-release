"""Return greetings and provide a small command-line entry point."""

import sys


def greet(name: str) -> str:
    """Return a greeting for the supplied name."""
    return f"Hello, {name}!"


def main() -> int:
    """Read the first argument, print one greeting, and report success."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet():
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
