import string
import numpy as np
import matplotlib.pyplot as plt

def main():
	alphabet = string.ascii_uppercase
	m = len(alphabet)
	code = 'BTJPXRMLXPCUVAMLXICVJPIBTWXVRCIMLMTRPMTNMTNYVCJXCDXVMWMBTRJJPXAMTNGXRJBAHUQCTJPXQGMRJXVCIJPXYMGGCIJPXHBTWRQMGMAXMTNJPXHBTWRMYJPXQGMRJXVCIJPXPMTNJPMJYVCJXJPXTJPXHBTWRACUTJXTMTAXYMRAPMTWXNMTNPBRJPCUWPJRJVCUFGXNPBLRCJPMJJPXSCBTJRCIPBRGCBTRYXVXGCCRXNMTNPBRHTXXRRLCJXCTXMWMBTRJMTCJPXV'
	#code = 'Anna Pavlovna smiled and promised to take Pierre in hand. She knew his father to be a connection of Prince Vasilis. The elderly lady who had been sitting with the old aunt rose hurriedly and overtook Prince Vasili in the anteroom. All the affectation of interest she had assumed had left her kindly and tear-worn face and it now expressed only anxiety and fear. Apparently she had forgotten her age and by force of habit employed all the old feminine arts. But as soon as the prince had gone her face resumed its former cold, artificial expression. She returned to the group where the vicomte was still talking, and again pretended to listen, while waiting till it would be time to leave. Her task was accomplished. Pierre was ungainly. Stout, about the average height, broad, with huge red hands; he did not know, as the saying is, how to enter a drawing room and still less how to leave one; that is, how to say something particularly agreeable before going away. Besides this he was absent-minded. When he rose to go, he took up instead of his own, the generals three-cornered hat, and held it, pulling at the plume, till the general asked him to restore it. All his absent-mindedness and inability to enter a room and converse in it was, however, redeemed by his kindly, simple, and modest expression. Anna Pavlovna turned toward him and, with a Christian mildness that expressed forgiveness of his indiscretion, nodded and said: Pierre at the age of ten had been sent abroad with an abbe as tutor, and had remained away till he was twenty. When he returned to Moscow his father dismissed the abbe and said to the young man, Now go to Petersburg, look round, and choose your profession. I will agree to anything. Here is a letter to Prince Vasili, and here is money. Write to me all about it, and I will help you in everything. Pierre had already been choosing a career for three months, and had not decided on anything. It was about this choice that Prince Andrew was speaking. Pierre rubbed his forehead. Dolokhov was of medium height, with curly hair and light-blue eyes. He was about twenty-five. Like all infantry officers he wore no mustache, so that his mouth, the most striking feature of his face, was clearly seen. The lines of that mouth were remarkably finely curved. The middle of the upper lip formed a sharp wedge and closed firmly on the firm lower one, and something like two distinct smiles played continually round the two corners of the mouth; this, together with the resolute, insolent intelligence of his eyes, produced an effect which made it impossible not to notice his face. Dolokhov was a man of small means and no connections. Yet, though Anatole spent tens of thousands of rubles, Dolokhov lived with him and had placed himself on such a footing that all who knew them, including Anatole himself, respected him more than they did Anatole. Dolokhov could play all games and nearly always won. However much he drank, he never lost his clearheadedness. Both Kuragin and Dolokhov were at that time notorious among the rakes and scapegraces of Petersburg.'
	code = code.upper()
	n = len(code)
	#remove non-uppercase characters
	code1 = ''
	for i in range(n):
                if ( alphabet.find(code[i]) != -1 ):
			code1 = code1 + code[i]
	code = code1
	n = len(code)
	#count the occurence of each alphabet
	cnt = np.zeros(m)
	for s in range(n):
		t = 0
		found = 0
		while (found==0):
			if ( code[s] != alphabet[t] ):
				t = t+1
			else:
				cnt[t] = cnt[t]+1
				found = 1				
	for i in range(m):
		print i, alphabet[i], cnt[i]
	plt.plot(np.linspace(0,m-1,m), cnt,'o-')
	plt.xlabel ('index')
	plt.ylabel ('frequency')
	plt.show()
	return	

if __name__ == '__main__':
	main()
