"""Build a TCP-based server"""

import socket
import threading

from pyredis.commands import handle_command
from pyredis.datastore import DataStore
from pyredis.protocol import encode_message, extract_frame_from_buffer

RECV_SIZE = 2048


def handle_client_connection(client_socket, datastore):
    buffer = bytearray()

    try:
        while True:
            data = client_socket.recv(RECV_SIZE)

            if not data:
                break

            # do something with the data
            buffer.extend(data)

            frame, frame_size = extract_frame_from_buffer(buffer)

            if frame:
                buffer = buffer[frame_size:]
                result = handle_command(frame)
                client_socket.send(encode_message(result))

    finally:
        client_socket.close()


class Server:
    """Sits in a loop listening for connections"""

    def __init__(self, port):
        self.port = port
        self._running = False
        self._datastore = DataStore()

    def run(self):
        self._running = True

        # create a socket using AF_INET (addressable through an IP address and port number)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            self._server_socket = server_socket
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind to an address and listen for incoming connections
            server_address = ("localhost", self.port)
            server_socket.bind(server_address)
            server_socket.listen()

            while self._running:
                # Accept and handle client connection
                connection, _ = server_socket.accept()
                # handle_client_connection(connection, self._datastore)

                client_handler = threading.Thread(
                    target=handle_client_connection, args=(connection, self._datastore)
                )

                client_handler.start()

    def stop(self):
        self._running = False
