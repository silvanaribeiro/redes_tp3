#Parametros do Cliente : Porta Local, Endereco de Ip do servidor, porta do servidor
import select
import socket 
import struct
import sys
from sys import stdin


def main(argv):
	HOST = None
	PORT = None
	LOCAL_PORT = None
	# Deve receber os 3 parametros para iniciar conexao
	if len(argv) >= 3:
		LOCAL_PORT = argv[0]
		HOST = argv[1] # Endereco IP do Servidor 
		PORT = argv[2] # Porta em que o Servidor esta
		TEXT = argv[3] # Teste no windows
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server.bind(('',int(LOCAL_PORT))) 
		#input = [server,sys.stdin] #SO FUNCIONA NO LINUX, MAS EH O QUE DEVE SER MANDADO PRA CORRECAO
		input = [server]
		running = 1
		send_message(HOST, PORT, TEXT)
		while running:
			inputready,outputready,exceptready = select.select(input,[],[])
			print("entrou running")
			for s in inputready+[sys.stdin]: # PARA WINDOWS
				print("entrou for")
			#for s in inputready: # PARA LINUX
				if s == server:
					# handle the server socket
					client, address = server.accept()
					input.append(client)
				elif s == sys.stdin:
					print("entrou stdin")
					# handle standard input
					junk = input()
					print(junk)
					running = 0
				else:
					# handle all other sockets
					print("entrou outros sockets")
					data = s.recv(size).decode('ascii')
					print(data)
					if data:
						s.send(data)
					else:
						s.close()
						input.remove(s)
		server.close() 

def send_message(HOST, PORT, message):
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = (HOST, int(PORT))

	udp.sendto(message.encode('ascii'), dest)
	udp.close()		

if __name__ == "__main__":
	main(sys.argv[1:])
