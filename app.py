from flask import Flask, render_template, request
import os

app = Flask(__name__)

# get the ip address of the connection
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("Connected")
    return s.getsockname()[0]


if __name__ == '__main__':
    ip_address_var = get_ip_address()
    app.run(host=ip_address_var, port=5012)
    app.debug = True