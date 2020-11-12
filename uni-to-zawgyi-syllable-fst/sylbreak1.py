import re 
import sys
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'

file1 = sys.argv[1]
f = open(file1,"r")
lines = f.readlines()

def syllable(data):
	BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
	sylbreak =  BreakPattern.sub(" " + r"\1", data)
	return sylbreak;

for i in range(len(lines)):
	res = ""
	con = lines[i].rstrip("\n").split(" ")
	for j in range(len(con)):
		if not(re.match(r"[a-zA-z0-9]+", con[j])):
			syl = syllable(con[j])
			res += syl
		else:
			res += " "+con[j].upper()

	res = res.lstrip(" ")
	
	print(res)
