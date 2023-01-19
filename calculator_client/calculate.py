from .TCP_client import RemoteService, CommunicationError


class CalculationError(Exception):
    def __init__(self, message: str):
        self.message = message


class RemoteCalculationError(Exception):
    pass


class RemoteCalculator:

    def __init__(self, server_address):
        self.server_address = server_address
        self.remote_service = RemoteService(self.server_address)
        self.connection = None

    def connect(self):
        try:
            self.connection = self.remote_service.connect()

        except ConnectionRefusedError as e:

            raise CommunicationError(str(e))

    def _check_if_error_returned(self, str_to_check):
        try:
            float(str_to_check)

        except Exception:
            error_message = str_to_check
            raise RemoteCalculationError(error_message)

    def calculate(self, expression: str):
        try:
            result = self.remote_service.get_result(expression)
            self._check_if_error_returned(result)

            return result

        except RemoteCalculationError as e:

            raise CalculationError(str(e))

        except CommunicationError as e:

            raise CommunicationError(str(e))
