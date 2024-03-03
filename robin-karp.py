d = 256

def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 
	t = 0 
	h = 1
	print("\n",M," ",N)

	for i in range(M-1):
		h = (h*d) % q

	for i in range(M):
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(pat[i])) % q
		print("\n",ord(pat[i])," ",ord(pat[i]))
		print("\n",p," ",q)

	for i in range(N-M+1):
		if p == t:
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1

			if j == M:
				print("Pattern found at index " + str(i))

		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

			if t < 0:
				t = t+q

if __name__ == '__main__':
	txt = "GEEKS FOR GEEKS"
	pat = "GEEK"

	# A prime number
	q = 101

	search(pat, txt, q)
