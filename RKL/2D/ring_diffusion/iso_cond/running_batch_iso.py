from diffusion_rkl1_iso import main

sset = [101, 51, 21, 11, 5, 2]
nset = [50, 100, 200, 400]
for s in sset:
	for i in nset:
		main(s, i, i)
