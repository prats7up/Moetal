import string
from collections import OrderedDict

def encipher_caeser_c(c_in, shift):
	alphabet = string.ascii_lowercase
	n = len(alphabet)
	beg = alphabet.index(shift) 
	key = alphabet[beg:n]+alphabet[0:beg]
	c_out = key[alphabet.index(c_in)]
	return c_out.upper()

def decipher_caeser_c(c_in, shift):
        alphabet = string.ascii_uppercase
        n = len(alphabet)
        beg = alphabet.index(shift)       
        key = alphabet[beg:n]+alphabet[0:beg]
        c_out = alphabet[key.index(c_in)]
        return c_out.lower()

def encipher_v(string_in, phrase):
	alphabet = string.ascii_lowercase
	phrase = "".join(OrderedDict.fromkeys(phrase))
	len_phrase = len(phrase)
	m  = len(string_in)
	string_in1 = ''
	for i in range(m):
		if ( alphabet.find(string_in[i]) != -1 ):
			string_in1 = string_in1 + string_in[i]
	m = len(string_in1)
	string_in = string_in1 
	string_out = ''
	for i in range(m):
		k = i%len_phrase
		if ( alphabet.find(string_in[i]) != -1 ):
                        string_out = string_out + encipher_caeser_c(string_in[i], phrase[k]) 
        return string_out.upper()
	
def decipher_v(string_in, phrase):
	alphabet = string.ascii_uppercase
	phrase = "".join(OrderedDict.fromkeys(phrase))
	len_phrase = len(phrase)
	m  = len(string_in)
        string_in1 = ''
        for i in range(m):
                if ( alphabet.find(string_in[i]) != -1 ):
                        string_in1 = string_in1 + string_in[i]
        m = len(string_in1)
        string_in = string_in1
	string_out = ''
	for i in range(m):
                k = i%len_phrase
                if ( alphabet.find(string_in[i]) != -1 ):
                        string_out = string_out + decipher_caeser_c(string_in[i], phrase[k])
	return string_out.lower()

def main():
	return

if __name__ == '__main__':
	main()
