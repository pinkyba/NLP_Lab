import sys

inFile = sys.argv[1]
f = open(inFile,"r")

fline = f.readlines()
flen = len(fline)
tmp = 0
count = 0
for i in range(flen):
	fs1 = fline[i].split(" ")
	#print(fs1)	
	for j in range(len(fs1)):
		tmp = count
		if j == 0:
			print("0"+"\t"+str(tmp+1)+"\t"+str(fs1[j]).rstrip("/\n"))
		else:
			print(str(tmp)+"\t"+str(tmp+1)+"\t"+str(fs1[j]).rstrip("/\n"))
		count = count + 1
	print(str(tmp+1))
	
