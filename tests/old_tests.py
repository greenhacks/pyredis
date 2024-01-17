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


def test_read_frame_null_value():
    "Handle Null values witha  special variation of Bulk Strings"

    buffer = b"$-1\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == None
    assert frame_size == None


def test_read_array_ping():
    "Handle arrays"

    buffer = b"*1\r\n$4\r\nping\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_array_echo():
    "Handle arrays"

    buffer = b"*2\r\n$4\r\necho\r\nhello world\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_array_get():
    "Handle arrays"

    buffer = b"*2\r\n$4\r\nget\r\nkey\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_simple_string():
    "Handle simple string"

    buffer = b"+OK\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_error():
    "Handle error"

    buffer = b"-Error message\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == None
    assert frame_size == None


def test_read_bulk_string():
    "Handle bulk string"

    buffer = b"$0\r\n\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_handle_more_simple_strings():
    "Handle simple string"

    buffer = b"+hello world\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_handle_integer():
    "Handle integer"

    buffer = b":5\r\n"
    frame, frame_size = extract_frame_from_buffer(buffer)
    assert frame == 5
    assert frame_size == 5
