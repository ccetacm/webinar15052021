format PE console
entry start
include 'C:\Users\91987\Downloads\fasmw17327\INCLUDE\win32a.inc'

;========================================================================================





section '.text' code readable executable

start:
	call read_hex
	mov ebx,eax
	call read_hex
	sub eax,ebx
	;eax=eax-ebx      
	call print_eax
	

	; Ending the programme

	push 0
	call [ExitProcess]

include 'training.inc'





