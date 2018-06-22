#Parametros do Servidor : porta do servidor
import socket
import struct
import sys, getopt, threading

def main(argv):
	HOST = None
	if len(argv) == 1:
			PORT = argv[0] # Porta em que o servidor esta 
			HOST = '' # Endereco IP do Servidor  
			        
def is_message_valid(message):
    valid_chars = ",.?!:;+-*/=@#$%()[]{}1234567890abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ "
    for c in message:
        if c not in valid_chars:
            return False
    return True
	
def decode_message(message):
    delimiters = ["+", "-", "#"]
    final_result = []
    second_round = []
    third_round = []
    result = message.split(delimiters[0])
    for r in result:
        if '-' not in r and '#' not in r and r is not '':
            final_result.append('+'+r)
        elif r is not '':
            second_round.append('+' +r)      
    for s in second_round:
        result = s.split(delimiters[1])
        for r in result:
            if '#' not in r and r is not '':
                if '+' in r:
                    final_result.append(r)
                else:
                    final_result.append('-'+r)
            elif r is not '':
                if r.startswith('+') or r.startswith('#'):
                    third_round.append(r)
                else:
                    third_round.append('-'+r)       
    
    for t in third_round:
        result = t.split(delimiters[2])
        for r in result:
            if '#' not in r and r is not '':
                if '-' not in r and '+' not in r:
                    final_result.append('#'+r)
                else:
                    final_result.append(r)
    return final_result

def add_tag_to_client(ip_port, tag, dict_client_tags):
    if ip_port in dict_client_tags:
        temp_list = dict_client_tags[ip_port]
        if tag not in temp_list:
            temp_list.append(tag)
            dict_client_tags[ip_port] = temp_list
    else:
        dict_client_tags[ip_port] = [tag]
    return dict_client_tags
	
def remove_tag_from_client(ip_port, tag, dict_client_tags):
    if ip_port in dict_client_tags:
        temp_list = dict_client_tags[ip_port]
        temp_list.remove(tag)
        dict_client_tags[ip_port] = temp_list
    return dict_client_tags
    
if __name__ == "__main__":
	main(sys.argv[1:])
