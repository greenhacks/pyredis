"""Tests for TCP protocol handler"""
import pytest
from protocol import extract_frame_from_buffer, SimpleString


@pytest.mark.parametrize(
    "buffer, expected",
    [
        (b"+Par", (None, 0)),
        (b"+OK\r\n", (SimpleString("OK"), 5)),
        (b"+OK\r\n+Next", (SimpleString("OK"), 5)),
    ],
)
def test_read_frame_simple_string(buffer, expected):
    """Using Pytest's parametrize"""
    actual = extract_frame_from_buffer(buffer)
    assert actual == expected


def test_read_frame_simple_string_incomplete_frame():
    """Handle incomplete frame"""

    buffer = b"+Par"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == None
    assert frame_size == 0


def test_read_frame_simple_string_complete_frame():
    """Handle complete frame"""

    buffer = b"+OK\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_frame_simple_string_extra_data():
    """Handle extra data"""

    buffer = b"+OK\r\n+Next"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5
