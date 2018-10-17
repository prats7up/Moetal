import string
from collections import OrderedDict
import numpy as np

alphabet = string.ascii_uppercase

#code = 'BYUALHAAFAYROVOEO'
#code = 'IOOEIORWOFULTSUEEMYSVHYAASE'
#code = 'TJBFPOARRAWKDYIESTNMHEIYI'
#code = 'HXWORTGSMMISOHEEHOEMN'
#code = 'TNFNAOAETTDVLHAAYLERYAIG'
#code = 'TIUSHOTSBDDITIAASIRYYANT'
#code = 'IEDHADTIBANHSUSXOVTBAUENESGROCF'
#code = 'NMIORSWITINEAAAMLMIINN'
#code = 'HAOYLSID'
#code = 'TTEIAMBEL'
#code = 'BYRTUESEHTMH'
#code = 'THAKEABAT'
#code = 'EBAFTARKATEES'
#code = 'TTESOINDDSTAAVIYYANILE'
#code = 'BEAEAURIRDTESYSNVB'
code = 'TSNHOASDDUBAASIYYTRIIT'

n = len(code)
#remove non-uppercase characters
code1 = ''
for i in range(n):
	if ( alphabet.find(code[i]) != -1 ):
		code1 = code1 + code[i]
code = code1
n = len(code)
#make factors till sqrt(n); SEEMS TO WORK NOW!
for s in range( 2, int(np.ceil(np.sqrt(n)))+1 ):
	n1 = s
	n2 = int(np.ceil(n/np.float(n1)))
	rem1 = n1 - (n1*n2-n); rem2 = n2 - (n1*n2-n)
	str1=''
	cnt=0; cnt1=0; div=0
	while (len(str1)<n):
		str1 = str1 + code[cnt]
		if (cnt1<rem1):
			skip = n2
		else:
			skip = n2-1
		cnt1 = (cnt1+1)%n1
		cnt = cnt+skip
		if (cnt>=n):
			div = div+1
			cnt = div
		else:
			cnt = cnt%n
		#print cnt1, skip, cnt
	message = str1.lower() 
	print n1, '-', message
	str1=''
        cnt=0; cnt1=0; div=0
        while (len(str1)<n):
                str1 = str1 + code[cnt]
                if (cnt1<rem2):
                        skip = n1
                else:
                        skip = n1-1
                cnt1 = (cnt1+1)%n2
                cnt = cnt+skip
                if (cnt>=n):
                        div = div+1
                        cnt = div
                else:
                        cnt = cnt%n
                #print cnt1, skip, cnt
        message = str1.lower()
        print n2, '-', message
