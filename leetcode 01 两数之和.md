###
### 解法，hashmap（经典思路就是，牺牲内存，也就是space complexity，从而换取更加优秀的time complexity，因为虽然hashmap的存储过程会有很高的space complexity，但是
### 查找过程中hashmap的time complexity就是O(1) （average time complexity）,就算即使是出现了hash冲突的情况，最坏的查找时间复杂度也是O(N)
### 存储空间复杂度：哈希映射的空间复杂度通常 O(n) 其中 n 是存储在映射中的元素数量。这是因为每个元素都需要一定的空间来存储，而且哈希映射的大小通常与其包含的元素数量成正比。
### 思路：创建一个字典（哈希表）”dic“，用for循环去遍历这个list当中的所有元素,在每次iteration开始的时候，把ans的结果储存为target - nums[i]，然后在判断这个ans是不是在字里
### 如果字典里没有，就添加到dic里，再执行下一个iteration，但如果找到了，也就是说，有这样的一个元素，是和ans的值相加等于target（这里写的是target-nums[i]），就返回
### ，注意，这里的返回值是[dic[ans], i]，我们这里的一个重要思路是，返回元素的键值，也就是数组列表的下标，从而实现返回元素的一个过程。这里的意思就是如果找到了ans，也就是两数
### 之和等于target的那个结果，就返回ans元素的下标。（如果直接返回ans就是返回的元素，不是下标）
###


```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in dic:
                return [dic[ans], i]
            dic[nums[i]] = i
'''
