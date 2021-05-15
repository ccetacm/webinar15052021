format PE console
entry start
include 'win32a.inc'

;========================================================================================

section '.data'

c:   dw dup(0)
d:   dw dup(0)



section '.text' code readable executable

start:
	call read_hex
	mov ebx,eax
	call read_hex
	sub eax,ebx
	call print_eax
	

	; Ending the programme

	push 0
	call [ExitProcess]

include 'training.inc'




int a  -----.
int c
a=c+1
echo 





data section

a dd(0)
c  dd(0)


text section

mov eax,[a]
mov ebx,[c]

add ebx,1
mov eax,ebx

mov [a],eax
