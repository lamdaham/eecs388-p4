#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'\x79\x69\x6A\x6F')
sys.stdout.buffer.write(b'\x20'*(10-len(b'\x79\x69\x6A\x6F')))
sys.stdout.buffer.write(b'\x41\x2B')