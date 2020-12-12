import os

n = 1

while str(n).zfill(2) in os.listdir():
    n += 1

os.mkdir(str(n).zfill(2))
os.chdir(str(n).zfill(2))
open(f"{n}_1.py", "w").close()
open(f"{n}_2.py", "w").close()
open(f"{n}_input.txt", "w").close()