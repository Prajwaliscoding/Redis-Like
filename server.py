import socket
import json
import threading
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
                parts = data.split()    
                if not parts:
                    continue

                elif parts[0].upper() == "SET" and len(parts) == 3:
                    kv.set(parts[1],parts[2])
                    conn.sendall(b"OK")
                elif parts[0].upper() == "GET" and len(parts) == 2:
                    result = kv.get(parts[1])
                    if result is None:
                        conn.sendall(b"None")
                    else:
                        conn.sendall(json.dumps(result).encode())
                else:
                    conn.sendall(b"ERROR...Unknown command.")
            except Exception as e:
                conn.sendall(str(e).encode())


def main():
    s=socket.socket()
    s.bind((SERVER,PORT))

    s.listen()
    print("Server is listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=[conn])
        thread.start()
        
if __name__=="__main__":
    main()
