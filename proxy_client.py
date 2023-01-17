import socket

bytes_to_read = 4096

def get(host, port):

    request = b"GET /HTTP/1.1\nwww.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((host,port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)

        print("waiting for response!")

        chunk = s.recv(bytes_to_read)
        result = b'' + chunk 
        while( len(chunk) > 0):
            chunk = s.recv(bytes_to_read)
            result += chunk

        s.close()

    return result

print(get("127.0.0.1", 8080))
