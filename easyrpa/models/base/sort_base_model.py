from dataclasses import dataclass


@dataclass
class SortBaseModel:
    prop: str
    order: str