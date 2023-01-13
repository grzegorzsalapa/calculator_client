from unittest.mock import MagicMock, patch
from calculator_client.calculate import calculate


def _set_up_mocked_calculator_socket(recv_value=None):
    socket_instance = MagicMock(name="SocketInstance")
    socket_instance.recv = MagicMock(return_value=recv_value)

    socket_context = MagicMock(name="SocketContext")
    socket_context.__enter__ = MagicMock(return_value=socket_instance)

    socket_mock = MagicMock()
    socket_mock.socket = MagicMock(name="SocketModule", return_value=socket_context)

    return socket_mock


def test_that_received_result_on_socket_is_passed_properly_as_a_result_to_calculate():
    socket_mock = _set_up_mocked_calculator_socket(recv_value=b'6')

    with patch('calculator_client.TCP_client.socket', new=socket_mock):
        assert calculate('2+2*2') == '6'
