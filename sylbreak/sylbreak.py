import re 
import sys
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'


string = "ပြင်ဆင်ရေးကို စတင်ကတည်းက catdogစတင်ကတည်းကdogdog"
string = string.replace(" ","")

BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
sylbreak =  BreakPattern.sub("/" + r"\1", string)
print(sylbreak)
