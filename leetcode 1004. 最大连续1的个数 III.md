### 另一道sliding window的题目，也是找满足条件的sub-array长度。第一个循环用来移动指针（也就是意义上的添加元素），第二个循环用来判断，最大滑窗的意思，在第二个循环不满足条件的情况下
### 不用移动你的慢指针，如果满足，才移动你的慢指针。（最大滑窗是在迭代右移右边界的过程中更新结果，而最小滑窗是在迭代右移左边界的过程中更新结果。）

```py
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        count_zero = 0
        res = 0
        while (j < len(nums)):
            if(nums[j] == 0):
                count_zero += 1
            j += 1
            while(count_zero > k):
                if(nums[i] == 0):
                    count_zero -= 1
                i += 1
            res = max(res, j - i)
        return res
```
