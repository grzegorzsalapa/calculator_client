from .TCP_client import get_result, CommunicationError

class CalculationError(Exception):
    def __init__(self, message: str):
        self.message = message


def calculate(expression: str):
    try:
        result = get_result(expression)

        return result

    except CommunicationError as e:

        raise CalculationError(str(e))

