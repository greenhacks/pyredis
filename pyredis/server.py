"""Build a TCP-based server"""

import socket


class Server:
    """Sits in a loop listening for connections"""

    def __init__(self, port):
        self.port = port
        self._running = False

    def run(self):
        self._running = True

        # create a socket using AF_INET (addressable through an IP address and port number)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            self._server_socket = server_socket
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # TODO: Bind to an address and listen for incoming connections

            while self._running:
                # TODO: Accepting connection

                # TODO: Handle client connection

                pass

    def stop(self):
        self._running = False

    def handle_client_connection(client_socket):
        try:
            while True:
                data = client_socket.recv(RECV_SIZE)

                if not data:
                    break

                # TODO: do something with the data

        finally:
            client_socket.close()
