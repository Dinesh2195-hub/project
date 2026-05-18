"""Example Python module using f-strings."""

from datetime import datetime
from typing import Dict


def greet_user(name: str) -> str:
    """Return a personalized greeting using an f-string."""
    return f"Hello, {name}! Welcome to the f_string_demo project."


def format_summary(values: Dict[str, float]) -> str:
    """Return a formatted summary of numeric values using f-strings."""
    total = sum(values.values())
    lines = [f"- {label}: {amount:.2f}" for label, amount in values.items()]
    return (
        f"Summary generated at {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        f"Total: {total:.2f}\n"
        f"Details:\n" + "\n".join(lines)
    )


def main() -> None:
    name = "Developer"
    values = {"apples": 3.5, "oranges": 4.25, "bananas": 2.75}

    print(greet_user(name))
    print()
    print(format_summary(values))


if __name__ == "__main__":
    main()
