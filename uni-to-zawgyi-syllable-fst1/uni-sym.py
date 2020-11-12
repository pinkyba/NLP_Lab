import sys

f = sys.argv[1]
fo = open(f,"r")

line = fo.readlines()
print("Ɛ"+"\t"+"0")
print("\s"+"\t"+"1")
c = 2
for k in range(len(line)):
	
	print(line[k].rstrip("\n")+"\t"+str(c+k))
