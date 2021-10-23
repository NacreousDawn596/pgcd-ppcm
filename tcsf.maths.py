import sys
types = sys.argv[1]
f = eval(sys.argv[2])
s = eval(sys.argv[3]) 
def pgcd(a, b):
	while a!=b: 
		d=abs(b-a) 
		b=a 
		a=d 
	return d
		
		
def ppcm(a, b):
	pgc = pgcd(a, b)
	return a*b / int(pgc)
	
if types == "pgcd":
	res = pgcd(f, s)
	print(f"pgcd: ", res)
	if res == 1:
		print("ces deux nombres sont premiers entre eux")
elif types == "ppcm":
	res = ppcm(f, s)
	print("ppcm: ", res)
