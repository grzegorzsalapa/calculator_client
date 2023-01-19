import socket
import time


class CommunicationError(Exception):
    def __init__(self, message):
        self.message = message


PORT = 9010

def connect_socket(server_address):
    attempt = 0
    attempts_allowed = 3
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_address, PORT))

            return s

        except ConnectionRefusedError as e:
            s.close()
            attempt += 1
            print("Unable to connect to", server_address, f"| Attempt no {attempt}/{attempts_allowed}.\n")
            if attempt == attempts_allowed:
                raise ConnectionRefusedError(str(e))
            time.sleep(5)


def get_result(expression: str, s):

    try:
        expressionb = bytes(expression, 'utf-8')
        s.sendall(expressionb)
        resultb = s.recv(1024)
        response = str(resultb)[2:][:-1]

        return response

    except BrokenPipeError as e:
        s.close()
        raise CommunicationError(str(e))
