import socket

# IP = socket.gethostbyname(socket.gethostname())
IP = "192.168.0.96"
PORT = 4455
ADDR = (IP, PORT)
FORMAT = 'utf-8'
SIZE = 5096
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    file = open("/home/scientist/Documents/vertive_app/Kivy_demo_all/demo.kv", "r")
    data = file.read()

    client.send("demo.kv".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"server recived  {msg}")

    client.send(data.encode(FORMAT))

    msg = client.recv(SIZE).decode(FORMAT)
    print(f"server recived  {msg}")

    file.close()
    client.close()


if __name__ =="__main__":
    main()