### 题解：直接不考虑暴力解法，直接考虑双指针（快慢指针），快指针用来扫描整个数组，慢指针用来更新sub-array， 如果是写的for loop作为外层循环，就要在j - i这里+1，因为呢
### 这里的for loop会在进行while判断之后在把j + 1.

### 下面还有一个用两个while loop的解法，非常相似，逻辑基本一样
```py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        result = len(nums) + 1
        total = 0
        i, j = 0,0
        for i in range(len(nums)):
            total += nums[j]
            # 问题所在，为什么这里写for不行，因为j的值要等下面的while跑完之后才会➕1，然而加1过后，total
            # 
            while (total >= target):
                result = min(result, j - i + 1) # 这里的j - i是滑动窗口的大小
                total -= nums[i]
                i += 1
        if result == len(nums) + 1:
            return 0
        else:
            return result

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        result = len(nums) + 1
        total = 0
        i, j = 0,0
        while(j < len(nums)):
            total += nums[j]
            j += 1
            while (total >= target):
                result = min(result, j - i + 1) # 这里的j - i是滑动窗口的大小
                total -= nums[i]
                i += 1
        if result == len(nums) + 1:
            return 0
        else:
            return result

```
