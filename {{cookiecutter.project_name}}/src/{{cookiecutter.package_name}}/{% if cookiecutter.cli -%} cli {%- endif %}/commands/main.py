"""
Command-line interface.
"""

{% if cookiecutter.cli_logging -%}
import logging
{% endif %}
from rich.console import Console
{% if cookiecutter.cli_logging -%}
from rich.logging import RichHandler
{% endif %}
import click

from {{ cookiecutter.package_name }} import __version__

DEFAULT_CONFIG_FILE = "pyproject.toml"
{% if cookiecutter.cli_logging -%}
FORMAT = "[%(name)s] %(levelname)s %(module)s:%(funcName)s: %(message)"
DATEFMT = "[%X]"
{%- endif %}


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(
    version=__version__,
    prog_name="{{ cookiecutter.project_name }}",
    help="Show the version of {{ cookiecutter.project_name }} and exit"
)
@click.option(
    "-c",
    "--config",
    "config_file",
    default=DEFAULT_CONFIG_FILE,
    help="Specify a configuration file for {{ cookiecutter.project_name }} to use",
    type=click.Path(exists=True),
)
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    help="Set logging verbosity",
    default=0,
    count=True,
    show_default=True,
    type=click.IntRange(0, 2, clamp=True),
)
@click.pass_context
def main(
    ctx: click.Context, config_file: str = DEFAULT_CONFIG_FILE, verbosity: int = 0
) -> None:
    """{{cookiecutter.friendly_name}}."""

    console = Console(stderr=True)

    {% if cookiecutter.cli_logging -%}
    log_level = [logging.WARNING, logging.INFO, logging.DEBUG][verbosity]
    logging.basicConfig(
        level=log_level,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[
            RichHandler(
                console=console, rich_tracebacks=True, tracebacks_suppress=[click]
            ),
        ],
    )

    log = logging.getLogger(__name__)
    {%- endif %}
