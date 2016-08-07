import ctypes


COMMAND_TYPE = {
    'PUSH': ctypes.c_bool(False),
    'POP': ctypes.c_bool(True)
}


class Command:
    def __init__(self, command_type, data=''):
        self.command_type = command_type
        self.data_length = len(str(data))
        self.data = str(data)
