class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p = 0
        q = len(numbers) - 1

        while (p < q):
            sum = numbers[p] + numbers[q]
            if (sum > target):
                q -= 1
            elif (sum < target):
                p += 1
            else :
                return [p + 1, q + 1]

        