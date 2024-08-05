import socket

BUFFER_SIZE = 1024

def socket_data_receive(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)  # become a server socket, maximum 5 connections

    while True:
        connection, address = server_socket.accept()
        buf = connection.recv(BUFFER_SIZE)
        print(f"Connection: {connection}")
        if len(buf) > 0:
            print(buf)
