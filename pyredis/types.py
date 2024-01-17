from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class SimpleString:
    data: str


@dataclass
class BulkString:
    data: bytes


@dataclass
class Error:
    data: str


@dataclass
class Integer:
    value: int


@dataclass
class Array(Sequence):
    data: list

    def __getitem__(self, index: int):
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)
