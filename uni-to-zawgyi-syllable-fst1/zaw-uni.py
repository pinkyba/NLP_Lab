import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

file1 = open(f1, "r")
file2 = open(f2, "r")
line1 = file1.readlines()
line2 = file2.readlines()

for k in range(len(line1)):
	con1 = line1[k].rstrip("\n").split(" ")
	con2 = line2[k].rstrip("\n").split(" ")
	
	for i in range(len(con1)):
		print("0"+"\t"+"0"+"\t"+con1[i]+"\t"+con2[i])
print("0")
		
