"""Write a program to take user input on how many times the code should run, 
code has a functionof checking CPU usage for every enironment"""

import psutil

execution = int(input("how many times the code should run?: "))

def check_cpu():
    print(f"CPU is: {psutil.cpu_percent(interval=1)}%")

for i in range(execution):
    check_cpu()