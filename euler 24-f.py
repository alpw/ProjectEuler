from itertools import permutations

nums = []

for num in list(permutations(range(0,10))):
    nums.append(num)
    if len(nums) == int(1e6):
        break

print(nums[-1])

"""   ...::: WORKED :::...   """