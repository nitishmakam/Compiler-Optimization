import re
def fold(filename,filename2):
	modifiedlines=[]
	with open(filename,'r') as file:
		for line in file:
			isFloat=False
			line=line.strip('\n')
			currentline=line+'\n'
			if('=' in line):
				line=line.strip(';')
				lines=line.split('=')
				lines[1]=lines[1].replace(' ','')		
				if("." in lines[1]):
					isFloat=True
				flag=re.search(".*[a-zA-Z]+.*",lines[1])
				if(not flag):
					value=float(eval(lines[1]))
					if(not isFloat):
						value=int(value)
					currentline=lines[0]+"="+str(value)+';'+'\n'
			modifiedlines.append(currentline)
	with open(filename2,'w') as file:
		for d in modifiedlines:
			file.write(d)
		file.write('\n')
		file.truncate()
filename='test.c'
filename2='test1.c'
fold(filename,filename2)
