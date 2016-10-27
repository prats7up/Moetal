import string
from collections import OrderedDict
from caeser_cipher import decipher_caeser

def main():
	alphabet = string.ascii_uppercase
	n = len(alphabet)
	#code = 'RXQLOQOEKQHUIKSXQSKDDYDWVEN'
	code = 'MHILYLZAZBHLXBPZXBLMVYABUHLHWWPBZJSHBKPBZJHLJBZKPJABTHYJHUBTLZAULBAYVU'
	for i in range(n):
		message = decipher_caeser(code, alphabet[i])
		print alphabet[i], '-', message
	return

if __name__ == '__main__':
	main()
