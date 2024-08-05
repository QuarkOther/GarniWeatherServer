from common.config_load import SERVER_IP, SERVER_PORT
from socketDataGet.getSocketData import socket_data_receive


def __main__():
    socket_data_receive(SERVER_IP, SERVER_PORT)


if __name__ == "__main__":
    __main__()
