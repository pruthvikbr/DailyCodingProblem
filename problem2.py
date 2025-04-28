#Given an array of integers, return a new array such that each element at index i of the new array 
#is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?






def product_except_self_division(nums):
    zero_count=nums.count(0) #Counting the number of 0's
    total_product=1
    if zero_count > 2:
        return [0] *len(nums)
    
    for num in nums:
        if num!=0:
            total_product *=num
        
    result=[]

    for num in nums:
        if zero_count==0:
            result.append(total_product//num)
        else:
            if num==0:
                result.append(total_product)
            else:
                result.append(0)
    return result


print(product_except_self_division([1, 2, 3, 4, 5]))  # Expected: [120, 60, 40, 30, 24]
print(product_except_self_division([3, 2, 1]))        # Expected: [2, 3, 6]
print(product_except_self_division([0, 1, 2, 3]))     # Expected: [6, 0, 0, 0]
print(product_except_self_division([0, 0, 1, 2]))     # Expected: [0, 0, 0, 0]
print(product_except_self_division([5]))              # Expected: [1]
