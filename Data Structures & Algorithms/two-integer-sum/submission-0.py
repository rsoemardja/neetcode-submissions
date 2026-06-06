class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. The Registry (Our character list/memory board)
        prev_map = {}

        # 2. The Narrator (Moving through each panel/number)
        for i, n in enumerate(nums):
            #3. The Detective Work(Finding the missing piece)
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i

            