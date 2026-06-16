class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        runner = numbers[left] + numbers[right]
        if runner == target: return [left+1, right+1]
        while left < right:
            runner = numbers[left] + numbers[right]
            if runner > target:
                right -= 1
            elif runner < target:
                left += 1
            else:
                return [left+1, right+1]
        
        return []