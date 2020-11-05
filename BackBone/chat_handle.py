import socket
import queue
import threading

# We're going to use a tcp style system of connection. We'll use tcp

class ClientHandler(object):
    """
    class for handling client sockets
    """
    def __init__(self, address_pair=("", 8080), max_connections=1):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(address_pair)
        self._connection_thread = threading.Thread(target=ClientHandler.accept_worker, args=(self._sock,))


    # class methods
    @classmethod
    def accept_worker:
        pass