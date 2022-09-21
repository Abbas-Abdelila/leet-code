class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_element = 0
        n_of_operation = 0
        
        for num in nums:
            if  num <= max_element:
                n_of_operation += max_element - num + 1
                max_element += 1
            else:
                max_element = num
        
        return n_of_operation
        