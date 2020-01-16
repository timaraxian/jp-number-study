import random
import time
from helpers import num_to_jp

max_number = input("what is the max number you want to study: ")
cycles = input("how many numbers do you want to study: ")
sleep_timer = input("how many seconds break: ")

for _ in range(int(cycles)):
    rand_num = random.randint(0, int(max_number))
    print(rand_num)
    time.sleep(int(sleep_timer))
    print(num_to_jp(rand_num))
    time.sleep(int(sleep_timer))
