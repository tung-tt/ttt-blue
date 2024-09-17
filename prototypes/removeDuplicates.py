def removeDuplicates(nums):
        k = 0
        for i in nums:
            if k == 0 or i != nums[k - 1]:
                nums[k] = i
                k += 1
        return k
removeDuplicates([1, 1, 2])