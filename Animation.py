"""
Created on Sat Sep 19 19:49:26 2020
@author: ISH KAPOOR
"""
import os, time
os.system('cls')
filenames = []

total_files = 30

for i in range(0, int(total_files)+1):
    name = "ascii_image" + str(i) + ".txt"
    filenames.append(name)

frames = []

for name in filenames:
    with open(name, 'r', encoding = 'utf8') as f:
        frames.append(f.readlines())

for i in range(10):
    for frame in frames:
        print("".join(frame))
        time.sleep(0.007)
        os.system('cls')