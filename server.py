import socket, random

target = {'T1' : '30', 'T2' : '30', 'T3' : '30', 'CPU' : '10', 'RAM' : '10', 'ROM' : '10'}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.108', 55030))
print('Server is running')
while True:
    data, addr = sock.recvfrom(1024)
    print(f'Received a message from {addr}:{data.decode()} ')
    data = str(data.upper().decode("utf-8"))
    if target.get(data):
        sock.sendto(target[data].encode("utf-8"), addr)
    else:
        sock.sendto('Error'.encode("utf-8"), addr)
conn.close()
