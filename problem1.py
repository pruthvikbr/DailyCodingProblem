

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