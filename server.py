import socket

target = {'T1' : '30', 'T2' : '30', 'T3' : '30', 'CPU' : '10', 'RAM' : '10', 'ROM' : '10'}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55030))
sock.listen(1)
print('Server is running')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    data = str(data.upper().decode("utf-8"))
    if target.get(data):
        conn.send(target[data].encode())
    else:
        conn.send('Error'.encode())
conn.close() 
