"""Studio command group for deploying and interfacing with the Jivas Studio."""

from pathlib import Path

import click
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.staticfiles import StaticFiles
from jac_cloud.jaseci.security import decrypt
from uvicorn import run

from jvmanager.group import jvmanager


# @click.group()
# def studio() -> None:
#     """Group for managing Jivas Studio resources."""
#     pass  # pragma: no cover


@jvmanager.command()
@click.option("--port", default=8990, help="Port for the manager to launch on.")
def launch(port: int) -> None:
    """Launch the Jivas Manager on the specified port."""
    click.echo(f"Launching Jivas Manager on port {port}...")

    app = FastAPI(title="Jivas Manager")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    client_dir = Path(__file__).resolve().parent.parent.joinpath("manager", "client")

    app.mount(
        "/",
        StaticFiles(directory=client_dir, html=True),
        name="studio",
    )

    run(app, host="0.0.0.0", port=port)
