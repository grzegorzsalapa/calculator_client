import socket
import time


class CommunicationError(Exception):
    def __init__(self, message):
        self.message = message


class RemoteService:

    def __init__(self, server_address: str):
        self.server_address = server_address
        self.PORT = 9010
        self.s = socket.socket()

    def connect(self):
        attempt = 0
        attempts_allowed = 3

        while True:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.server_address, self.PORT))

            except ConnectionRefusedError as e:
                self.s.close()
                attempt += 1
                print("Unable to connect to", self.server_address,
                      f"| Attempt no {attempt}/{attempts_allowed}.\n")
                if attempt == attempts_allowed:
                    raise ConnectionRefusedError(str(e))
                time.sleep(5)

    def get_result(self, expression: str):
        self.expression = expression
        try:
            expressionb = bytes(self.expression, 'utf-8')
            self.s.sendall(expressionb)
            resultb = self.s.recv(1024)
            response = str(resultb)[2:][:-1]

            return response

        except BrokenPipeError:
            self.s.close()
            self.connect()
            #raise CommunicationError(str(e))
