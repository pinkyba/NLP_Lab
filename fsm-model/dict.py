import sys

inFile = sys.argv[1]
f = open(inFile,"r")

fline = f.readlines()
flen = len(fline)

for i in range (flen):
	fs1 = fline[i].split(" ")
	#print(fs1)
	for j in range(len(fs1)):
		fs1[j] = fs1[j].rstrip("/\n")
		fs2 = fs1[j].split("/")
		print("0"+"\t"+"0"+"\t"+str(fs2[1])+"\t"+str(fs2[0]))
print("0")
