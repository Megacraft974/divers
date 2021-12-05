# un+1 = 1/4un
# u1 = 1/4

# un = 1/4^n
# u2 = 0.0625
# u3 = 0.015625

def seuil(A):
	un=1/4
	n=1
	while un>A:
		un=un/4
		n=n+1
	return n

print(seuil(0.000000001))