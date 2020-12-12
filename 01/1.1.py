with open("1-input.txt") as fin:
    data = fin.read()
    
numbers = [int(i) for i in data.split("\n")[:-1]]

def naive():
    for i in numbers:
        for j in numbers:
            if i != j:
                if i + j == 2020:
                    print(i * j)

def smarter():
    seen = set()
    for i in numbers:
        seen.add(i)
        if 2020 - i in seen:
            print(i * (2020 - i))
            break