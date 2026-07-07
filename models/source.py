from dataclasses import dataclass


@dataclass
class Source:

    title: str = ""

    url: str = ""

    source_type: str = ""

    priority: int = 0

    text: str = ""

    success: bool = False