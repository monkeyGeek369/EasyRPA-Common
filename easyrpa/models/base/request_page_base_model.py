from dataclasses import dataclass
from easyrpa.models.base.sort_base_model import SortBaseModel


@dataclass
class RequestPageBaseModel:
    page: int
    page_size: int
    sorts: list[SortBaseModel]