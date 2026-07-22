class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset 
        dupliSet = set()
        # for loop to traverse the list
        for i in range(len(nums)):
            # check if list.value == hashset
            if nums[i] in dupliSet:    
                return True
        # add list.value to hashset
            dupliSet.add(nums[i])
        return False