import string
from collections import OrderedDict

def encipher_general(string_in, key):
	alphabet = string.ascii_lowercase
	n = len(alphabet)
	print 'alphabet=', alphabet
	print 'key=     ', key
	m  = len(string_in)
	string_out = '' 
	for i in range(m):
		if ( alphabet.find(string_in[i]) != -1 ):
			string_out = string_out + key[alphabet.index(string_in[i])]
	return string_out.upper()

def decipher_general(string_in, key):
        alphabet = string.ascii_uppercase
        n = len(alphabet)
	print 'alphabet=', alphabet
        print 'key=     ', key
        m  = len(string_in) 
        string_out = ''
        for i in range(m):
		if ( alphabet.find(string_in[i]) != -1 ):
                	string_out = string_out + alphabet[key.index(string_in[i])] 
        return string_out.lower()

def main():
	return

if __name__ == '__main__':
	main()