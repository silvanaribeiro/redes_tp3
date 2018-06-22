#Parametros do Cliente : Porta Local, Endereco de Ip do servidor, porta do servidor

import socket 
import struct
import sys


def main(argv):
	HOST = None
	PORT = None
	LOCAL_PORT = None
	# Deve receber os 3 parametros para iniciar conexao
	if len(argv) == 3:
		LOCAL_PORT = argv[0]
		HOST = argv[1] # Endereco IP do Servidor 
		PORT = argv[2] # Porta em que o Servidor esta 

if __name__ == "__main__":
	main(sys.argv[1:])
