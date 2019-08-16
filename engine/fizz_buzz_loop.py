from time import sleep
from engine.fizz_buzz_engine import number_to_fizz_buzz

def start_fizz_buzz_loop(loop_length: int = 100, sleep_time_in_ms: int = 100):
  sleep_time_in_s = sleep_time_in_ms / 1000

  for x in range(1, loop_length + 1):
    fizz_buzz_or_number = number_to_fizz_buzz(x)
    print(fizz_buzz_or_number)
    sleep(sleep_time_in_s)