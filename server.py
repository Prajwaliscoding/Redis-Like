import socket
import json
from key_value_store import KVStore

kv = KVStore()
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())

def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            try:
                command = json.loads(data)
                if command["op"] == "set":
                    kv.set(command["key"],command["value"])
                    conn.sendall(b"OK")
                elif command["op"] == "get":
                    value = kv.get(command["key"])
                    conn.sendall(json.dumps(value).encode())
            except Exception as e:
                conn.sendall(str(e).encode())


def main():
    s=socket.socket()
    s.bind((SERVER,PORT))

    s.listen()
    print("Server is listening...")
    while True:
        conn, addr = s.accept()
        print("Client added with ",addr)
        handle_client(conn)

if __name__=="__main__":
    main()