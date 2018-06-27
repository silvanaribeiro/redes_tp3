#Parametros do Servidor : porta do servidor
import socket
import struct
import sys, getopt, threading

def main(argv):
	HOST = None
	dict_client_tags = {}
	if len(argv) == 1:
			PORT = argv[0] # Porta em que o servidor esta 
			HOST = '' # Endereco IP do Servidor  
			start_listening(HOST, PORT, dict_client_tags)
			        
def is_message_valid(message):
	valid_chars = ",.?!:;+-*/=@#$%()[]{}1234567890abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ "
	for c in message:
		if c not in valid_chars:
			print('nao eh valida')
			return False
	return True
	
def decode_message(message):
	final_result = list()
	delimiters = ["+", "-", "#"]
	word = ""
	count_delimiters = 0
	for letter in message:
		if letter not in delimiters:
			word += letter
		elif letter in delimiters and count_delimiters is 0:
			word = letter
			count_delimiters = 1
		elif letter in delimiters and count_delimiters is 1:
			final_result.append(word)
			word = letter
			count_delimiters = 1
	final_result.append(word)
	return final_result
	
def add_tag_to_client(ip_port, tag, dict_client_tags):
	tag = tag[1:]
	if ip_port in dict_client_tags:
		temp_list = dict_client_tags[ip_port]
		if tag not in temp_list:
			temp_list.append(tag)
			dict_client_tags[ip_port] = temp_list
	else:
		dict_client_tags[ip_port] = [tag]
	return dict_client_tags
	
def remove_tag_from_client(ip_port, tag, dict_client_tags):
	tag = tag[1:]
	if ip_port in dict_client_tags:
		temp_list = dict_client_tags[ip_port]
		temp_list.remove(tag)
		dict_client_tags[ip_port] = temp_list
	return dict_client_tags
    
def start_listening(IP, PORT, dict_client_tags):
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	orig = (IP, int(PORT))
	udp.bind(orig)
	while True:
		message, client = udp.recvfrom(1024)
		message = message.decode('ascii')
		client = str(client[0])+":"+str(client[1])
		print("recebeu", message, client)
		if is_message_valid(message):
			received_tags = decode_message(message)
			print("tags", received_tags)
			for tag in received_tags:
				if tag.startswith('+'):
					add_tag_to_client(client, tag, dict_client_tags)
				elif tag.startswith('-'):
					remove_tag_from_client(ip_port, tag, dict_client_tags)
				elif tag.startswith('#'):
					send_message_to_interested_part(tag, message, dict_client_tags)
			print("dict", dict_client_tags)
	udp.close()
	
def send_message_to_interested_part(tag, message, dict_client_tags):
	tag = tag[1:]
	for client, tags in dict_client_tags.items():
		if tag in tags:
			ip, port = client.split(':')
			print("envia para", ip, port, message)
			send_message(ip, port, message)
			
def send_message(HOST, PORT, message):
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = (HOST, int(PORT))

	udp.sendto(message.encode('ascii'), dest)
	udp.close()		
	
if __name__ == "__main__":
	main(sys.argv[1:])
