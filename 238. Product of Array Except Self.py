def productExceptSelf(self, nums):
    prefix = []
    postfix = []
    final_list = []
    result1=1
    result2=1
    for num in nums :
        result1 *= num
        prefix.append(result1)

    for i in range(len(nums) -1 ,-1, -1):
        result2 *= nums[i]
        postfix.append(result2)

    postfix = postfix[::-1]

    for i in range(len(nums)):
        if i == 0 :
            final_list.append(postfix[i+1])
        elif i == len(nums) - 1 :
            final_list.append(prefix[i-1])
        else:
            final_list.append(prefix[i-1] * postfix[i+1])


    return final_list

