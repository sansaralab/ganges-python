from .types import Command, COMMAND_TYPE
from .client import Client


class Ganges:
    _hostname = None
    _port = None

    def __init__(self, hostname, port):
        self._hostname = hostname
        self._port = port

    def push(self, data):
        client = Client(self._hostname, self._port)
        command = Command(COMMAND_TYPE['PUSH'], data)
        return client.send(command)

    def pop(self):
        client = Client(self._hostname, self._port)
        command = Command(COMMAND_TYPE['POP'])
        return client.send(command)
