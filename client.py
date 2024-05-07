import threading
import time
import socket

request = input('Введите  ключ: ').upper()

try:
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 55030))
        sock.send(bytes(request, encoding='utf-8'))
        data = sock.recv(1024)
        print('Температура ' + request + ': ' + data.decode('utf-8'))
        print("Подождите")
        time.sleep(3)
except KeyboardInterrupt:
    print("Поток остановлен пользователем.")

