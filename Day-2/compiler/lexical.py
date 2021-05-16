import re
from os import sys

def lexical(file):                                           
	keywords={'int':110,'echo':220,'read':330}
	operators={'+':10,'-':11,'=':12}
	types={'keywords':0,'operators':1,'identifier':2,'constant':3}
	df=[]
	#sl=[]
	buffers=''
	for chars in file:
		if chars=='':
			continue
		sl=[]                                                  #int a
		i=1
		for char in chars:
			
			s=0
			'''if char in operators:
				sl.append((operators[char],types['operators']))
				s+=1'''
			if char.isalnum():     #int b
				buffers+=char
				s=s+1
			if (not (char.isalnum()) or i==len(chars)) and len(buffers)!=0:
				res=re.search(r'^[A-Za-z]([A-Za-z0-9_]*)$',buffers)  #if string in buffer is satisfying conditions of being a identifier'
				res1=re.search(r'(\d)+',buffers) #if string in buffer is satisfying condition of being number
				if buffers in keywords:
					sl.append((keywords[buffers],keywords[buffers])) #s1.append((110,110))
					s+=1
				elif res:
					
					if res:
						sl.append((buffers,types['identifier']))
						s+=1
				elif res1:
					
					if res1:
						sl.append((buffers,types['constant']))
						s+=1
				buffers=''
			if char in operators:
				sl.append((operators[char],operators[char]))
				s+=1

			if s==0:
				print(f'{char}  is not valid symbol')
				sys.exit()
			i=i+1
		df.append(sl)      #int a
	return df              #int b
                          



if __name__ == '__main__':
	file=open('test.ig','r')
	string=file.read()
	lists=string.split('\n')
	tokens=lexical(lists)
	print(tokens)




		
