import socket

def sockets(ip,port):
    try:
        host = ip
        port = port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((f'{host}', port))
        if result == 0:
            s.close()
            return "open"
        else:
            s.close()
            return "closed"

    except KeyboardInterrupt:
        print("Error", "\nExiting.")


    except socket.gaierror:
        print("Error", "IP cannot be resolved.")


    except socket.error:
        print("Error", "Connection Problem.")
