from diffusion_rkc2 import main

sset = [50, 20, 10, 5, 2]
nset = [50, 100, 200]
for s in sset:
	for i in nset:
		main(s, i, i)
