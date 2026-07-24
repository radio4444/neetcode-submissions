class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hash set
        dupli_set = set()
        # traverse the list. 
        for i in nums: 
            # check if the elemnt exists 
            if i in dupli_set:
                return True
            # add the element in the set
            dupli_set.add(i) # attribute error: should be .add() not .append()
        return False