with open("1-input.txt") as fin:
    data = fin.read()
    
numbers = [int(i) for i in data.split("\n")[:-1]]

print(len(numbers))

def naive():
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    print(i * j * k)
                    break
                    
                    
def smarter():
    for i in range(len(numbers)):
        rem = 2020 - numbers[i]
        seen = set()
        for j in range(i, len(numbers)):
            seen.add(numbers[j])
            if rem - numbers[j] in seen:
                product = numbers[i] * numbers[j] * (rem - numbers[j])
                print(product)
                
smarter()