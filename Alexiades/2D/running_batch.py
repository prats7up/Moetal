from diffusion_AAG import main

sset = [100, 50, 20, 10, 5]
nset = [50, 100, 200]
for s in sset:
	for i in nset:
		main(s, i, i)
