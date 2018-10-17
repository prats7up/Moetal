import string
from collections import OrderedDict

def encipher_caeser(string_in, shift):
	alphabet = string.ascii_lowercase
	n = len(alphabet)
	beg = alphabet.index(shift) 
	key = alphabet[beg:n]+alphabet[0:beg]
	print 'alphabet=', alphabet
	print 'key=     ', key
	m  = len(string_in)
	string_out = '' 
	for i in range(m):
		if ( alphabet.find(string_in[i]) != -1 ):
			string_out = string_out + key[alphabet.index(string_in[i])]
	return string_out.upper()

def decipher_caeser(string_in, shift):
        alphabet = string.ascii_uppercase
        n = len(alphabet)
        beg = alphabet.index(shift)       
        key = alphabet[beg:n]+alphabet[0:beg]
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
