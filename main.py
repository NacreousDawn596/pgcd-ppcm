import sys
def pgcd(a, b):
	while a!=b: 
		d=abs(b-a) 
		b=a 
		a=d 
	return d
		
		
def ppcm(a, b):
	pgc = pgcd(a, b)
	return a*b / int(pgc)

def check(num):	
	num = int(num)
	if num > 1:
		for i in range(2, int(num/2)+1):
		    if (num % i) == 0:
		        print(num, ": n'est pas un nombre premier")
		        break
		else:
		    print(num, ": est un nombre premier")
	else:
		print(num, ": n'est pas un nombre premier")

try:
	types = sys.argv[1]
	f = eval(sys.argv[2])
	s = eval(sys.argv[3])
except IndexError:
	 for h in sys.argv[2::]:
	 	check(h)

if types == "pgcd":
	res = pgcd(f, s)
	print(f"pgcd: ", res)
	if res == 1:
		print("ces deux nombres sont premiers entre eux")
elif types == "ppcm":
	res = ppcm(f, s)
	print("ppcm: ", res)
elif types == "check":
	for h in sys.argv[2::]:
		check(h)
