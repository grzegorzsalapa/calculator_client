import socket
import time


class RemoteCalculationError(Exception):
    pass


class RemoteService:

    def __init__(self, server_address: str):
        self.server_address = server_address
        self.PORT = 9010
        self.soc = None
        self.timeout = 5

    def connect(self):
        attempts = 0
        attempts_max = 3

        while True:
            try:
                self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print(f"    Connecting to remote calculator on {self.server_address}...\n")
                self.soc.settimeout(self.timeout)
                self.soc.connect((self.server_address, self.PORT))
                print(f"\r    Successfully connected to remote calculator on {self.server_address}.\n")
                break

            except ConnectionRefusedError as e:
                self.soc.close()
                attempts += 1
                if attempts == attempts_max:
                    print('')
                    self.soc = None
                    raise ConnectionError(str(e))
                #print("    Please wait...\n")
                time.sleep(5)
                print(str(e), "\n")

    def get_result(self, expression: str):
        expr = expression
        while True:
            try:
                expr_b = bytes(expr, 'utf-8')
                self.soc.sendall(expr_b)
                result_b = self.soc.recv(1024)
                while not result_b:
                    raise BrokenPipeError
                response = str(result_b)[2:][:-1]
                _check_if_error_returned(response)

                return response

            except BrokenPipeError:
                self.soc.close()
                print("\n    Connection lost. Attempting to reconnect.\n")
                self.connect()


def _check_if_error_returned(str_to_check):
    try:
        float(str_to_check)

    except ValueError:
        error_message = str_to_check
        raise RemoteCalculationError(error_message)
