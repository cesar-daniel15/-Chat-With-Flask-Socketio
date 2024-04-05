import socket

server_running = False  # Variável para indicar se o servidor está ligado ou desligado

def start_server():
    global server_running
    # Cria o socket
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o host e a porta
    host = 'localhost'
    porta = 5000

    # Liga o socket ao host e à porta
    servidor.bind((host, porta))

    # Escuta por conexões
    servidor.listen(1)
    print("Servidor esperando conexões em", host, ":", porta)
    server_running = True  # Define a variável como True quando o servidor começar a ser executado

    while True:
        # Aceita uma conexão
        conexao, endereco = servidor.accept()
        print("Conectado por", endereco)

        try:
            while True:
                # Recebe dados do cliente
                dados = conexao.recv(1024)
                if not dados:
                    break
                print("Recebido do cliente:", dados.decode())

                # Envia dados de volta ao cliente
                resposta = input("Digite uma resposta: ")
                conexao.send(resposta.encode())
        finally:
            conexao.close()

if __name__ == "__main__":
    start_server()
