import socket
import time

i = 0

def send_res(sock, coords):
    res = f"{coords[0]} manipulator got in pose x: {coords[1]} y: {coords[2]} z: {coords[3]} v: {coords[4]}"

    sock.sendto(res.encode('utf-8'), ('localhost', 12345))


def handle_req(sock):
    data, _ = sock.recvfrom(4096)

    coords = data.decode('utf-8').split(':')

    print(f'got pose x: {coords[1]} y: {coords[2]} z: {coords[3]} v: {coords[4]}')
    print('Moving...')

    time.sleep(5)

    print('Got in position')

    send_res(sock, coords)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('localhost', 12346))

    while True:
        handle_req(sock)
        