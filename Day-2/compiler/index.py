from lexical import lexical
from syntax import syntax
from translate import translate
from os import sys,system


with open(sys.argv[1],'r') as fg:
	code=fg.read()
	lists=code.split('\n')
	tokens=lexical(lists)
	syntax(tokens)

translate(tokens,sys.argv[1])
system('fasm '+sys.argv[1]+'.asm')



