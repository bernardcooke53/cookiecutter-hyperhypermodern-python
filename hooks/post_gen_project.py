#!/usr/bin/env python

import json
import subprocess
from pathlib import Path


def reindent_cookiecutter_json() -> None:
    """Indent .cookiecutter.json using four spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=4)
        io.write("\n")


def generate_poetry_lockfile() -> None:
    """
    Generate poetry.lock
    """
    subprocess.check_call(["poetry", "lock"])


if __name__ == "__main__":
    reindent_cookiecutter_json()
    generate_poetry_lockfile()
