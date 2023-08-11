### 题解：直接不考虑暴力解法，直接考虑双指针（快慢指针），快指针用来扫描整个数组，慢指针用来更新sub-array， 如果是写的for loop作为外层循环，就要在j - i这里+1，因为呢
### 这里的for loop会在进行while判断之后在把j + 1.

### 下面还有一个用两个while loop的解法，非常相似，逻辑基本一样
### 对于while循环来讲，没有像for loop那样这么直观，因为，在这里，如果是while这样的写法，他的j值，会比for循环写法的大一位，
### 2（0），3（1），1（2），2（3），4（4），3（5）举例，当我们的j遍历到4这个数字的时候，我们的sub-array total等于8，大于7了，这个时候是不是应该进入内层的while循环，去利用我们的慢指针i，进行我们sub-array大小的判断（因为我们需要的是个最小的能满足条件的array，eg，数组的和 >= 7，这里的答案应该是（4，3）。）
### 而在我们进行了移动快指针操作的时候，我们在算了total之后，j的值我们也相对应的加了一，因为如果不加1的话，我们滑动窗口的大小就会少一位。（2，3，1，2），对应这个数组的index，（0，1，2，3），如果我们的j刚刚好是3，那么这个滑动窗口的大小就是(j - i)也就是3，那么对应数组就会是这样的（0，1，2），这样在看起来似乎没有什么问题，但在后面计算的时候就会报错，最终的result结果会因为你遍历到list末尾的时候，少了1。
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
