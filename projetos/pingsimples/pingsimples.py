#Importar a biblioteca os
import os

print('#' * 40)
#criar a variável que irá receber o ip ou host a ser "pingado"
ip_ou_host = input('Digite o Ip ou Host a ser verificado: ')

#Chamar a biblioteca com método que contém informações do sistema.
os.system(f'ping -n 6 {ip_ou_host}')
