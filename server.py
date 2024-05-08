import concurrent.futures
import random
import socket
import threading
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.143.11', 9999))

target = {'T0': 25.0, 'T1': 30.0, 'T2': 27.0, 'T3': 32.0, 'CPU': 10, 'RAM': 15, 'ROM': 12}
targetLock = threading.Lock()


def temperatureIncrement(currentValue):
    return round(currentValue + random.random(), 1)


def temperatureDecrement(currentValue):
    return round(currentValue - random.random(), 1)


def hardwareDataIncrement(currentValue):
    return currentValue + 1


def hardwareDataDecrement(currentValue):
    return currentValue - 1


def runChangeData():
    t0Switcher = True
    t1Switcher = True
    t2Switcher = True
    t3Switcher = True
    cpuSwitcher = True
    ramSwitcher = True
    romSwitcher = True

    while True:
        for key, value in target.items():
            if key == 'T0':
                if t0Switcher:
                    newValue = temperatureIncrement(value)
                    if newValue < 110:
                        target[key] = newValue
                    else:
                        target[key] = temperatureDecrement(value)
                        t0Switcher = not t0Switcher
                else:
                    newValue = temperatureDecrement(value)
                    if newValue > -10:
                        target[key] = newValue
                    else:
                        target[key] = temperatureIncrement(value)
                        t0Switcher = not t0Switcher
            elif key == 'T1':
                if t1Switcher:
                    newValue = temperatureIncrement(value)
                    if newValue < 110:
                        target[key] = newValue
                    else:
                        target[key] = temperatureDecrement(value)
                        t1Switcher = not t1Switcher
                else:
                    newValue = temperatureDecrement(value)
                    if newValue > -10:
                        target[key] = newValue
                    else:
                        target[key] = temperatureIncrement(value)
                        t1Switcher = not t1Switcher
            elif key == 'T2':
                if t2Switcher:
                    newValue = temperatureIncrement(value)
                    if newValue < 110:
                        target[key] = newValue
                    else:
                        target[key] = temperatureDecrement(value)
                        t2Switcher = not t2Switcher
                else:
                    newValue = temperatureDecrement(value)
                    if newValue > -10:
                        target[key] = newValue
                    else:
                        target[key] = temperatureIncrement(value)
                        t2Switcher = not t2Switcher
            elif key == 'T3':
                if t3Switcher:
                    newValue = temperatureIncrement(value)
                    if newValue < 110:
                        target[key] = newValue
                    else:
                        target[key] = temperatureDecrement(value)
                        t3Switcher = not t3Switcher
                else:
                    newValue = temperatureDecrement(value)
                    if newValue > -10:
                        target[key] = newValue
                    else:
                        target[key] = temperatureIncrement(value)
                        t3Switcher = not t3Switcher
            elif key == 'CPU':
                if cpuSwitcher:
                    newValue = hardwareDataIncrement(value)
                    if newValue <= 100:
                        target[key] = newValue
                    else:
                        target[key] = hardwareDataDecrement(value)
                        cpuSwitcher = not cpuSwitcher
                else:
                    newValue = hardwareDataDecrement(value)
                    if newValue >= 0:
                        target[key] = newValue
                    else:
                        target[key] = hardwareDataIncrement(value)
                        cpuSwitcher = not cpuSwitcher
            elif key == 'RAM':
                if ramSwitcher:
                    newValue = hardwareDataIncrement(value)
                    if newValue <= 100:
                        target[key] = newValue
                    else:
                        ramSwitcher = not ramSwitcher
                else:
                    newValue = hardwareDataDecrement(value)
                    if newValue >= 0:
                        target[key] = newValue
                    else:
                        target[key] = hardwareDataIncrement(value)
                        ramSwitcher = not ramSwitcher
            elif key == 'ROM':
                if romSwitcher:
                    newValue = hardwareDataIncrement(value)
                    if newValue <= 100:
                        target[key] = newValue
                    else:
                        romSwitcher = not romSwitcher
                else:
                    newValue = hardwareDataDecrement(value)
                    if newValue >= 0:
                        target[key] = newValue
                    else:
                        target[key] = hardwareDataIncrement(value)
                        romSwitcher = not romSwitcher

        time.sleep(1)


def runClimateConnection():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f'REQUEST from {addr}: {data.decode()} ')
            data = str(data.decode()).upper()
            if data in list(target.keys()):
                print(f'RESPONSE to {addr}: {target[data]}\n')
                sock.sendto(str(target[data]).encode("utf-8"), addr)
            else:
                sock.sendto('Ошибка запроса!'.encode("utf-8"), addr)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(runClimateConnection)
        executor.submit(runChangeData)
        print('Server is running')
