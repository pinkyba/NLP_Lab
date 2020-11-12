import sys

f = sys.argv[1]
fo = open(f,"r")

line = fo.readlines()

con = line[0].rstrip("\n").split(" ")

print("Ɛ"+"\t"+"0")
print("\s"+"\t"+"1")
j = 2
for i in range(len(con)):
	print(con[i]+"\t"+str(j))
	j += 1
