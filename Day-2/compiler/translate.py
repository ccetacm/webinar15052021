from os import sys

text=''
data=''


def add(operand,symboltable):
	global text
	op2=operand.pop()
	op1=operand.pop()
	if op1[1]==2 and op2[1]==2:
		if op1[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()

		text+='mov eax,dword ['+op1[0]+']\n'
		text+='add eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==3 and op2[1]==2:
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='mov eax,'+op1[0]+'\n'
		text+='add eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==-3 and op2[1]==2:
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='add eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==2 and op2[1]==3:
		if op1[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='mov eax,dword ['+op1[0]+']\n'
		text+='add eax,'+op2[0]+'\n'
		operand.append((-3,-3))
	elif op1[1]==3 and op2[1]==3:
		text+='mov eax,'+op1[0]+'\n'
		text+='add eax,'+op2[0]+'\n'
		operand.append((-3,-3))
	elif op1[1]==-3 and op2[1]==3:
		text+='add eax,'+op2[0]+'\n'
		operand.append((-3,-3))

def sub(operand,symboltable):
	global text
	op2=operand.pop()
	op1=operand.pop()
	if op1[1]==2 and op2[1]==2:
		if op1[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()

		text+='mov eax,dword ['+op1[0]+']\n'
		text+='sub eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==3 and op2[1]==2:
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='mov eax,'+op1[0]+'\n'
		text+='sub eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==-3 and op2[1]==2:
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='sub eax,dword ['+op2[0]+']\n'
		operand.append((-3,-3))
	elif op1[1]==2 and op2[1]==3:
		if op1[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='mov eax,dword ['+op1[0]+']\n'
		text+='sub eax,'+op2[0]+'\n'
		operand.append((-3,-3))
	elif op1[1]==3 and op2[1]==3:
		text+='mov eax,'+op1[0]+'\n'
		text+='sub eax,'+op2[0]+'\n'
		operand.append((-3,-3))
	elif op1[1]==-3 and op2[1]==3:
		text+='sub eax,'+op2[0]+'\n'
		operand.append((-3,-3))


def assign(operand,symboltable):
	global text
	#print(operand)
	op2=operand.pop()
	op1=operand.pop()
	
	#print(op2)
	#print(symboltable)
	if op1[0] not in symboltable:
		print("Compilation Error")

		sys.exit()
	if op2[1]==2:
		if op2[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		text+='mov eax,dword ['+op2[0]+']\n'
		text+='mov dword ['+op1[0]+'] , eax\n'
		operand.append((-3,-3))
	elif op2[1]==3:
		text+='mov eax,'+op2[0]+'\n'
		text+='mov dword ['+op1[0]+'] , eax\n'
		operand.append((-3,-3))
	elif op2[1]==-3:
		text+='mov dword ['+op1[0]+'] , eax\n'
		operand.append((-3,-3))


def allocate(operand,symboltable):
	global data
	op1=operand.pop()
	
	if op1[0] in symboltable:
		print("Compilation Error")

		sys.exit()
	data+=op1[0]+'     dd 1 dup(0)\n'
	symboltable.append(op1[0])
	return 0

def echo(operand,symboltable):
	global text
	op1=operand.pop()
	if op1[1]==2:
		if op1[0] not in symboltable:
			print("Compilation Error")

			sys.exit()
		
		text+='mov eax,dword ['+op1[0]+']\n'
		text+='call  print_eax\n'
	elif op1[1]==3:
		text+='mov eax,'+op1[0]+'\n'
		text+='call print_eax\n'
	return 0


def read(operand,symboltable):
	global text
	op1=operand.pop()
	
	if op1[0] not in symboltable:
		print("Compilation Error")

		sys.exit()
		
	
	text+='call  read_hex\n'
	text+='mov dword ['+op1[0]+'],eax\n'
	
	return 0




def translate(tokens,file_name):
	global text
	global data
	database={'10':[2,add],'11':[2,sub],'12':[2,assign],'110':[1,allocate],'220':[1,echo],'330':[1,read]}
	priority={'10':0,'11':0,'12':1,'110':2,'220':3,'330':4}
	symboltable=[]
	operand=[]
	operator=[]
	'''text=''
	data='''
	index=0
	for token in tokens:
		index=index+1
		#print(index)
		for symbol in token:
			if str(symbol[1]) not in database:
				operand.append(symbol)
			else:
				if len(operator)==0 or (priority[str(symbol[1])] < priority[str(operator[-1][1])]):
					operator.append(symbol)
				else:

					database[str(operator.pop()[1])][1](operand,symboltable)
					operator.append(symbol)
		while len(operator)!=0:
			database[str(operator.pop()[1])][1](operand,symboltable)
		operand=[]

	header=''
	header+='format PE console\n'
	header+='entry start\n'
	header+="include 'C:\\Users\\91987\\Downloads\\fasmw17327\\INCLUDE\\win32a.inc'\n"
	data="section '.data' readable writeable\n"+data
	print(data)
	text="section '.text' code readable executable\nstart:\n"+text+"push 0\ncall [ExitProcess]\ninclude 'training.inc'"
	print(text)

	with open(file_name+'.asm','w') as fg:
		fg.write(header+data+text)



if __name__ == '__main__':
	translate([[(110, 110), ('a', 2)], [(110, 110), ('b', 2)], [(110, 110), ('c', 2)], [('c', 2), (12, 12), ('2', 3)], [('b', 2), (12, 12), ('c', 2), (10, 10), ('2', 3)], [(220, 220), ('b', 2)]],'test.ig')





