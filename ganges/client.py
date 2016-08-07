class Client:
    _hostname = None
    _port = None

    def __init__(self, hostname, port):
        self._hostname = hostname
        self._port = port

    def send(self, command):
        return 'Not implemented'
