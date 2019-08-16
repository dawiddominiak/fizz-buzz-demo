from engine.fizz_buzz_loop import start_fizz_buzz_loop
from sys import argv

loop_length = 100 # default

if len(argv) >= 2:
  loop_length = int(argv[1])

start_fizz_buzz_loop(loop_length)