from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class OSFunction:
    name: str            # The name of the function, as its class name.
    description: str     # Describe what this functionality is, describe its arguments.
    arguments_list: Dict # Describe name of arguments (from description)
                         # and types stored as strings (e.g. "bool").
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data.get('name'),
            description = data.get('description'),
            arguments_list = data.get('arguments_list')
        )


# Abstract class for all scriptlets.
class OSScriptlet(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def execute(self) -> bool:
        pass
