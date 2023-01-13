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
    # s.connect = Mock()
    # s.sendall = Mock()
    s.recv = Mock(return_value=b'6')

    assert calculate('2+2*2') == '6'