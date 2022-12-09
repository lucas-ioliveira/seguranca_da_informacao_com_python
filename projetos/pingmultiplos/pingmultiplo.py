import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip', ip)
        print('-' * 40)
        #os.system('ping ' + ip)
        os.system(f'ping -n 2 {ip}')
        print('-' * 40)
        time.sleep(5)
        