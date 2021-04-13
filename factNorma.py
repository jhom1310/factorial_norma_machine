x = int(input())
b = x
a = 0
c = 0
d = 0

a += 1
while(b != 0):
	while (a != 0):
		c += 1
		a -= 1
	while (c != 0):
		while (b != 0):
			a += 1
			d += 1
			b -= 1
		while(d != 0):
			b += 1
			d -= 1
		c -= 1
	b -= 1

print("Fatorial de {} é {}".format(x,a))
