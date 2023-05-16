numbers = list(map(float, input().split()))
if len(numbers) % 2 == 1:
    print("The median is", sorted(numbers)[(len(numbers) - 1) // 2])
else:
    sum_two = sorted(numbers)[len(numbers) // 2] + sorted(numbers)[len(numbers) // 2 - 1]
    print("The mean of center numbers is", sum_two/2)
