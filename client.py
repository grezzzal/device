import time
import socket

request = input('Введите  ключ: ').upper()

try:
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(request, encoding='utf-8'), ('192.168.1.108', 55030))
        data, addr = sock.recvfrom(1024)
        print('Температура ' + request + ': ' + data.decode('utf-8'))
        print("Подождите")
        time.sleep(3)
except KeyboardInterrupt:
    print("Поток остановлен пользователем.")

