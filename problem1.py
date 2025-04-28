
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?



##***********************************************##

def two_sum(nums, k):
    seen = set()
    for num in nums:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# Multiple test cases
test_cases = [
    ([10, 15, 3, 7], 17),   # True
    ([1, 2, 3, 4], 8),      # False
    ([5, 5, 5, 5], 10),     # True
    ([0, -1, 2, -3, 1], -2) # True (-3 + 1)
]

for nums, k in test_cases:
    result = two_sum(nums, k)
    print(f"List: {nums}, k: {k} --> {result}")
