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
    ],
)
def test_handle_command(command, expected):
    result = handle_command(command)
    assert result == expected
