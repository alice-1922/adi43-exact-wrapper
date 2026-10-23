"""A minimal greeting CLI, version 1.0.0."""

import sys

__version__ = "1.0.0"


def greeting(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greeting(name))
