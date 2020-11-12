import re 
import sys
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'
string = "ပြင်ဆင်ရေးကို စတင်ကတည်းက လွှတ်တော်ရဲ့ လက်ရှိသက်တမ်းအတွင်း အပြီးသတ်ပြင်ဆင်မယ်လို့ စဉ်းစားပြီး လက်ခံခဲ့တာ ဖြစ်တယ်လို့လည်း ဒီဇင်ဘာလရက် ပြည်ထောင်စုလွှတ်တော် အစည်းအဝေးမှာ ပြောခဲ့ပါတယ်။ပြည်ခိုင်ဖြိုးနဲ့ တပ်မတော်သား ကိုယ်စားလှယ်တွေ တင်သွင်းထားတဲ့ အခြေခံဥပဒေပြင်ဆင်ရေး မူကြမ်းတွေဟာ ဥပဒေကြမ်း အဆင့်ကို ရောက်ရှိနေပြီ ဖြစ်ပြီးတော့ အဲဒီကိုယ်စားလှယ်တွေက ဥပဒေကြမ်း လေးခု ကို လွှတ်တော်မှာ တင်သွင်းခဲ့ပါတယ်။"
string = string.replace(" ","")

BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
sylbreak =  BreakPattern.sub("/" + r"\1", string)
con = sylbreak.split("/")
del con[0]

pattern = re.compile(r'[က-အ]+[ာိီုူါေဲံ့း်]*')
pattern1 = re.compile(r'[က-အ][ျြှွ][က-အ]*[ာိီုူါေဲံ့း်]*[က-အ]*[ာိီုူါေဲံ့း်]*')
pattern2 = re.compile(r'[က-အ][ျြှွ][ျြှွ][က-အ]*[ာိီုူါေဲံ့း်]*[က-အ]*[ာိီုူါေဲံ့း်]*')
pattern3 = re.compile(r'[။ဥ၍ဩ၏ဤ၌]')
res = ""
for i in range(len(con)):
	less = ""
	if(pattern3.match(con[i])):
		res += pattern3.match(con[i]).group()
	elif(pattern2.match(con[i])):
		mo = pattern2.match(con[i]).group()
		res += mo[0]+mo[1]+mo[2]
		for j in range(3,len(mo)):	
			less += mo[j]
		res += "အ"+less+" "
	elif (pattern1.match(con[i])):
		mo = pattern1.match(con[i]).group()
		res += mo[0]+mo[1]
		for j in range(2,len(mo)):	
			less += mo[j]		
		res += "အ"+less+" "
	else:
		mo = pattern.match(con[i]).group()
		res += mo[0]
		for j in range(1,len(mo)):	
			less += mo[j]
		res += "အ"+less+" "	
print(res)
