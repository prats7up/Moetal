from diffusion_rkl1 import main

sset = [400, 200]
nset = [100, 200, 400]
for s in sset:
	for i in nset:
		main(s, i, i)
