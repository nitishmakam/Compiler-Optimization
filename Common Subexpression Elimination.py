from sympy import cse,pprint,sympify,numbered_symbols
from sympy.printing import ccode
from sympy.abc import a,b,c,x,y
import re
def commonsubelim(filename1,filename2):
	modifiedlines=[]
	with open(filename1,'r') as file:
		for line in file:
			line=line.strip('\n')
			currentline=line+'\n'
			flag=False
			if('=' in line):
				line=line.strip(';')
				lines=line.split('=')
				docse=False
				lines[1]=lines[1].replace(' ','')
				docse=re.search("[0-9]",lines[1])
				if(not docse):
					lines[1]=eval(lines[1])	
					compressedexpr=cse(lines[1],numbered_symbols("help"))
					currentline=lines[0]+'='
					for helper in compressedexpr[0]:
						flag=True											
						#currentline=currentline+str(ccode(helper[1],helper[0]))+"\n"
						modifiedlines.append("int "+str(ccode(helper[1],helper[0]))+"\n")
					for i,result in enumerate(compressedexpr[1]):
						modifiedlines.append("int "+(ccode(result,"result")))
						modifiedlines.append("\n")			
			if(flag==False):
				modifiedlines.append(currentline)	
	with open(filename2,'w') as file:
		for line in modifiedlines:
			file.write(line)
		file.write('\n')
		file.truncate()

filename1='test1.c'
filename2='b.c'
commonsubelim(filename1,filename2)
