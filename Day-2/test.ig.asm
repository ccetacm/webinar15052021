format PE console
entry start
include 'C:\Users\91987\Downloads\fasmw17327\INCLUDE\win32a.inc'
section '.data' readable writeable
a     dd 1 dup(0)
b     dd 1 dup(0)
c     dd 1 dup(0)
section '.text' code readable executable
start:
call  read_hex
mov dword [a],eax
mov eax,2
mov dword [c] , eax
mov eax,dword [c]
add eax,2
add eax,dword [a]
mov dword [b] , eax
mov eax,dword [b]
call  print_eax
push 0
call [ExitProcess]
include 'training.inc'