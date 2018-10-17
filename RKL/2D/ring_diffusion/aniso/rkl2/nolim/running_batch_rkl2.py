from diffusion_rkl2 import main

#sset = [100, 50, 20, 10, 5, 2]
#nset = [50, 100, 200, 400]
#sset = [100, 50, 20]
sset = [10, 5, 2]
nset = [50, 100, 200]
for s in sset:
	for i in nset:
		main(s, i, i)
