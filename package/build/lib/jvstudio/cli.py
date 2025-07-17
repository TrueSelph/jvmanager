"""Jivas Studio CLI tool."""

import click

from jvstudio import __version__
from jvstudio.commands.studio import studio


@click.group()
@click.version_option(__version__, prog_name="jvcli")
def jvstudio() -> None:
    """Jivas Studio CLI tool."""
    pass  # pragma: no cover


# Register command groups
jvstudio.add_command(studio)


if __name__ == "__main__":
    jvstudio()  # pragma: no cover
