# Задача на LeetCode: Two Sum (https://leetcode.com/problems/two-sum/)
# Описание задачи:
# Даны массив целых чисел nums и целое число target, верните индексы двух чисел так, чтобы они в сумме давали target.  # noqa: E501
# Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.  # noqa: E501
# Вы можете вернуть ответ в любом порядке.
class Solution:
    def twoSum(self,nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
page_1 = Solution()
print(page_1.twosum([2,7,11,15], 18))