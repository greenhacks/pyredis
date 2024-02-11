import pytest
from pyredis.protocol import extract_frame_from_buffer, encode_message
from pyredis.types import Array, BulkString, Integer, Error, SimpleString


@pytest.mark.parametrize(
    "command, expected",
    [
        # Echo Tests
        (
            Array([BulkString(b"ECHO")]),
            Error("ERR wrong number of arguments for 'echo' command"),
        ),
        {Array([BulkString(b"echo"), BulkString(b"Hello")]), BulkString("Hello")},
        {
            Array([BulkString(b"echo"), BulkString(b"Hello"), BulkString(b"World")]),
            Error("ERR wrong number of arguments for 'echo' command"),
        },
        # Ping Tests
        (Array([BulkString(b"ping")]), SimpleString("PONG")),
        (Array([BulkString(b"ping"), BulkString(b"Hello")]), BulkString("Hello")),
        # SET Tests
        (
            Array([BulkString(b"set")]),
            Error("ERR wrong number of arguments for 'set' command"),
        ),
        (
            Array([BulkString(b"set"), SimpleString(b"key")]),
            Error("ERR wrong number of arguments for 'set command"),
        ),
        (
            Array([BulkString(b"set"), SimpleString(b"key"), SimpleString(b"value")]),
            SimpleString("OK"),
        ),
        # GET Tests
        (
            Array([BulkString(b"get")]),
            Error("ERR wrong number of arguments for 'set' command"),
        ),
        (
            Array([BulkString(b"get"), SimpleString(b"key")]),
            Error("ERR wrong number of arguments for 'set command"),
        ),
        (
            Array([BulkString(b"get"), SimpleString(b"key"), SimpleString(b"value")]),
            SimpleString("OK"),
        ),
    ],
)
def test_handle_command(command, expected):
    result = handle_command(command)
    assert result == expected


def test_set_and_get_item():
    """Testing the DataStore"""
    ds = DataStore()
    ds["key"] = 1
    assert ds["key"] == 1
