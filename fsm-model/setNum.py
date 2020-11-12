import sys
readf = sys.argv[1]
f = open(readf,"r")

fline = f.readlines()
flen = len(fline)

for i in range(flen):
	print(str(fline[i].rstrip("/\n"))+"\t"+str(i))
