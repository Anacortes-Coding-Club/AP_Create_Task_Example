sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()

for line in sample:
    nums = [int(n) for n in line.split()]
    if all(nums[i] > nums[i+1] for i in range(len(nums)-1)):
        print("all decreasing", nums)


# write a function to compute the n'th fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

print(fibonacci(300))  # 832040