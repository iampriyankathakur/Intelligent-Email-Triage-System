from rich.console import Console
from rich.table import Table

console = Console()

def display_results(results):

    table = Table(title="📨 Email Analysis")

    table.add_column("Field")
    table.add_column("Value")

    for key, value in results.items():

        if isinstance(value, list):
            value = ", ".join(value)

        table.add_row(key, str(value))

    console.print(table)
