import string
from collections import OrderedDict

def encipher_caeser_phrase(string_in, shift, phrase):
        phrase = "".join(OrderedDict.fromkeys(phrase))
        len_phrase = len(phrase)
        alphabet = string.ascii_lowercase
        n = len(alphabet)
        beg = alphabet.index(shift)
        key = phrase
        alphabet1 = alphabet[beg:n]+alphabet[0:beg]
        beg = 0
        while ( len(key)<n):
                if (phrase.find(alphabet1[beg]) == -1):
                        key = key + alphabet1[beg]
                beg = beg + 1
        print 'alphabet=', alphabet
        print 'key=     ', key
        m  = len(string_in)
        string_out = ''
        for i in range(m):
                if ( alphabet.find(string_in[i]) != -1 ):
                        string_out = string_out + key[alphabet.index(string_in[i])]
        return string_out.upper()

def decipher_caeser_phrase(string_in, shift, phrase):
	phrase = "".join(OrderedDict.fromkeys(phrase))
	len_phrase = len(phrase)
        alphabet = string.ascii_uppercase
        n = len(alphabet)
        beg = alphabet.index(shift)
	key = phrase
	alphabet1 = alphabet[beg:n]+alphabet[0:beg]
	beg = 0
        while ( len(key)<n):
                if (phrase.find(alphabet1[beg]) == -1):
                        key = key + alphabet1[beg]
                beg = beg + 1
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
