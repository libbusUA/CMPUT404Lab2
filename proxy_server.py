import socket

from threading import Thread

bytes_to_read = 4096

proxy_server_host = "127.0.0.1"

proxy_server_port = 8080


def send_request(host, port, request_data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

        data = client_socket.recv(bytes_to_read)
        result = b''+ data

        while( len(data) > 0):
            data = client_socket.recv(bytes_to_read)
            result += data

        return result

    return 

def handle_connection(conn, addr):
    
    with conn:
        print(f"Connected by: {addr}")
        request = b''
        while True:
            data = conn.recv(bytes_to_read)
            if not data:
                break
            print(data)
            request += data

            response = send_request("www.google.com", 80, request)

            conn.sendall(response)


    return 

def start_server():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
        server_socket.bind((proxy_server_host, proxy_server_port))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        conn, addr = server_socket.accept()

        handle_connection(conn, addr)

    return 


def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((proxy_server_host, proxy_server_port))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target = handle_connection, args=(conn, addr))

            thread.run()





#start_server()
start_threaded_server()
