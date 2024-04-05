import socket

# Conecta-se ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))

while True:
    # Recebe dados do servidor
    dados = cliente.recv(1024)
    print("Mensagem do servidor:", dados.decode())

    # Envia mensagem para o servidor
    mensagem = input("Digite sua mensagem: ")
    cliente.send(mensagem.encode())

cliente.close()
