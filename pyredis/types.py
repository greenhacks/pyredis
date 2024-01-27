from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class SimpleString:
    data: str

    def as_str(self):
        return self.data

    def resp_encode(self):
        return f"+{self.data}\r\n".encode()


@dataclass
class BulkString:
    data: bytes

    def as_str(self):
        return self.data.decode()

    def resp_encode(self):
        if self.data is None:
            return b"$-1\r\n"

        return f"${len(self.data)}\r\n{self.data}\r\n".encode()

    def file_encode(self):
        if self.data is None:
            return b"$-1\r\n"
        return f"${len(self.data)}\r\n{self.data.decode(())}\r\n".encode()


@dataclass
class Error:
    data: str

    def as_str(self):
        return self.data

    def resp_encode(self):
        return f"-{self.data}\r\n".encode()


@dataclass
class Integer:
    value: int

    def as_str(self):
        return self.data

    def resp_encode(self):
        return f":{self.data}\r\n".encode()


@dataclass
class Array(Sequence):
    data: list

    def resp_encode(self):
        if self.data is None:
            return b"*-1\r\n"

        encoded_sub_messages = [f"*{len(self.data)}\r\n".encode()]

        for msg in self.data:
            encoded_sub_messages.append(msg.resp._encode())

        return b"".join(encoded_sub_messages)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)
