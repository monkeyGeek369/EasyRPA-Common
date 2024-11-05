from dataclasses import dataclass
from easyrpa.models.base.sort_base_model import SortBaseModel


@dataclass
class ResponsePageBaseModel:
    total: int
    data: any
    sorts: list[SortBaseModel]