from diffusion_rkl1 import main

sset = [30, 25]
nset = [50, 100, 200]
for s in sset:
	for i in nset:
		main(s, i, i)
