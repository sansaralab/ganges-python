import ctypes


COMMAND_TYPE = {
    'PUSH': ctypes.c_uint8(0),
    'POP': ctypes.c_uint8(1)
}


class Command:
    def __init__(self, command_type, data=''):
        self.command_type = command_type
        self.data_length = ctypes.c_uint32(len(str(data)))
        self.data = str(data)
