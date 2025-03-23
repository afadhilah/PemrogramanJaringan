N = int(input())

total = 0

for _ in range(N):
    line = input()
    
    numbers = map(int, line.replace('-', ' -').split())

    for num in numbers:
        if num > 0:
            total += num

print(total)
