from __future__ import division
import numpy as np
import socket, argparse, sys, threading

def parseargs():
    cli_args = argparse.ArgumentParser(description="White Rose Educational Script")
    cli_args.add_argument('--host', help="IP address to connect, default is localhost", default='127.0.0.1', type=str)
    cli_args.add_argument('--port', help="Port number, default is 5000", default=5000, type=int)
    return cli_args.parse_args(sys.argv[1:])

def start_reverseshell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        command = input("Enter command: ")
        s.send(command.encode())
        if command.lower() == "exit":
            break
        response = s.recv(1024).decode()
        print(response)
    s.close()

if __name__ == "__main__":
    options = parseargs()
    print("White Rose Script initialized.")
    threading.Thread(target=start_reverseshell, args=(options.host, options.port)).start()

