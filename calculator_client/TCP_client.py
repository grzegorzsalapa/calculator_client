import socket


class CommunicationError(Exception):
    def __init__(self, message):
        self.message = message


PORT = 9010

def connect_socket(server_address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_address, PORT))

        return s

    except Exception as e:
        s.close()
        raise CommunicationError(str(e))


def get_result(expression: str, s):
    try:
        expressionb = bytes(expression, 'utf-8')
        s.sendall(expressionb)
        resultb = s.recv(1024)
        response = str(resultb)[2:][:-1]

        return response

    except Exception as e:
        s.close()
        raise CommunicationError(str(e))
