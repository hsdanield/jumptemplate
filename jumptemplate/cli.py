from typing import Optional, List

import typer
from rich.console import Console
from rich.table import Table

main = typer.Typer(help="Modelo de Template Jump Application")
console = Console()


@main.command("main")
def template():
    """
        Template Jump
    """
    console.print("Template Jump")


