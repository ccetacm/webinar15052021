from os import sys

def syntax(tokens):
	valid=[(2),(3),(110,2),(220,2),(220,3),(330,2),(2,10,2),(3,10,3),(2,10,3),(3,10,2),(2,11,2),(3,11,3),(2,11,3),(3,11,2),(2,12,3),(2,12,2)]
	result=[2,3,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,3]
	index=0
	for token in tokens:
		index=index+1
		if len(token)==1:
			test=(token[0][1])
			if test in valid:
				pass
			else:
				print(f"syntax error at line {index}")
				sys.exit()
		elif len(token)==2:
			test=(token[0][1],token[1][1])
			if test in valid:
				pass
			else:
				print(f"syntax error at line {index}")
				sys.exit()
		elif len(token)>=3:
			i=1
			prev=token[0][1]
			while i<=len(token)-1:
				second=token[i][1]
				if i+1<=len(token)-1:
					third=token[i+1][1]
					test=(prev,second,third)
				else:
					test=(prev,second)
				if test in valid:
					prev=result[valid.index(test)]
					i=i+2
				else:
					print(f"syntax error at line {index}")
					sys.exit()



if __name__ == '__main__':
	syntax([[(110, 110), ('a', 2)], [(110, 110), ('b', 2)], [(110, 110), ('c', 2)], [('c', 2), (12, 12), ('2', 3)], [('b', 2), (12, 12), ('c', 2), (10, 10), ('2', 3)], [(220, 220), ('b', 2)]])

	