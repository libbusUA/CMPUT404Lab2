import socket

bytes_to_read = 4096

def get(host, port):

    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)

    s.shutdown(socket.SHUT_WR)

    result = s.recv(bytes_to_read)

    while(len(result) > 0):
            print(result)
            result = s.recv(bytes_to_read)
    s.close()


    
get('www.google.com', 80)
