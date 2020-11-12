import re 
import sys
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'

f = sys.argv[1]
f1 = open(f,"r")
line = f1.readlines()
#string = "ပြင်ဆင်ရေးကို စတင်ကတည်းက catdogစတင်ကတည်းကdogdog"
#string = string.replace(" ","")

def syllable(data):
	BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
	sylbreak =  BreakPattern.sub("/" + r"\1", data)
	return sylbreak
c = 0
for i in range(len(line)):
	syl = syllable(line[i].rstrip("\n").replace(" ",""))
	con = syl.split("/")
	for j in range(1,len(con)):
		print(str(c)+"\t"+str(c+1)+"\t"+con[j])
		c = c+1
print(c)
