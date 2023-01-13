from unittest.mock import Mock, patch
from calculator_client.TCP_client import get_result, CommunicationError
from calculator_client.calculate import calculate
import socket


def test_1(mocker):
    def mock_recv(self, x):
        return b'6'


    mocker.patch('calculator_client.TCP_client.socket.socket')
    mocker.patch('calculator_client.TCP_client.socket.socket.connect')
    mocker.patch('calculator_client.TCP_client.socket.socket.sendall')
    mocker.patch('calculator_client.TCP_client.socket.socket.recv', mock_recv)

    assert calculate('2+2*2') == '6'

#
def test_2():
    s = socket.socket()
    s.connect = Mock()
    s.sendall = Mock()
    s.recv = Mock(return_value=b'6')

    assert calculate('2+2*2') == '6'


socket_mock = Mock()
socket_mock.connect.return_value = None
socket_mock.sendall.return_value = None
socket_mock.recv().return_value = 0

@patch('calculator_client.TCP_client.socket.socket')
def test_3(socket_mock):
    assert calculate('2+2*2') == '6'

@patch('calculator_client.TCP_client.socket.socket')
def test_4(socket_mock):
    calculate('2+2*2')
    assert socket_mock.sendall.assert_called()
    assert socket_mock.sendall.assert_called_with(b'2+2*2')
