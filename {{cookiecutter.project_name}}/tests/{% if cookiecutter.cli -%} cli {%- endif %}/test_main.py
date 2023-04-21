"""Test cases for the __main__ module."""
from click.testing import CliRunner
from {{cookiecutter.package_name}} import cli


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
