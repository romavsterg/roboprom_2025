import time
import serial
import socket

state = 0
coords = [
    ('paletaizer', '200', '100', '150', '0'),
    ('paletaizer', '200', '0', '150', '0'),
    ('paletaizer', '100', '0', '150', '0'),
    ('paletaizer', '200', '100', '150', '0')
]

def handle_knu_message():
    global state
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if data[-2] == '1':
            print('button pressed')
            state = 2

def send_coords(sock, coords):
    sock.sendto(':'.join(coords).encode('utf-8'), ('localhost', 12346))
    
def move(sock, i):
    global state

    print(f'sending pose x: {coords[i][1]} y: {coords[i][2]} z: {coords[i][3]} v: {coords[i][4]}')
    send_coords(sock, coords[i])

    state = 1

    print(f'got msg from manipulator:\n{get_res(sock)}')

def get_res(sock):
    data, addr = sock.recvfrom(4096)
    return data.decode('utf-8')


try:
    ser = serial.Serial('COM8', 9600, timeout=1)
except Exception as e:
    print(e)
    exit()

def send_state():
    global state
    
    ser.write((str(state) + '\n').encode('utf-8'))


try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('localhost', 12345))            
        i = 0

        while True:
            handle_knu_message()
            send_state()

            if state == 2:
                i = (i + 1) % 4
                move(sock, i)
            
            if i == 0:
                state = 0

            time.sleep(0.5)
except KeyboardInterrupt:
    ser.close()
