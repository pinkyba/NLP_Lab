# How to run: python word-seg-check1.py ./test-data-for-word-segment-checker.txt > out

import sys

fileName = sys.argv[1]
f = open(fileName, "r")
fline = f.readlines()

for i in range(len(fline)):
	# split words with space for first line
	line1 = fline[i].split(" ")

	# go to next line loop that is checked with line by line with first line
	if i < len(fline) - 1:
		start = i + 1

		# loop one by one next line and split words with space
		for j in range(start,len(fline)):
			line2 = fline[j].split(" ")
			for k in range(len(line1)):
				for m in range(len(line2)):
					# compare 1-gram and 2-gram between the two lines
					if m < len(line2) - 1 and line1[k] == line2[m]+line2[m+1]:
						print(line1[k]+" ======> "+line2[m]+" "+line2[m+1])
					
					# compare 1-gram and 3-gram between the two lines
					if m < len(line2) - 2 and line1[k] == line2[m]+line2[m+1]+line2[m+2]:
						print(line1[k]+" ======> "+line2[m]+" "+line2[m+1]+" "+line2[m+2])

					# compare 2-gram and 1-gram between the two lines
					if k < len(line1) - 1 and line1[k]+line1[k+1] == line2[m]:
						print(line1[k]+" "+line1[k+1]+" =====> "+line2[m])

					# compare 2-gram and 2-gram between the two lines
					if k < len(line1) - 1 and m < len(line2) - 1 and line1[k]+line1[k+1] == line2[m]+line2[m+1]:
						print(line1[k]+" "+line1[k+1]+" =====> "+line2[m]+" "+line2[m+1])

					# compare 2-gram and 3-gram between the two lines
					if k < len(line1) - 1 and m < len(line2) - 2 and line1[k]+line1[k+1] == line2[m]+line2[m+1]+line2[m+2]:
						print(line1[k]+" "+line1[k+1]+" =====> "+line2[m]+" "+line2[m+1]+" "+line2[m+2])

					# compare with 3-gram/1-gram, 3-gram/2-gram, and 3-gram/3-gram
					if k < len(line1) - 2 and line1[k]+line1[k+1]+line1[k+2] == line2[m]:
						print(line1[k]+" "+line1[k+1]+" "+line1[k+2]+" =====> "+line2[m])
					if k < len(line1) - 2 and m < len(line2) - 1 and line1[k]+line1[k+1]+line1[k+2] == line2[m]+line2[m+1]:
						print(line1[k]+" "+line1[k+1]+" "+line1[k+2]+" =====> "+line2[m]+" "+line2[m+1])
					if k < len(line1) - 2 and m < len(line2) - 2 and line1[k]+line1[k+1]+line1[k+2] == line2[m]+line2[m+1]+line2[m+2]:
						print(line1[k]+" "+line1[k+1]+" "+line1[k+2]+" =====> "+line2[m]+" "+line2[m+1]+" "+line2[m+2])	
					
